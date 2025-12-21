# isCancelled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the request has been cancelled.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isCancelled: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) when the resource loader cancels the loading of a request, just prior to sending the message [`resourceLoader(_:didCancel:)`](avassetresourceloaderdelegate/resourceloader(_:didcancel:)-3nl51.md) to the delegate.

## See Also

- [var response: URLResponse?](avassetresourceloadingrequest/response.md)
  The URL response for the loading request.
- [func finishLoading()](avassetresourceloadingrequest/finishloading.md)
  Causes the receiver to treat the processing of the request as complete.
- [func finishLoading(with: (any Error)?)](avassetresourceloadingrequest/finishloading(with:).md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [var isFinished: Bool](avassetresourceloadingrequest/isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](avassetresourceloadingrequest/finishloading(with:data:redirect:).md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/iscancelled)*