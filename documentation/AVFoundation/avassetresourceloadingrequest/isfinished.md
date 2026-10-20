# isFinished

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isFinished) BOOL finished;
```

#### Discussion

The value of this property is [`false`](../../Swift/false.md) initially. The value changes to [`true`](../../Swift/true.md) when the delegate object handling the request calls the [`finishLoading(with:data:redirect:)`](./finishloading%28with,data,redirect%29.md) or [`finishLoading(with:)`](./finishloading%28with%29.md) method.

## See Also

### Reporting the result of the request
- [var response: URLResponse?](./response.md)
  The URL response for the loading request.
- [func finishLoading()](./finishloading%28%29.md)
  Causes the receiver to treat the processing of the request as complete.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the request has been cancelled.
- [func finishLoading(with: (any Error)?)](./finishloading%28with%29.md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](./finishloading%28with,data,redirect%29.md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/isfinished)*