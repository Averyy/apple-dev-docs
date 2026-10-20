# MPSGraphPaddingMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MPSGraphPaddingMode : NSInteger;
```

## Topics

### Enumeration Cases
- [MPSGraphPaddingMode.antiPeriodic](./mpsgraphpaddingmode/antiperiodic.md)
  Anti Periodic `x[-2] -> -x[L-3]`
- [MPSGraphPaddingMode.clampToEdge](./mpsgraphpaddingmode/clamptoedge.md)
  ClampToEdge (PyTorch ReplicationPad)
- [MPSGraphPaddingMode.constant](./mpsgraphpaddingmode/constant.md)
  Constant
- [MPSGraphPaddingMode.periodic](./mpsgraphpaddingmode/periodic.md)
  Periodic `x[-2] -> x[L-3], where L is size of x.`
- [MPSGraphPaddingMode.reflect](./mpsgraphpaddingmode/reflect.md)
  Reflect
- [MPSGraphPaddingMode.symmetric](./mpsgraphpaddingmode/symmetric.md)
  Symmetric
- [MPSGraphPaddingMode.zero](./mpsgraphpaddingmode/zero.md)
  Zero
### Initializers
- [init?(rawValue: Int)](./mpsgraphpaddingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpaddingmode)*