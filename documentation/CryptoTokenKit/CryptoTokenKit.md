# CryptoTokenKit

**Framework**: CryptoTokenKit  
**Kind**: module

Access security tokens and the cryptographic assets they store.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

#### Overview

You use the CryptoTokenKit framework to easily access cryptographic tokens. Tokens are physical devices built in to the system, located on attached hardware (like a smart card), or accessible through a network connection. Tokens store cryptographic objects like keys and certificates. They also may perform operations—for example, encryption or digital signature verification—using these objects. You use the framework to work with a token’s assets as if they were part of your system, even though they remain secured by the token.

You can also use the framework to enable a token for two-factor authentication in macOS. Authentication services manage associations between users and identities stored on a token, granting users access when the appropriate token is present and unlocked. You supply a token driver in the form of an app extension that bridges the gap between authentication services and the underlying token hardware.

Starting in macOS 10.15.4, the CryptoTokenKit framework includes support for always-available tokens, referred to as persistent tokens. Persistent token support provides access to tokens from Hardware Security Modules (HSMs). The app hosting the token extension allows the system to address and use available tokens, address and use identities available by accessing tokens, and to access additional configuration information about tokens. Persistent tokens aren’t suitable for validating a user login because they’re available on a per-user basis, and therefore aren’t accessible until after the user logs in.

> **Note**:  When you want to manage the associations between users and tokens on a given computer, use the `sc_auth` command line utility. See the `sc_auth(8)` man page for details.

## Topics

### Smart Cards
- [Using Cryptographic Assets Stored on a Smart Card](using-cryptographic-assets-stored-on-a-smart-card.md)
  Access certificates, keys, and identities stored on a smart card as if they were part of the keychain.
- [class TKSmartCardSlotManager](tksmartcardslotmanager.md)
  An interface to all available smart card reader slots.
- [class TKSmartCardSlot](tksmartcardslot.md)
  A single smart card reader slot in the system.
- [class TKSmartCard](tksmartcard.md)
  A representation of a smart card.
### Smart Card App Extensions
- [Authenticating Users with a Cryptographic Token](authenticating-users-with-a-cryptographic-token.md)
  Grant access to user accounts and the keychain by creating a smart card app extension.
- [Configuring Smart Card Authentication](configuring-smart-card-authentication.md)
  Set preferences for smart card authentication operations, including those on managed devices.
- [class TKSmartCardTokenDriver](tksmartcardtokendriver.md)
  The driver that acts as an entry point for smart card app extensions.
- [class TKSmartCardToken](tksmartcardtoken.md)
  A representation of a smart card based cryptographic token.
- [class TKSmartCardTokenSession](tksmartcardtokensession.md)
  A token session that is based on a smart card token.
### Tokens
- [class TKTokenWatcher](tktokenwatcher.md)
  An object that tracks the tokens available in the system.
- [class TKTokenDriver](tktokendriver.md)
  A base class for building token drivers.
- [class TKToken](tktoken.md)
  A representation of a hardware-based cryptographic token.
- [class TKTokenSession](tktokensession.md)
  A token session that manages the authentication state of a token.
### Errors
- [struct TKError](tkerror.md)
  An error specific to the CryptoTokenKit framework.
- [let TKErrorDomain: String](tkerrordomain.md)
  The domain for all CryptoTokenKit framework errors.
- [TKError.Code](tkerror/code.md)
  Error codes from CryptoTokenKit.
### Classes
- [class TKSmartCardSlotNFCSession](tksmartcardslotnfcsession.md)
  NFC session that’s related to NFC smart card slot which was created.
- [class TKSmartCardTokenRegistrationManager](tksmartcardtokenregistrationmanager.md)
  Provides a centralized management system for registering and unregistering smartcards using their token IDs.
### Type Aliases
- [typealias IntermediateKeyAuthenticator](intermediatekeyauthenticator.md)
- [typealias TKTokenObjectID](tktokenobjectid-8mo7f.md)
### Enumerations
- [enum IKeyAuthenticator](ikeyauthenticator.md)
- [enum IKeyErrorCodes](ikeyerrorcodes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CryptoTokenKit)*