# layerID

**Framework**: ML Compute  
**Kind**: property

A unique number that identifies each layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var layerID: Int { get }
```

#### Discussion

The framework assigns `layerID` during layer initialization.

## See Also

- [var label: String](mlclayer/label.md)
  A string that helps identify this layer.
- [var isDebuggingEnabled: Bool](mlclayer/isdebuggingenabled.md)
  A Boolean that indicates whether you choose to debug the layer when executing a graph that includes it.
- [var deviceType: MLCDeviceType](mlclayer/devicetype.md)
  A device type that indicates where the system executes the layer.
- [class func supportsDataType(MLCDataType, on: MLCDevice) -> Bool](mlclayer/supportsdatatype(_:on:).md)
  Returns a Boolean that indicates whether instances of this layer accept source tensors for the data type and device that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayer/layerid)*