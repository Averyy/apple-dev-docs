# cancelAuthorization(with:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Tells your request handler to cancel the authorization of the given request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func cancelAuthorization(with request: ASAuthorizationProviderExtensionAuthorizationRequest)
```

```objc
- (void) cancelAuthorizationWithRequest:(ASAuthorizationProviderExtensionAuthorizationRequest *) request;
```

#### Discussion

The system calls this method on the main thread.

## Parameters

- `request`: The request to cancel.

## See Also

### Starting or Canceling a Request
- [func beginAuthorization(with: ASAuthorizationProviderExtensionAuthorizationRequest)](./beginauthorization%28with%29.md)
  Tells your request handler to authorize the given request.
- [class ASAuthorizationProviderExtensionAuthorizationRequest](../asauthorizationproviderextensionauthorizationrequest.md)
  An authorization request that your provider extension handles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequesthandler/cancelauthorization(with:))*