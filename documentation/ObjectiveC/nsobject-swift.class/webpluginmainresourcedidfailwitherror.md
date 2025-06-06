# webPlugInMainResourceDidFailWithError(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invoked when an error occurs loading the main resource.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func webPlugInMainResourceDidFailWithError(_ error: (any Error)!)
```

#### Discussion

This message is invoked when the underlying `NSURLConnection` object for the main resource sends the connection:didFailWithError: message to its delegate.

## Parameters

- `error`: An error object containing details of why the connection failed to load the request successfully.

## See Also

- [func webPlugInMainResourceDidFinishLoading()](nsobject-swift.class/webpluginmainresourcedidfinishloading.md)
  Invoked when the connection successfully finishes loading data.
- [func webPlugInMainResourceDidReceive(Data!)](nsobject-swift.class/webpluginmainresourcedidreceive(_:)-5b6f6.md)
  Invoked when the connection loads data incrementally.
- [func webPlugInMainResourceDidReceive(URLResponse!)](nsobject-swift.class/webpluginmainresourcedidreceive(_:)-6x7b9.md)
  Invoked when the connection receives sufficient data to construct the URL response for its request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfailwitherror(_:))*