# requestAuthorizationForPublicKeyCredentials(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Requests a person’s permission to use their passkeys.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
func requestAuthorizationForPublicKeyCredentials(_ completionHandler: @escaping @Sendable (ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState) -> Void)
```

```swift
func requestAuthorizationForPublicKeyCredentials() async -> ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState
```

```objc
- (void) requestAuthorizationForPublicKeyCredentials:(void (^)(ASAuthorizationWebBrowserPublicKeyCredentialManagerAuthorizationState authorizationState)) completionHandler;
```

## Mentions

- [Authenticating people by using passkeys in browser apps](../authenticating-people-by-using-passkeys-in-browser-apps.md)

## Parameters

- `completionHandler`: A block you provide that the operating system calls when the request is completed.

## See Also

### Requesting access to passkeys
- [var authorizationStateForPlatformCredentials: ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState](./authorizationstateforplatformcredentials.md)
  Returns a value that indicates whether the browser app has access to a person’s passkeys.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState](./authorizationstate.md)
  An enumeration of values that indicate whether the browser app has access to a person’s passkeys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager/requestauthorizationforpublickeycredentials(_:))*