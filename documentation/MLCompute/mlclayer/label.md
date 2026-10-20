# label

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A string that helps identify this layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var label: String { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSString * label;
```

## See Also

### Inspecting a Layer
- [var layerID: Int](./layerid.md)
  A unique number that identifies each layer.
- [var isDebuggingEnabled: Bool](./isdebuggingenabled.md)
  A Boolean that indicates whether you choose to debug the layer when executing a graph that includes it.
- [var deviceType: MLCDeviceType](./devicetype.md)
  A device type that indicates where the system executes the layer.
- [class func supportsDataType(MLCDataType, on: MLCDevice) -> Bool](./supportsdatatype%28_,on%29.md)
  Returns a Boolean that indicates whether instances of this layer accept source tensors for the data type and device that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayer/label)*