# ASAuthorizationProviderExtensionRegistrationHandler

**Framework**: Authentication Services  
**Kind**: protocol

An interface through which a single sign-on (SSO) authentication provider extension registers users and devices for platform SSO.

**Availability**:
- macOS 13.0+

## Declaration

```swift
protocol ASAuthorizationProviderExtensionRegistrationHandler : NSObjectProtocol
```

## Mentions

- [Registering devices and users](registering-devices-and-users.md)

## Topics

### Registering users and devices
- [func beginDeviceRegistration(loginManager: ASAuthorizationProviderExtensionLoginManager, options: ASAuthorizationProviderExtensionRequestOptions, completion: (ASAuthorizationProviderExtensionRegistrationResult) -> Void)](asauthorizationproviderextensionregistrationhandler/begindeviceregistration(loginmanager:options:completion:).md)
  Initiates the device registration process for the single sign-on extension.
- [func beginUserRegistration(loginManager: ASAuthorizationProviderExtensionLoginManager, userName: String?, method: ASAuthorizationProviderExtensionAuthenticationMethod, options: ASAuthorizationProviderExtensionRequestOptions, completion: (ASAuthorizationProviderExtensionRegistrationResult) -> Void)](asauthorizationproviderextensionregistrationhandler/beginuserregistration(loginmanager:username:method:options:completion:).md)
  Initiates the user registration process for the user and the single sign-on extension.
- [func registrationDidComplete()](asauthorizationproviderextensionregistrationhandler/registrationdidcomplete.md)
  Calls the extension to allow it to complete registration.
### Instance Methods
- [func protocolVersion() -> ASAuthorizationProviderExtensionPlatformSSOProtocolVersion](asauthorizationproviderextensionregistrationhandler/protocolversion.md)
- [func registrationDidCancel()](asauthorizationproviderextensionregistrationhandler/registrationdidcancel.md)
- [func supportedGrantTypes() -> ASAuthorizationProviderExtensionSupportedGrantTypes](asauthorizationproviderextensionregistrationhandler/supportedgranttypes.md)
- [func displayNames(forGroups: [String], using: ASAuthorizationProviderExtensionLoginManager, completion: ([String : String]) -> Void)](asauthorizationproviderextensionregistrationhandler/displaynames(forgroups:using:completion:).md)
- [func keyWillRotate(for: ASAuthorizationProviderExtensionKeyType, newKey: SecKey, loginManager: ASAuthorizationProviderExtensionLoginManager, completion: (Bool) -> Void)](asauthorizationproviderextensionregistrationhandler/keywillrotate(for:newkey:loginmanager:completion:).md)
- [func profilePictureForUser(using: ASAuthorizationProviderExtensionLoginManager, completion: (Data) -> Void)](asauthorizationproviderextensionregistrationhandler/profilepictureforuser(using:completion:).md)
### Instance Properties
- [var supportedDeviceEncryptionAlgorithms: [ASAuthorizationProviderExtensionEncryptionAlgorithm]](asauthorizationproviderextensionregistrationhandler/supporteddeviceencryptionalgorithms.md)
- [var supportedDeviceSigningAlgorithms: [ASAuthorizationProviderExtensionSigningAlgorithm]](asauthorizationproviderextensionregistrationhandler/supporteddevicesigningalgorithms.md)
- [var supportedUserSecureEnclaveKeySigningAlgorithms: [ASAuthorizationProviderExtensionSigningAlgorithm]](asauthorizationproviderextensionregistrationhandler/supportedusersecureenclavekeysigningalgorithms.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating extensions that support Platform SSO](creating-extensions-that-support-platform-sso.md)
  Configure capabilities and authentication options for extensions.
- [Registering devices and users](registering-devices-and-users.md)
  Implement device and user registration.
- [enum ASAuthorizationProviderExtensionAuthenticationMethod](asauthorizationproviderextensionauthenticationmethod.md)
  The platform single sign-on method for the user.
- [struct ASAuthorizationProviderExtensionRequestOptions](asauthorizationproviderextensionrequestoptions.md)
  The options for the extension to obtain the status of the registration.
- [enum ASAuthorizationProviderExtensionRegistrationResult](asauthorizationproviderextensionregistrationresult.md)
  The registration result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationhandler)*