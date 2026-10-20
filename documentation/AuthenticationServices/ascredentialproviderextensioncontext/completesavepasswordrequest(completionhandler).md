# completeSavePasswordRequest(completionHandler:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Signal that a password request was successfully saved.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
func completeSavePasswordRequest(completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func completeSavePasswordRequest() async -> Bool
```

```objc
- (void) completeSavePasswordRequestWithCompletionHandler:(void (^)(BOOL expired)) completionHandler;
```

#### Discussion

> **Note**: You are responsible for updating the ASCredentialIdentityStore.

## Parameters

- `completionHandler`: An optional block your extension can provide to perform any cleanup work after the system has captured the results. The expired parameter is true if the system decides to prematurely end a previous non-expiration invocation of the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext/completesavepasswordrequest(completionhandler:))*