# completeRequest(completionHandler:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Completes the request to the extension context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
func completeRequest(completionHandler completion: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func completeRequest() async -> Bool
```

```objc
- (void) completeRequestWithCompletionHandler:(void (^)(BOOL expired)) completion;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func completeRequest() async -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Call this method on the instance of [`CXCallDirectoryExtensionContext`](../cxcalldirectoryextensioncontext.md) passed as an argument to the block parameter of the  [`CXCallDirectoryProvider`](../cxcalldirectoryprovider.md) instance method [`beginRequest(with:)`](../cxcalldirectoryprovider/beginrequest%28with%29.md). This method should be called once at the end of the block.

## Parameters

- `completion`: A block to be executed after the request to the extension context is completed.

  - **expired**: Whether the receiver expired during the request.

  If [`true`](../../Swift/true.md), then any identification or blocking entries added by the extension context were not added to the extension.

## See Also

### Completing Requests
- [var isIncremental: Bool](./isincremental.md)
  A Boolean value that indicates whether the request provides data incrementally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/completerequest(completionhandler:))*