# webPlugInMainResourceDidFinishLoading()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invoked when the connection successfully finishes loading data.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func webPlugInMainResourceDidFinishLoading()
```

```objc
- (void) webPlugInMainResourceDidFinishLoading;
```

## Discussion

This message is invoked when the `WebPlugInShouldLoadMainResourceKey` plug-in command-line argument is set to [`NO`](../no.md) and the underlying `NSURLConnection` object for the main resource sends the connectionDidFinishLoading: message to its delegate.

## See Also

### Main resource messages
- [func webPlugInMainResourceDidFailWithError((any Error)!)](./webpluginmainresourcedidfailwitherror%28_%29.md)
  Invoked when an error occurs loading the main resource.
- [func webPlugInMainResourceDidReceive(Data!)](./webpluginmainresourcedidreceive%28_%29-5b6f6.md)
  Invoked when the connection loads data incrementally.
- [func webPlugInMainResourceDidReceive(URLResponse!)](./webpluginmainresourcedidreceive%28_%29-6x7b9.md)
  Invoked when the connection receives sufficient data to construct the URL response for its request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfinishloading())*