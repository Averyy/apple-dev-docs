# finishLoading(with:)

**Framework**: AVFoundation  
**Kind**: method

Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finishLoading(with error: (any Error)?)
```

#### Discussion

When a resource loader’s delegate takes responsibility for loading a resource, it calls this method when a failure occurred when loading the resource. This method marks the loading request as finished and notifies the resource loader object that the resource could not be loaded.

## Parameters

- `error`: An error object indicating the reason for the failure.

## See Also

- [var response: URLResponse?](avassetresourceloadingrequest/response.md)
  The URL response for the loading request.
- [func finishLoading()](avassetresourceloadingrequest/finishloading.md)
  Causes the receiver to treat the processing of the request as complete.
- [var isCancelled: Bool](avassetresourceloadingrequest/iscancelled.md)
  A Boolean value that indicates whether the request has been cancelled.
- [var isFinished: Bool](avassetresourceloadingrequest/isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](avassetresourceloadingrequest/finishloading(with:data:redirect:).md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/finishloading(with:))*