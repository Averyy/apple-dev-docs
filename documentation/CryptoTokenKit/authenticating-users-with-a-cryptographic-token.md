# Authenticating Users with a Cryptographic Token

**Framework**: CryptoTokenKit

Grant access to user accounts and the keychain by creating a smart card app extension.

#### Overview

A typical use of hardware-based cryptographic tokens is two-factor authentication. This kind of authentication enhances security by making users establish their identity in two ways: with something they have (like a token that’s a USB-based smart card) and with something they know (a password that unlocks the token). A misplaced token is useless without the password. A compromised password provides no access without the physical token.

In macOS, you can write an app extension that enables the system to authenticate users possessing a token. A driver you supply allows the system to establish the presence of the token in the system and confirm that the user has a password or PIN that unlocks the token.

##### Ensure the Token Meets Minimum Requirements

Before writing the app extension, make sure the token you’re trying to support meets certain basic prerequisites. To do this, you may need to obtain technical documentation from the token’s manufacturer. The exact requirements depend on how you plan to use it.

To authenticate user logins, the token must contain at least one cryptographic key. This key must be capable of creating a cryptographic signature using an algorithm from one of the following families:

- Elliptic curve signature digest X962
- RSA signature digest PSS
- RSA signature digest PKCS1v15

Additionally, to use the token for unlocking the keychain, make sure it contains at least one of the following keys:

- A 256-bit elliptic curve key of type [`kSecAttrKeyTypeECSECPrimeRandom`](https://developer.apple.com/documentation/Security/kSecAttrKeyTypeECSECPrimeRandom). This key must support the [`ecdhKeyExchangeStandard`](https://developer.apple.com/documentation/Security/SecKeyAlgorithm/ecdhKeyExchangeStandard) key exchange algorithm.
- A 2048-, 3072-, or 4096-bit RSA key of type [`kSecAttrKeyTypeRSA`](https://developer.apple.com/documentation/Security/kSecAttrKeyTypeRSA). This key must support decryption with the [`rsaEncryptionOAEPSHA256`](https://developer.apple.com/documentation/Security/SecKeyAlgorithm/rsaEncryptionOAEPSHA256) algorithm.

To support an RSA option in either of the above use cases, the token hardware must either implement the specific RSA signature or decryption algorithm that the key supports, or simply implement the raw variant ([`rsaSignatureRaw`](https://developer.apple.com/documentation/Security/SecKeyAlgorithm/rsaSignatureRaw) for login, or [`rsaEncryptionRaw`](https://developer.apple.com/documentation/Security/SecKeyAlgorithm/rsaEncryptionRaw) for keychain unlock). When the hardware provides only the raw operation, macOS automatically handles any needed padding.

##### Create the Smart Card App Extension

When you’re ready to begin coding, use Xcode to create an app extension target inside a new, empty macOS host app. Xcode provides a smart card app extension template that produces both the target and a group of files to get you started.

For example, for a token extension that you name `TokenExtension`, Xcode produces the target plus an entitlements file, an `Info.plist` file, and the three source files in a new folder within the project:

![Screenshot of Xcode showing the target and files generated from the smart card extension template.](https://docs-assets.developer.apple.com/published/4e427754f0434c685963118474d91ad4/media-2940047%402x.png)

For more information about working with app extensions in general, see [`App Extensions`](https://developer.apple.comhttps://developer.apple.com/app-extensions/).

> **Note**:  The host app for this kind of extension typically contains no functionality. Instead, it exists only as a delivery mechanism for the extension.

 The host app for this kind of extension typically contains no functionality. Instead, it exists only as a delivery mechanism for the extension.

A smart card app extension has no UI component. The system handles all user interaction associated with authenticating the user. Instead, your `TokenDriver` class—derived from the [`TKSmartCardTokenDriver`](tksmartcardtokendriver.md) class—acts as the entry point for the extension. More precisely, the `NSExtensionAttributes` subdictionary of the `NSExtension` dictionary in the `Info.plist` file has a key `com.apple.ctk.driver-class` that names the entry point class. Xcode sets this for you as part of the template:

![Screenshot of Xcode showing the Info.plist file of the TokenExtension, highlighting the driver class item.](https://docs-assets.developer.apple.com/published/fe4784f0d2bed0cb08f563bb05c4da01/media-2940045%402x.png)

You supply functionality for the `Token` class (derived from the [`TKSmartCardToken`](tksmartcardtoken.md) class) and `TokenSession` class (derived from the [`TKSmartCardTokenSession`](tksmartcardtokensession.md) class) that is specific to the token hardware you are supporting. These pieces work together to form the app extension:

![Diagram showing the interconnections between the user, authentication services, your app extension, and the external smart card.](https://docs-assets.developer.apple.com/published/5a882b84cfef7b2dfdec6c940a5428cc/media-2940884%402x.png)

##### Register the Extension with Securityagent

To activate the app extension and make the token available to the system for authentication, you launch the extension’s hosting app as the `_securityagent` user:

```shell
sudo -u _securityagent /Applications/HostApp.app/Contents/MacOS/HostApp
```

The system prompts for an administrative password before executing this call.

The hosting app may in fact do nothing more than exit cleanly, but the act of running it has the side effect of registering its app extension with the system. You only need to do this once, typically during a managed installation.

## See Also

- [Configuring Smart Card Authentication](configuring-smart-card-authentication.md)
  Set preferences for smart card authentication operations, including those on managed devices.
- [class TKSmartCardTokenDriver](tksmartcardtokendriver.md)
  The driver that acts as an entry point for smart card app extensions.
- [class TKSmartCardToken](tksmartcardtoken.md)
  A representation of a smart card based cryptographic token.
- [class TKSmartCardTokenSession](tksmartcardtokensession.md)
  A token session that is based on a smart card token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/authenticating-users-with-a-cryptographic-token)*