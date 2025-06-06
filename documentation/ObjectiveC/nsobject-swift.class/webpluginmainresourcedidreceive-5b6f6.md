# webPlugInMainResourceDidReceive(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invoked when the connection loads data incrementally.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func webPlugInMainResourceDidReceive(_ data: Data!)
```

#### Discussion

This message is invoked when the `WebPlugInShouldLoadMainResourceKey` plug-in command-line argument is set to [`NO`](no.md) and the underlying `NSURLConnection` object for the main resource sends the connection:didReceiveData: message to its delegate.

## Parameters

- `data`: The newly available data.

## See Also

- [func webPlugInMainResourceDidFailWithError((any Error)!)](nsobject-swift.class/webpluginmainresourcedidfailwitherror(_:).md)
  Invoked when an error occurs loading the main resource.
- [func webPlugInMainResourceDidFinishLoading()](nsobject-swift.class/webpluginmainresourcedidfinishloading.md)
  Invoked when the connection successfully finishes loading data.
- [func webPlugInMainResourceDidReceive(URLResponse!)](nsobject-swift.class/webpluginmainresourcedidreceive(_:)-6x7b9.md)
  Invoked when the connection receives sufficient data to construct the URL response for its request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive(_:)-5b6f6)*