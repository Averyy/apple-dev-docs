# supportsDataType(_:on:)

**Framework**: ML Compute  
**Kind**: method

Returns a Boolean that indicates whether instances of this layer accept source tensors for the data type and device that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class func supportsDataType(_ dataType: MLCDataType, on device: MLCDevice) -> Bool
```

#### Return Value

`true` if the specified data type and device are supported.

## Parameters

- `dataType`: The data type of a possible input tensor to the layer.
- `device`: The device to use to determine layer support.

## See Also

- [var layerID: Int](mlclayer/layerid.md)
  A unique number that identifies each layer.
- [var label: String](mlclayer/label.md)
  A string that helps identify this layer.
- [var isDebuggingEnabled: Bool](mlclayer/isdebuggingenabled.md)
  A Boolean that indicates whether you choose to debug the layer when executing a graph that includes it.
- [var deviceType: MLCDeviceType](mlclayer/devicetype.md)
  A device type that indicates where the system executes the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayer/supportsdatatype(_:on:))*