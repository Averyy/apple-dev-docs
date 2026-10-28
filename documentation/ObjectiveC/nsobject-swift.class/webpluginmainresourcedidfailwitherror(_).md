# webPlugInMainResourceDidFailWithError(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invoked when an error occurs loading the main resource.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func webPlugInMainResourceDidFailWithError(_ error: (any Error)!)
```

```objc
- (void) webPlugInMainResourceDidFailWithError:(NSError *) error;
```

## Discussion

This message is invoked when the underlying `NSURLConnection` object for the main resource sends the connection:didFailWithError: message to its delegate.

## Parameters

- `error`: An error object containing details of why the connection failed to load the request successfully.

## See Also

### Main resource messages
- [func webPlugInMainResourceDidFinishLoading()](./webpluginmainresourcedidfinishloading%28%29.md)
  Invoked when the connection successfully finishes loading data.
- [func webPlugInMainResourceDidReceive(Data!)](./webpluginmainresourcedidreceive%28_%29-5b6f6.md)
  Invoked when the connection loads data incrementally.
- [func webPlugInMainResourceDidReceive(URLResponse!)](./webpluginmainresourcedidreceive%28_%29-6x7b9.md)
  Invoked when the connection receives sufficient data to construct the URL response for its request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfailwitherror(_:))*