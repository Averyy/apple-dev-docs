# Local Authentication

**Framework**: Local Authentication  
**Kind**: module

Authenticate users biometrically or with a passphrase they already know.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

Many users rely on biometric authentication like Face ID, Touch ID, or Optic ID to enable secure, effortless access to their devices. As a fallback option, and for devices without biometry, a passcode or password serves a similar purpose. Use the LocalAuthentication framework to leverage these mechanisms in your app and extend authentication procedures your app already implements.

![Diagram showing the relationship between your app operating in user space, the LocalAuthentication framework in the operating system, and the Secure Enclave.](https://docs-assets.developer.apple.com/published/cde4c45af06ae6fcc524c80cf6215e94/media-3002744%402x.png)

To maximize security, your app never gains access to any of the underlying authentication data. You can’t access any fingerprint images, for example. The Secure Enclave, a hardware-based security processor isolated from the rest of the system, manages this data out of reach even of the operating system. Instead, you specify a particular policy and provide messaging that tells the user why you want them to authenticate. The framework then coordinates with the Secure Enclave to carry out the operation. Afterward, you receive only a Boolean result indicating authentication success or failure.

## Topics

### Essentials
- [Logging a User into Your App with Face ID or Touch ID](logging-a-user-into-your-app-with-face-id-or-touch-id.md)
  Supplement your own authentication scheme with biometric authentication, making it easy for users to access sensitive parts of your app.
- [Accessing Keychain Items with Face ID or Touch ID](accessing-keychain-items-with-face-id-or-touch-id.md)
  Protect a keychain item with biometric authentication.
### Authentication and access
- [class LARight](laright.md)
  A grouped set of requirements that gate access to a resource or operation.
- [LARight.State](laright/state-swift.enum.md)
  The possible states for a right during authorization.
- [class LAContext](lacontext.md)
  A mechanism for evaluating authentication policies and access controls.
### Persistence
- [class LARightStore](larightstore.md)
  A container for data protected by a right.
- [class LAPersistedRight](lapersistedright.md)
  A right that gates access to a key and a secret.
- [class LASecret](lasecret.md)
  Data that’s protected by a persisted right.
### Key pairs
- [class LAPublicKey](lapublickey.md)
  The public portion of an asymmetric key pair.
- [class LAPrivateKey](laprivatekey.md)
  The private portion of an asymmetric key pair.
### Requirements
- [class LAAuthenticationRequirement](laauthenticationrequirement.md)
  A set of requirements that protect a right.
- [class LABiometryFallbackRequirement](labiometryfallbackrequirement.md)
  A set of requirements to fall back on if biometrics aren’t present.
### Authentication views
- [struct LocalAuthenticationView](localauthenticationview.md)
  A SwiftUI view that displays an authentication interface.
### Errors
- [struct LAError](laerror-swift.struct.md)
  Errors issued by the LocalAuthentication framework.
- [LAError.Code](laerror-swift.struct/code.md)
  Errors issued by the LocalAuthentication framework.
- [let LAErrorDomain: String](laerrordomain.md)
  The error domain that the framework uses when issuing errors.
### Reference
- [LocalAuthentication Constants](localauthentication-constants.md)
### Classes
- [class LADomainState](ladomainstate.md)
- [class LADomainStateBiometry](ladomainstatebiometry.md)
- [class LADomainStateCompanion](ladomainstatecompanion.md)
- [class LAEnvironment](laenvironment.md)
### Variables
- [var kLAAccessControlOperationCreateItem: Int32](klaaccesscontroloperationcreateitem.md)
- [var kLAAccessControlOperationCreateKey: Int32](klaaccesscontroloperationcreatekey.md)
- [var kLAAccessControlOperationUseItem: Int32](klaaccesscontroloperationuseitem.md)
- [var kLAAccessControlOperationUseKeyDecrypt: Int32](klaaccesscontroloperationusekeydecrypt.md)
- [var kLAAccessControlOperationUseKeyKeyExchange: Int32](klaaccesscontroloperationusekeykeyexchange.md)
- [var kLAAccessControlOperationUseKeySign: Int32](klaaccesscontroloperationusekeysign.md)
- [var kLACompanionTypeMac: Int32](klacompaniontypemac.md)
- [var kLACompanionTypeWatch: Int32](klacompaniontypewatch.md)
- [var kLAErrorCompanionNotAvailable: Int32](klaerrorcompanionnotavailable.md)
- [var kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrCompanion: Int32](klapolicydeviceownerauthenticationwithbiometricsorcompanion.md)
- [var kLAPolicyDeviceOwnerAuthenticationWithCompanion: Int32](klapolicydeviceownerauthenticationwithcompanion.md)
### Enumerations
- [enum LACompanionType](lacompaniontype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/LocalAuthentication)*