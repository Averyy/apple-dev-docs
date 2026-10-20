# userNeedsReauthentication(completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Requests platform single sign-on to reauthenticate the current user.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func userNeedsReauthentication(completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func userNeedsReauthentication() async throws
```

```objc
- (void) userNeedsReauthenticationWithCompletion:(void (^)(NSError *error)) completion;
```

#### Discussion

Use this method to request reauthentication, such as when revoking or expiring tokens.

## Parameters

- `completion`: The completion with the error, if any.

## See Also

### Performing authentication
- [enum ASAuthorizationProviderExtensionKeyType](../asauthorizationproviderextensionkeytype.md)
  The key types for platform single sign-on.
- [var isDeviceRegistered: Bool](./isdeviceregistered.md)
  A Boolean value that indicates whether the device completes registration.
- [var isUserRegistered: Bool](./isuserregistered.md)
  A Boolean value that indicates whether the user completes registration.
- [var loginConfiguration: ASAuthorizationProviderExtensionLoginConfiguration?](./loginconfiguration.md)
  The current login configuration for the extension.
- [var ssoTokens: [AnyHashable : Any]?](./ssotokens.md)
  The single sign-on response tokens for the current user and extension.
- [func identity(for: ASAuthorizationProviderExtensionKeyType) -> SecIdentity?](./identity%28for%29.md)
  Retrieves the identity for the specified platform single sign-on key type.
- [func key(for: ASAuthorizationProviderExtensionKeyType) -> SecKey?](./key%28for%29.md)
  Retrieves the key for the specified platform single sign-on key type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/userneedsreauthentication(completion:))*