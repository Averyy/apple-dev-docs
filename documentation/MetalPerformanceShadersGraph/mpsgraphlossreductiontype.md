# MPSGraphLossReductionType

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

The type of the reduction the graph applies in the loss operations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphLossReductionType
```

## Topics

### Enumeration Cases
- [MPSGraphLossReductionType.mean](mpsgraphlossreductiontype/mean.md)
  Reduces the loss down to a scalar with a mean operation.
- [MPSGraphLossReductionType.none](mpsgraphlossreductiontype/none.md)
  Computes the loss without reduction.
- [MPSGraphLossReductionType.sum](mpsgraphlossreductiontype/sum.md)
  Reduces the loss down to a scalar with a sum operation.
### Initializers
- [init?(rawValue: UInt64)](mpsgraphlossreductiontype/init(rawvalue:).md)
### Type Properties
- [static var axis: MPSGraphLossReductionType](mpsgraphlossreductiontype/axis.md)
  Computes the loss without reduction.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphlossreductiontype)*