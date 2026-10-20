# finishLoading(with:data:redirect:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .

**Availability**:
- macOS 10.15+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 9.0

> **Deprecated**: This method is deprecated. Use the following methods and properties instead: the [`response`](./response.md) property to provide the response object, the [`redirect`](./redirect.md) property when redirecting a request, invoking the [`dataRequest`](./datarequest.md) instance’s[`respond(with:)`](../avassetresourceloadingdatarequest/respond%28with%29.md) method to provide data, and the [`finishLoading()`](./finishloading%28%29.md) method to indicate that loading is finished.

## Declaration

```swift
func finishLoading(with response: URLResponse?, data: Data?, redirect: URLRequest?)
```

```objc
- (void) finishLoadingWithResponse:(NSURLResponse *) response data:(NSData *) data redirect:(NSURLRequest *) redirect;
```

#### Discussion

When a resource loader’s delegate takes responsibility for loading a resource, it calls this method to indicate that the resource was loaded successfully. This method marks the loading request as finished and returns the provided data back to the resource loader object for processing.

## Parameters

- `response`: The response object for the requested resource. Use the request object in the receiver’s [`request`](./request.md) property to get information about the requested resource.
- `data`: The data of the resource. If no data is available, specify `nil`.
- `redirect`: When redirecting a resource request, use this parameter to specify the corresponding [`NSURLRequest`](../../Foundation/nsurlrequest.md) object. If you are handling the request and not redirecting it, specify `nil`.

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
- [var isFinished: Bool](./isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/finishloading(with:data:redirect:))*