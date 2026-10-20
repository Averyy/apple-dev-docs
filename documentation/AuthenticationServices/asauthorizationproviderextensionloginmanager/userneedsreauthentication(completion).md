# userNeedsReauthentication(completion:)

**Framework**: Authentication Services  
**Kind**: method

Requests platform single sign-on to reauthenticate the current user.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func userNeedsReauthentication() async throws
```

#### Discussion

Use this method to request reauthentication, such as when revoking or expiring tokens.

## Parameters

- `completion`: The completion with the error, if any.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/userneedsreauthentication(completion:))*