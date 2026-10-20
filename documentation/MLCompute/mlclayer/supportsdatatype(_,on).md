# supportsDataType(_:on:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Returns a Boolean that indicates whether instances of this layer accept source tensors for the data type and device that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class func supportsDataType(_ dataType: MLCDataType, on device: MLCDevice) -> Bool
```

```objc
+ (BOOL) supportsDataType:(MLCDataType) dataType onDevice:(MLCDevice *) device;
```

#### Return Value

`true` if the specified data type and device are supported.

## Parameters

- `dataType`: The data type of a possible input tensor to the layer.
- `device`: The device to use to determine layer support.

## See Also

### Inspecting a Layer
- [var layerID: Int](./layerid.md)
  A unique number that identifies each layer.
- [var label: String](./label.md)
  A string that helps identify this layer.
- [var isDebuggingEnabled: Bool](./isdebuggingenabled.md)
  A Boolean that indicates whether you choose to debug the layer when executing a graph that includes it.
- [var deviceType: MLCDeviceType](./devicetype.md)
  A device type that indicates where the system executes the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayer/supportsdatatype(_:on:))*