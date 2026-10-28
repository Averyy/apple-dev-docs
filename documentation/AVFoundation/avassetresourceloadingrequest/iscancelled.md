# isCancelled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isCancelled) BOOL cancelled;
```

## Discussion

[`true`](../../Swift/true.md) when the resource loader cancels the loading of a request, just prior to sending the message [`resourceLoader(_:didCancel:)`](../avassetresourceloaderdelegate/resourceloader%28_,didcancel%29-3nl51.md) to the delegate.

## See Also

### Reporting the result of the request
- [var response: URLResponse?](./response.md)
  The URL response for the loading request.
- [func finishLoading()](./finishloading%28%29.md)
  Causes the receiver to treat the processing of the request as complete.
- [func finishLoading(with: (any Error)?)](./finishloading%28with%29.md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](./finishloading%28with,data,redirect%29.md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/iscancelled)*