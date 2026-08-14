# completeRequest(completionHandler:)

**Framework**: CallKit  
**Kind**: method

Completes the request to the extension context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
func completeRequest() async -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func completeRequest() async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/swift/calling-objective-c-apis-asynchronously).

Call this method on the instance of [`CXCallDirectoryExtensionContext`](cxcalldirectoryextensioncontext.md) passed as an argument to the block parameter of the  [`CXCallDirectoryProvider`](cxcalldirectoryprovider.md) instance method [`beginRequest(with:)`](cxcalldirectoryprovider/beginrequest(with:).md). This method should be called once at the end of the block.

## Parameters

- `completion`: A block to be executed after the request to the extension context is completed. - **expired**: Whether the receiver expired during the request. If [`true`](https://developer.apple.com/documentation/swift/true), then any identification or blocking entries added by the extension context were not added to the extension.

## See Also

- [var isIncremental: Bool](cxcalldirectoryextensioncontext/isincremental.md)
  A Boolean value that indicates whether the request provides data incrementally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/completerequest(completionhandler:))*