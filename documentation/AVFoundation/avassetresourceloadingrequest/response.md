# response

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSURLResponse * response;
```

## Discussion

The value of this property is an instance of [`URLResponse`](../../Foundation/urlresponse.md), indicating a response to the loading request. If no response is needed, the value of this property is `nil`.

## See Also

### Reporting the result of the request
- [func finishLoading()](./finishloading%28%29.md)
  Causes the receiver to treat the processing of the request as complete.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the request has been cancelled.
- [func finishLoading(with: (any Error)?)](./finishloading%28with%29.md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](./finishloading%28with,data,redirect%29.md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/response)*