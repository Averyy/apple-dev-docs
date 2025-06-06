# ASAuthorizationProviderExtensionLoginManager

**Framework**: Authentication Services  
**Kind**: class

An interface to maintain platform single sign-on (SSO) during authentication and registration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class ASAuthorizationProviderExtensionLoginManager
```

## Mentions

- [Configuring authentication with the identity provider (IdP)](configuring-authentication-with-the-identity-provider-idp.md)

#### Overview

Use this class to perform registration and authentication tasks, and to repair registrations.

## Topics

### Performing registration
- [var loginUserName: String?](asauthorizationproviderextensionloginmanager/loginusername.md)
  The user name to use when authenticating with the identity provider.
- [var registrationToken: String?](asauthorizationproviderextensionloginmanager/registrationtoken.md)
  The device registration token from the mobile device management profile.
- [func presentRegistrationViewController(completion: ((any Error)?) -> Void)](asauthorizationproviderextensionloginmanager/presentregistrationviewcontroller(completion:).md)
  Requests platform single sign-on to show the extension’s view controller to the user.
- [func saveCertificate(SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)](asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:).md)
  Saves the provided certificate for the key type.
- [func saveLoginConfiguration(ASAuthorizationProviderExtensionLoginConfiguration) throws](asauthorizationproviderextensionloginmanager/saveloginconfiguration(_:).md)
  Saves or replaces the login configuration.
### Performing authentication
- [enum ASAuthorizationProviderExtensionKeyType](asauthorizationproviderextensionkeytype.md)
  The key types for platform single sign-on.
- [var isDeviceRegistered: Bool](asauthorizationproviderextensionloginmanager/isdeviceregistered.md)
  A Boolean value that indicates whether the device completes registration.
- [var isUserRegistered: Bool](asauthorizationproviderextensionloginmanager/isuserregistered.md)
  A Boolean value that indicates whether the user completes registration.
- [var loginConfiguration: ASAuthorizationProviderExtensionLoginConfiguration?](asauthorizationproviderextensionloginmanager/loginconfiguration.md)
  The current login configuration for the extension.
- [var ssoTokens: [AnyHashable : Any]?](asauthorizationproviderextensionloginmanager/ssotokens.md)
  The single sign-on response tokens for the current user and extension.
- [func identity(for: ASAuthorizationProviderExtensionKeyType) -> SecIdentity?](asauthorizationproviderextensionloginmanager/identity(for:).md)
  Retrieves the identity for the specified platform single sign-on key type.
- [func key(for: ASAuthorizationProviderExtensionKeyType) -> SecKey?](asauthorizationproviderextensionloginmanager/key(for:).md)
  Retrieves the key for the specified platform single sign-on key type.
- [func userNeedsReauthentication(completion: ((any Error)?) -> Void)](asauthorizationproviderextensionloginmanager/userneedsreauthentication(completion:).md)
  Requests platform single sign-on to reauthenticate the current user.
### Repairing registrations
- [func userRegistrationsNeedsRepair()](asauthorizationproviderextensionloginmanager/userregistrationsneedsrepair.md)
  Invokes the user registration to run again so the current user can repair it.
- [func deviceRegistrationsNeedsRepair()](asauthorizationproviderextensionloginmanager/deviceregistrationsneedsrepair.md)
  Invokes the device registration to run again so the current user can repair it.
- [func resetKeys()](asauthorizationproviderextensionloginmanager/resetkeys.md)
  Creates new encryption, signing, and Secure Enclave keys for the user.
### Instance Properties
- [var extensionData: [AnyHashable : Any]](asauthorizationproviderextensionloginmanager/extensiondata.md)
- [var userLoginConfiguration: ASAuthorizationProviderExtensionUserLoginConfiguration?](asauthorizationproviderextensionloginmanager/userloginconfiguration.md)
### Instance Methods
- [func decryptionKeysNeedRepair()](asauthorizationproviderextensionloginmanager/decryptionkeysneedrepair.md)
- [func resetDeviceKeys()](asauthorizationproviderextensionloginmanager/resetdevicekeys.md)
- [func resetUserSecureEnclaveKey()](asauthorizationproviderextensionloginmanager/resetusersecureenclavekey.md)
- [func saveUserLoginConfiguration(ASAuthorizationProviderExtensionUserLoginConfiguration) throws](asauthorizationproviderextensionloginmanager/saveuserloginconfiguration(_:).md)
- [func attestKey(ofType: ASAuthorizationProviderExtensionKeyType, clientDataHash: Data) async throws -> [SecCertificate]](asauthorizationproviderextensionloginmanager/attestkey(oftype:clientdatahash:).md)
- [func attestPendingKey(ofType: ASAuthorizationProviderExtensionKeyType, clientDataHash: Data) async throws -> [SecCertificate]](asauthorizationproviderextensionloginmanager/attestpendingkey(oftype:clientdatahash:).md)
- [func beginKeyRotation(ASAuthorizationProviderExtensionKeyType) -> SecKey?](asauthorizationproviderextensionloginmanager/beginkeyrotation(_:).md)
- [func completeKeyRotation(ASAuthorizationProviderExtensionKeyType)](asauthorizationproviderextensionloginmanager/completekeyrotation(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Configuring Device Management](configuring-device-management.md)
  Configure Device Management to support device and user registration for platform SSO.
- [Configuring authentication with the identity provider (IdP)](configuring-authentication-with-the-identity-provider-idp.md)
  Specify how platform SSO authenticates with the identity provider.
- [class ASAuthorizationProviderExtensionLoginConfiguration](asauthorizationproviderextensionloginconfiguration.md)
  An interface for configuring platform single sign-on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager)*