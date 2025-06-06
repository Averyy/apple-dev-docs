# deviceType

**Framework**: ML Compute  
**Kind**: property

A device type that indicates where the system executes the layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
var deviceType: MLCDeviceType { get }
```

#### Discussion

The system uses the [`MLCDevice`](mlcdevice.md) you provide to [`compile(options:device:)`](mlctraininggraph/compile(options:device:).md) to execute the layers in the graph.

If you select [`MLCDeviceType.ane`](mlcdevicetype/ane.md), it is possible that some layers may not execute on the [`MLCDeviceType.ane`](mlcdevicetype/ane.md), but instead on the CPU or GPU.

## See Also

- [var layerID: Int](mlclayer/layerid.md)
  A unique number that identifies each layer.
- [var label: String](mlclayer/label.md)
  A string that helps identify this layer.
- [var isDebuggingEnabled: Bool](mlclayer/isdebuggingenabled.md)
  A Boolean that indicates whether you choose to debug the layer when executing a graph that includes it.
- [class func supportsDataType(MLCDataType, on: MLCDevice) -> Bool](mlclayer/supportsdatatype(_:on:).md)
  Returns a Boolean that indicates whether instances of this layer accept source tensors for the data type and device that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayer/devicetype)*