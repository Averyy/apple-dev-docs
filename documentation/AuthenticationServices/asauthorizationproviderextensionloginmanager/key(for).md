# key(for:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Retrieves the key for the specified platform single sign-on key type.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func key(for keyType: ASAuthorizationProviderExtensionKeyType) -> SecKey?
```

```objc
- (SecKeyRef) copyKeyForKeyType:(ASAuthorizationProviderExtensionKeyType) keyType;
```

## Mentions

- [Configuring authentication with the identity provider (IdP)](../configuring-authentication-with-the-identity-provider-idp.md)

## Return Value

The key identity if it exists, or `nil` if it doesn’t.

## Parameters

- `keyType`: The key type to retrieve.

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
- [func userNeedsReauthentication(completion: ((any Error)?) -> Void)](./userneedsreauthentication%28completion%29.md)
  Requests platform single sign-on to reauthenticate the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/key(for:))*