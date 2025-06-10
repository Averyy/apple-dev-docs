# MPSGraphPoolingReturnIndicesMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

The flattening mode for returned indices with max-pooling.

**Availability**:
- iOS 15.3+
- iPadOS 15.3+
- Mac Catalyst 15.3+
- macOS 12.2+
- tvOS 15.3+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphPoolingReturnIndicesMode
```

## Topics

### Enumeration Cases
- [MPSGraphPoolingReturnIndicesMode.globalFlatten1D](mpsgraphpoolingreturnindicesmode/globalflatten1d.md)
  Returns indices flattened in inner most (last) dimension.
- [MPSGraphPoolingReturnIndicesMode.globalFlatten2D](mpsgraphpoolingreturnindicesmode/globalflatten2d.md)
  Returns indices flattened in 2 innermost dimensions. eg: HW in NCHW.
- [MPSGraphPoolingReturnIndicesMode.globalFlatten3D](mpsgraphpoolingreturnindicesmode/globalflatten3d.md)
  Returns indices flattened in 3 innernost dimensions. eg: HWC in NHWC.
- [MPSGraphPoolingReturnIndicesMode.globalFlatten4D](mpsgraphpoolingreturnindicesmode/globalflatten4d.md)
  Returns indices flattened in 4 innermost dimensions.
- [MPSGraphPoolingReturnIndicesMode.localFlatten1D](mpsgraphpoolingreturnindicesmode/localflatten1d.md)
  Returns indices within pooling window, flattened in inner most dimension.
- [MPSGraphPoolingReturnIndicesMode.localFlatten2D](mpsgraphpoolingreturnindicesmode/localflatten2d.md)
  Returns indices within pooling window, flattened in 2 innermost dimensions. eg: HW in NCHW.
- [MPSGraphPoolingReturnIndicesMode.localFlatten3D](mpsgraphpoolingreturnindicesmode/localflatten3d.md)
  Returns indices within pooling window, flattened in 3 innernost dimensions. eg: HWC in NHWC.
- [MPSGraphPoolingReturnIndicesMode.localFlatten4D](mpsgraphpoolingreturnindicesmode/localflatten4d.md)
  Returns indices within pooling window, flattened in 4 innermost dimensions.
- [MPSGraphPoolingReturnIndicesMode.none](mpsgraphpoolingreturnindicesmode/none.md)
  No indices returned.
### Initializers
- [init?(rawValue: UInt)](mpsgraphpoolingreturnindicesmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpoolingreturnindicesmode)*