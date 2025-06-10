# signalErrorResolved(_:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Indicates a resolved error.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func signalErrorResolved(_ error: any Error) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func signalErrorResolved(_ error: any Error) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method if any of your extension’s actions fail because of an [`NSFileProviderError.Code.notAuthenticated`](nsfileprovidererror/code/notauthenticated.md), [`NSFileProviderError.Code.insufficientQuota`](nsfileprovidererror/code/insufficientquota.md), or [`NSFileProviderError.Code.serverUnreachable`](nsfileprovidererror/code/serverunreachable.md) error. As soon as you resolve the underlying error, call this method to tell the system to retry the original action.

## Parameters

- `error`: The original error.
- `completionHandler`: A block that the system calls after resuming the action that triggered the original error. The block takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/signalerrorresolved(_:completionhandler:))*