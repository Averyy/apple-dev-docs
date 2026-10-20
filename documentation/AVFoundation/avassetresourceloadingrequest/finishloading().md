# finishLoading()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to treat the processing of the request as complete.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finishLoading()
```

```objc
- (void) finishLoading;
```

#### Discussion

If a [`dataRequest`](./datarequest.md) is present and the resource does not contain the full extent of the data that has been requested according to the values of the [`requestedOffset`](../avassetresourceloadingdatarequest/requestedoffset.md) and [`requestedLength`](../avassetresourceloadingdatarequest/requestedlength.md) properties of the request, invoke `finishLoading` after providing as much of the requested data as the resource contains.

## See Also

### Reporting the result of the request
- [var response: URLResponse?](./response.md)
  The URL response for the loading request.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the request has been cancelled.
- [func finishLoading(with: (any Error)?)](./finishloading%28with%29.md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](./finishloading%28with,data,redirect%29.md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/finishloading())*