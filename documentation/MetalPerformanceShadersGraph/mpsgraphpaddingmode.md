# MPSGraphPaddingMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

The tensor padding mode.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphPaddingMode
```

## Topics

### Enumeration Cases
- [MPSGraphPaddingMode.antiPeriodic](mpsgraphpaddingmode/antiperiodic.md)
  Anti Periodic `x[-2] -> -x[L-3]`
- [MPSGraphPaddingMode.clampToEdge](mpsgraphpaddingmode/clamptoedge.md)
  ClampToEdge (PyTorch ReplicationPad)
- [MPSGraphPaddingMode.constant](mpsgraphpaddingmode/constant.md)
  Constant
- [MPSGraphPaddingMode.periodic](mpsgraphpaddingmode/periodic.md)
  Periodic `x[-2] -> x[L-3], where L is size of x.`
- [MPSGraphPaddingMode.reflect](mpsgraphpaddingmode/reflect.md)
  Reflect
- [MPSGraphPaddingMode.symmetric](mpsgraphpaddingmode/symmetric.md)
  Symmetric
- [MPSGraphPaddingMode.zero](mpsgraphpaddingmode/zero.md)
  Zero
### Initializers
- [init?(rawValue: Int)](mpsgraphpaddingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpaddingmode)*