# isDeviceRegistered

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device completes registration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var isDeviceRegistered: Bool { get }
```

```objc
@property (readonly, getter=isDeviceRegistered) BOOL deviceRegistered;
```

## Discussion

Returns [`true`](../../Swift/true.md) if the current device completes registration.

## See Also

### Performing authentication
- [enum ASAuthorizationProviderExtensionKeyType](../asauthorizationproviderextensionkeytype.md)
  The key types for platform single sign-on.
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
- [func userNeedsReauthentication(completion: ((any Error)?) -> Void)](./userneedsreauthentication%28completion%29.md)
  Requests platform single sign-on to reauthenticate the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/isdeviceregistered)*