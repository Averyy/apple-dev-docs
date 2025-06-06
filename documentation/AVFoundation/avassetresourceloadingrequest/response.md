# response

**Framework**: AVFoundation  
**Kind**: property

The URL response for the loading request.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var response: URLResponse? { get set }
```

#### Discussion

The value of this property is an instance of [`URLResponse`](https://developer.apple.com/documentation/Foundation/URLResponse), indicating a response to the loading request. If no response is needed, the value of this property is `nil`.

## See Also

- [func finishLoading()](avassetresourceloadingrequest/finishloading.md)
  Causes the receiver to treat the processing of the request as complete.
- [var isCancelled: Bool](avassetresourceloadingrequest/iscancelled.md)
  A Boolean value that indicates whether the request has been cancelled.
- [func finishLoading(with: (any Error)?)](avassetresourceloadingrequest/finishloading(with:).md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [var isFinished: Bool](avassetresourceloadingrequest/isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](avassetresourceloadingrequest/finishloading(with:data:redirect:).md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/response)*