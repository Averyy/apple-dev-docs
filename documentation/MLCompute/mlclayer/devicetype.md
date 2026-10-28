# deviceType

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A device type that indicates where the system executes the layer.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
var deviceType: MLCDeviceType { get }
```

```objc
@property (nonatomic, readonly) MLCDeviceType deviceType;
```

## Discussion

The system uses the [`MLCDevice`](../mlcdevice.md) you provide to [`compile(options:device:)`](../mlctraininggraph/compile%28options,device%29.md) to execute the layers in the graph.

If you select [`MLCDeviceType.ane`](../mlcdevicetype/ane.md), it is possible that some layers may not execute on the [`MLCDeviceType.ane`](../mlcdevicetype/ane.md), but instead on the CPU or GPU.

## See Also

### Inspecting a Layer
- [var layerID: Int](./layerid.md)
  A unique number that identifies each layer.
- [var label: String](./label.md)
  A string that helps identify this layer.
- [var isDebuggingEnabled: Bool](./isdebuggingenabled.md)
  A Boolean that indicates whether you choose to debug the layer when executing a graph that includes it.
- [class func supportsDataType(MLCDataType, on: MLCDevice) -> Bool](./supportsdatatype%28_,on%29.md)
  Returns a Boolean that indicates whether instances of this layer accept source tensors for the data type and device that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayer/devicetype)*