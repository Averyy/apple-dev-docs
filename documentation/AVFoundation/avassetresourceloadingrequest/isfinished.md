# isFinished

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether loading of the resource has finished.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isFinished: Bool { get }
```

#### Discussion

The value of this property is [`false`](https://developer.apple.com/documentation/swift/false) initially. The value changes to [`true`](https://developer.apple.com/documentation/swift/true) when the delegate object handling the request calls the [`finishLoading(with:data:redirect:)`](avassetresourceloadingrequest/finishloading(with:data:redirect:).md) or [`finishLoading(with:)`](avassetresourceloadingrequest/finishloading(with:).md) method.

## See Also

- [var response: URLResponse?](avassetresourceloadingrequest/response.md)
  The URL response for the loading request.
- [func finishLoading()](avassetresourceloadingrequest/finishloading.md)
  Causes the receiver to treat the processing of the request as complete.
- [var isCancelled: Bool](avassetresourceloadingrequest/iscancelled.md)
  A Boolean value that indicates whether the request has been cancelled.
- [func finishLoading(with: (any Error)?)](avassetresourceloadingrequest/finishloading(with:).md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](avassetresourceloadingrequest/finishloading(with:data:redirect:).md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/isfinished)*