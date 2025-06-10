# ASAuthorizationProviderExtensionKeyType

**Framework**: Authentication Services  
**Kind**: enum

The key types for platform single sign-on.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum ASAuthorizationProviderExtensionKeyType
```

## Topics

### Identifying the key types
- [ASAuthorizationProviderExtensionKeyType.userDeviceEncryption](asauthorizationproviderextensionkeytype/userdeviceencryption.md)
  The user device encryption key.
- [ASAuthorizationProviderExtensionKeyType.userDeviceSigning](asauthorizationproviderextensionkeytype/userdevicesigning.md)
  The user device signing key.
- [ASAuthorizationProviderExtensionKeyType.userSecureEnclaveKey](asauthorizationproviderextensionkeytype/usersecureenclavekey.md)
  The user Secure Enclave key.
### Enumeration Cases
- [ASAuthorizationProviderExtensionKeyType.currentDeviceEncryption](asauthorizationproviderextensionkeytype/currentdeviceencryption.md)
- [ASAuthorizationProviderExtensionKeyType.currentDeviceSigning](asauthorizationproviderextensionkeytype/currentdevicesigning.md)
- [ASAuthorizationProviderExtensionKeyType.sharedDeviceEncryption](asauthorizationproviderextensionkeytype/shareddeviceencryption.md)
- [ASAuthorizationProviderExtensionKeyType.sharedDeviceSigning](asauthorizationproviderextensionkeytype/shareddevicesigning.md)
- [ASAuthorizationProviderExtensionKeyType.userSmartCard](asauthorizationproviderextensionkeytype/usersmartcard.md)
### Initializers
- [init?(rawValue: Int)](asauthorizationproviderextensionkeytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionkeytype)*