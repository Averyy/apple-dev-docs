# finishLoading(with:data:redirect:)

**Framework**: AVFoundation  
**Kind**: method

Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .

**Availability**:
- macOS 10.15+
- tvOS 9.0+

## Declaration

```swift
func finishLoading(with response: URLResponse?, data: Data?, redirect: URLRequest?)
```

#### Discussion

When a resource loader’s delegate takes responsibility for loading a resource, it calls this method to indicate that the resource was loaded successfully. This method marks the loading request as finished and returns the provided data back to the resource loader object for processing.

## Parameters

- `response`: The response object for the requested resource. Use the request object in the receiver’s   property to get information about the requested resource.
- `data`: The data of the resource. If no data is available, specify  .
- `redirect`: When redirecting a resource request, use this parameter to specify the corresponding   object. If you are handling the request and not redirecting it, specify  .

## See Also

- [var response: URLResponse?](avassetresourceloadingrequest/response.md)
  The URL response for the loading request.
- [func finishLoading()](avassetresourceloadingrequest/finishloading.md)
  Causes the receiver to treat the processing of the request as complete.
- [var isCancelled: Bool](avassetresourceloadingrequest/iscancelled.md)
  A Boolean value that indicates whether the request has been cancelled.
- [func finishLoading(with: (any Error)?)](avassetresourceloadingrequest/finishloading(with:).md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [var isFinished: Bool](avassetresourceloadingrequest/isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/finishloading(with:data:redirect:))*