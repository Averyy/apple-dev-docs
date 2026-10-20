# ASAuthorizationProviderExtensionLoginManager

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

An interface to maintain platform single sign-on (SSO) during authentication and registration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class ASAuthorizationProviderExtensionLoginManager
```

```objc
@interface ASAuthorizationProviderExtensionLoginManager : NSObject
```

## Mentions

- [Configuring authentication with the identity provider (IdP)](./configuring-authentication-with-the-identity-provider-idp.md)

#### Overview

Use this class to perform registration and authentication tasks, and to repair registrations.

## Topics

### Performing registration
- [var loginUserName: String?](./asauthorizationproviderextensionloginmanager/loginusername.md)
  The user name to use when authenticating with the identity provider.
- [var registrationToken: String?](./asauthorizationproviderextensionloginmanager/registrationtoken.md)
  The device registration token from the mobile device management profile.
- [func presentRegistrationViewController(completion: ((any Error)?) -> Void)](./asauthorizationproviderextensionloginmanager/presentregistrationviewcontroller%28completion%29.md)
  Requests platform single sign-on to show the extension’s view controller to the user.
- [func saveCertificate(SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)](./asauthorizationproviderextensionloginmanager/savecertificate%28_,keytype%29.md)
  Saves the provided certificate for the key type.
- [func saveLoginConfiguration(ASAuthorizationProviderExtensionLoginConfiguration) throws](./asauthorizationproviderextensionloginmanager/saveloginconfiguration%28_%29.md)
  Saves or replaces the login configuration.
### Performing authentication
- [enum ASAuthorizationProviderExtensionKeyType](./asauthorizationproviderextensionkeytype.md)
  The key types for platform single sign-on.
- [var isDeviceRegistered: Bool](./asauthorizationproviderextensionloginmanager/isdeviceregistered.md)
  A Boolean value that indicates whether the device completes registration.
- [var isUserRegistered: Bool](./asauthorizationproviderextensionloginmanager/isuserregistered.md)
  A Boolean value that indicates whether the user completes registration.
- [var loginConfiguration: ASAuthorizationProviderExtensionLoginConfiguration?](./asauthorizationproviderextensionloginmanager/loginconfiguration.md)
  The current login configuration for the extension.
- [var ssoTokens: [AnyHashable : Any]?](./asauthorizationproviderextensionloginmanager/ssotokens.md)
  The single sign-on response tokens for the current user and extension.
- [func identity(for: ASAuthorizationProviderExtensionKeyType) -> SecIdentity?](./asauthorizationproviderextensionloginmanager/identity%28for%29.md)
  Retrieves the identity for the specified platform single sign-on key type.
- [func key(for: ASAuthorizationProviderExtensionKeyType) -> SecKey?](./asauthorizationproviderextensionloginmanager/key%28for%29.md)
  Retrieves the key for the specified platform single sign-on key type.
- [func userNeedsReauthentication(completion: ((any Error)?) -> Void)](./asauthorizationproviderextensionloginmanager/userneedsreauthentication%28completion%29.md)
  Requests platform single sign-on to reauthenticate the current user.
### Repairing registrations
- [func userRegistrationsNeedsRepair()](./asauthorizationproviderextensionloginmanager/userregistrationsneedsrepair%28%29.md)
  Invokes the user registration to run again so the current user can repair it.
- [func deviceRegistrationsNeedsRepair()](./asauthorizationproviderextensionloginmanager/deviceregistrationsneedsrepair%28%29.md)
  Invokes the device registration to run again so the current user can repair it.
- [func resetKeys()](./asauthorizationproviderextensionloginmanager/resetkeys%28%29.md)
  Creates new encryption, signing, and Secure Enclave keys.
### Instance Properties
- [var extensionData: [AnyHashable : Any]](./asauthorizationproviderextensionloginmanager/extensiondata.md)
- [var userLoginConfiguration: ASAuthorizationProviderExtensionUserLoginConfiguration?](./asauthorizationproviderextensionloginmanager/userloginconfiguration.md)
- [var authenticationMethod: ASAuthorizationProviderExtensionAuthenticationMethod](./asauthorizationproviderextensionloginmanager/authenticationmethod.md)
### Instance Methods
- [func decryptionKeysNeedRepair()](./asauthorizationproviderextensionloginmanager/decryptionkeysneedrepair%28%29.md)
- [func resetDeviceKeys()](./asauthorizationproviderextensionloginmanager/resetdevicekeys%28%29.md)
- [func resetUserSecureEnclaveKey()](./asauthorizationproviderextensionloginmanager/resetusersecureenclavekey%28%29.md)
- [func saveUserLoginConfiguration(ASAuthorizationProviderExtensionUserLoginConfiguration) throws](./asauthorizationproviderextensionloginmanager/saveuserloginconfiguration%28_%29.md)
- [func attestKey(ofType: ASAuthorizationProviderExtensionKeyType, clientDataHash: Data) async throws -> [SecCertificate]](./asauthorizationproviderextensionloginmanager/attestkey%28oftype,clientdatahash%29.md)
- [func attestPendingKey(ofType: ASAuthorizationProviderExtensionKeyType, clientDataHash: Data) async throws -> [SecCertificate]](./asauthorizationproviderextensionloginmanager/attestpendingkey%28oftype,clientdatahash%29.md)
- [func beginKeyRotation(ASAuthorizationProviderExtensionKeyType) -> SecKey?](./asauthorizationproviderextensionloginmanager/beginkeyrotation%28_%29.md)
- [func completeKeyRotation(ASAuthorizationProviderExtensionKeyType)](./asauthorizationproviderextensionloginmanager/completekeyrotation%28_%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuration
- [Configuring authentication with the identity provider (IdP)](./configuring-authentication-with-the-identity-provider-idp.md)
  Specify how Platform SSO authenticates with the identity provider.
- [Interpreting Platform Single Sign-on authorization scopes](./interpreting-platform-single-sign-on-authorization-scopes.md)
  Use authorization scopes to apply authentication policies.
- [class ASAuthorizationProviderExtensionLoginConfiguration](./asauthorizationproviderextensionloginconfiguration.md)
  An interface for configuring platform single sign-on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager)*