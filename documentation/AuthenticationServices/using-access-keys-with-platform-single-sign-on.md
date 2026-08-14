# Using access keys with Platform Single Sign-on

**Framework**: Authentication Services

Authenticate users with access keys stored in Apple Wallet.

#### Overview

Platform Single Sign-on (Platform SSO) configured for Authenticated Guest Mode with Tap to Login supports authentication using an access key within Apple Wallet. With this configuration, users log in on a shared Mac with just the tap of their iPhone or Apple Watch on a supported NFC reader.

#### Explore How Access Keys Work with Platform Sso

Access keys consist of a credential stored in the Secure Element of supported iPhone and Apple Watch devices and a pass available to users within Apple Wallet. When the reader prompts users to authenticate with an access key, Apple Wallet selects the right key — and, if the key supports Express Mode and the user has turned it on, presents it automatically.

Apple Wallet and the reader terminal communicate using the Aliro protocol for authenticated and encrypted communication over Near Field Communication (NFC).

Access key creation and management require Credential Manager functionality and participation in the [`Apple Wallet Access Program`](https://developer.apple.comhttps://learn.wallet.apple/keys). The Credential Manager integrates with the Apple Access Platform and issues the access key pass shown in Apple Wallet. For example, an identity provider or physical access provider can act as a Credential Manager. For more information on how to join this program, see the [`Apple Wallet Access Program Guide`](https://developer.apple.comhttps://register.apple.com/resources/docs/apple-pay/access/program-guide/overview/).

Before provisioning any keys, the user must sign in with their Managed Apple Account or Apple Account on a compatible iPhone and turn on two-factor authentication. Student IDs are an exception and don’t require two-factor authentication.

#### Secure Access Keys

Access keys in Apple Wallet take full advantage of the privacy and security built into iPhone and Apple Watch because the device’s Secure Element stores their credentials. This makes them hardware-backed and encrypted, and helps to protect them from tampering and extraction attempts.

Apple Wallet never shares when or where a person uses their keys with Apple, and Apple servers never store that information.

For more information, see [`Access using Apple Wallet`](https://developer.apple.comhttps://support.apple.com/guide/security/sec75f6d5040) in the Apple Platform Security guide.

#### Provision Access Keys

A user creates an access key through the following process that the Credential Manager provides:

1. A user opens the app or website of the Credential Manager.
2. The user authenticates with the identity provider using their organizational credentials. After successful authentication, the app or website shows an Add to Wallet button. For more information, see [`Access Passes`](https://developer.apple.comhttps://register-docs.apple.com/apple-pay/access/program-guide/overview/access-passes/) in the Apple Wallet Access Program.
3. The user selects the Add to Wallet button, which instructs the Credential Manager to create, encrypt, and provide provisioning information to the device using the Apple Access Platform.

The provisioning information includes:

- The user name of the authenticated user
- The reader identifier
- The certificate authority (CA) — reader identities need to chain up to the CA to be trusted

The Apple Access Platform uses the provisioning information to inform the device to generate a private and public key within the Secure Element. The Secure Element creates the private key from its onboard true random number generator (TRNG). You can’t import or export the key. The device also stores the provisioning information alongside the keys in the Secure Element.

The device then provides the public key and an attestation to the Credential Manager. The attestation provides strong assurances that the device is a genuine Apple device and that a Secure Element generated the key.

The Credential Manager finalizes the access key pass and includes card art and user information. The Credential Manager also forwards the public key to the identity provider for association with the user account.

The Credential Manager uses the Apple Access Platform to provide the access key pass securely back to the device. The device stores the access key pass and makes it available in Wallet.

#### Configure the Nfc Reader

Use the [`ExtensibleSSO`](https://developer.apple.com/documentation/devicemanagement/extensiblesso) configuration or the [`ExtensibleSingleSignOn`](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon) profile to configure what the reader attached to the Mac uses for the NFC transaction.

The configuration specifies:

- The `AccessKeyReaderGroupIdentifier`
- The identity the reader terminal uses
- The root CA that issued the identity — the reader identity needs to chain up to this CA
- Whether the reader turns on Express Mode

For more information, see [`Configuring Platform Single Sign-on`](https://developer.apple.com/documentation/devicemanagement/configuring-platform-single-sign-on).

#### Use Access Keys

Each NFC transaction consists of multiple phases.

##### Poll the Reader

The NFC reader broadcasts the contactless polling loop and waits for an eligible device using the Enhanced Contactless Polling (ECP) protocol from Apple.

The ECP protocol enables the NFC reader to broadcast various configuration and capability information in the contactless polling loop to Apple devices before the transaction initiates. This information includes values such as the `AccessKeyReaderGroupIdentifier` that the extensible SSO configuration provides and the Terminal Capabilities Identifier (TCI). The TCI includes information like support for Express Mode.

##### Initiate the Transaction

When within range of the NFC reader, the device listens to the contactless polling loop to receive the ECP settings of the reader.

Using the `AccessKeyReaderGroupIdentifier` that the ECP message provides, the device looks for matching access keys to identify the relevant access key pass to display.

- If a single access key is relevant, Apple Wallet automatically selects it for the transaction, and if Express Mode is turned on, also performs the transaction automatically. This is the most common use case.
- If multiple access keys are relevant and Express Mode is turned on, Apple Wallet automatically selects the one set for use with Express Mode.
- If multiple access keys are relevant and Express Mode is turned off, users can select an access key manually before the transaction.

##### Perform the Transaction

The device verifies the reader identity up to the root CA that the Credential Manager provisions. If the checks pass, the device uses the provisioned key material. Otherwise, if the device can’t verify the reader identity, it uses random ephemeral key material instead.

The reader and the device perform a contactless transaction using the Aliro protocol. At the beginning of the transaction, Platform SSO requests a one-time code from the identity provider, which becomes part of an embedded assertion. The device signs the assertion with the private key.

##### Decide on the Requested Access

The reader provides the Platform SSO extension with the user name and public key from the access key pass as well as a signed embedded assertion. The extension sends them back to the identity provider to authorize or deny access.

> **Note**:  The identity provider decides whether to authorize the user based on the provided credential and provides the decision back to Platform SSO. The Apple Access Platform isn’t involved in this authorization process.

#### Decommission an Access Key

An access key might become obsolete — for example, when a user loses their device or the identity provider deactivates the user account. In those cases, the identity provider initiates the following process:

- The identity provider invalidates the key, which immediately blocks further authentication.
- The identity provider instructs the Credential Manager to unlink and clean up the access key.
- The Credential Manager notifies the Apple Access Platform to unlink the access key on a specific device.
- The Apple Access Platform sends a request to the device to delete the key material from the Secure Element.

## See Also

- [Authentication process](authentication-process.md)
  Use a system-supported method to authenticate with an identity provider.
- [Implementing web-based authentication with Platform Single Sign-on](implementing-web-based-authentication.md)
  Support modern, phishing-resistant, and flexible authentication methods.
- [class ASAuthorizationProviderExtensionKerberosMapping](asauthorizationproviderextensionkerberosmapping.md)
  A set of Kerberos mappings that the system login process uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/using-access-keys-with-platform-single-sign-on)*