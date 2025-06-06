# label

**Framework**: ML Compute  
**Kind**: property

A string that helps identify this layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var label: String { get set }
```

## See Also

- [var layerID: Int](mlclayer/layerid.md)
  A unique number that identifies each layer.
- [var isDebuggingEnabled: Bool](mlclayer/isdebuggingenabled.md)
  A Boolean that indicates whether you choose to debug the layer when executing a graph that includes it.
- [var deviceType: MLCDeviceType](mlclayer/devicetype.md)
  A device type that indicates where the system executes the layer.
- [class func supportsDataType(MLCDataType, on: MLCDevice) -> Bool](mlclayer/supportsdatatype(_:on:).md)
  Returns a Boolean that indicates whether instances of this layer accept source tensors for the data type and device that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayer/label)*