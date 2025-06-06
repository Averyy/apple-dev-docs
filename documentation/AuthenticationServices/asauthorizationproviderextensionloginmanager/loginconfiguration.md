# loginConfiguration

**Framework**: Authentication Services  
**Kind**: property

The current login configuration for the extension.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@NSCopying
var loginConfiguration: ASAuthorizationProviderExtensionLoginConfiguration? { get }
```

## See Also

- [enum ASAuthorizationProviderExtensionKeyType](asauthorizationproviderextensionkeytype.md)
  The key types for platform single sign-on.
- [var isDeviceRegistered: Bool](asauthorizationproviderextensionloginmanager/isdeviceregistered.md)
  A Boolean value that indicates whether the device completes registration.
- [var isUserRegistered: Bool](asauthorizationproviderextensionloginmanager/isuserregistered.md)
  A Boolean value that indicates whether the user completes registration.
- [var ssoTokens: [AnyHashable : Any]?](asauthorizationproviderextensionloginmanager/ssotokens.md)
  The single sign-on response tokens for the current user and extension.
- [func identity(for: ASAuthorizationProviderExtensionKeyType) -> SecIdentity?](asauthorizationproviderextensionloginmanager/identity(for:).md)
  Retrieves the identity for the specified platform single sign-on key type.
- [func key(for: ASAuthorizationProviderExtensionKeyType) -> SecKey?](asauthorizationproviderextensionloginmanager/key(for:).md)
  Retrieves the key for the specified platform single sign-on key type.
- [func userNeedsReauthentication(completion: ((any Error)?) -> Void)](asauthorizationproviderextensionloginmanager/userneedsreauthentication(completion:).md)
  Requests platform single sign-on to reauthenticate the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/loginconfiguration)*