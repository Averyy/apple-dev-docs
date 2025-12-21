# BNNS.Norm

**Framework**: Accelerate  
**Kind**: struct

Constants that describe norm types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
@frozen
struct Norm
```

## Topics

### Norm Types
- [static var taxicab: BNNS.Norm](bnns/norm/taxicab.md)
  A constant that represents the taxicab norm.
- [static var l1: BNNS.Norm](bnns/norm/l1.md)
  A constant that represents the L1 norm.
- [static var euclidean: BNNS.Norm](bnns/norm/euclidean.md)
  A constant that represents the Euclidean norm.
- [static var l2: BNNS.Norm](bnns/norm/l2.md)
  A constant that represents the L2 norm.
- [static var maximum: BNNS.Norm](bnns/norm/maximum.md)
  A constant that represents the maximum norm.
- [static var lInfinity: BNNS.Norm](bnns/norm/linfinity.md)
  A constant that represents the maximum norm.
### Raw Values
- [init(rawValue: Float)](bnns/norm/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: Float](bnns/norm/rawvalue.md)
  The corresponding value of the raw type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, dictionary: BNNSNDArrayDescriptor, paddingIndex: Int, maximumNorm: Float, normType: BNNS.Norm, scalesGradientByFrequency: Bool, filterParameters: BNNSFilterParameters?)](bnns/embeddinglayer/init(input:output:dictionary:paddingindex:maximumnorm:normtype:scalesgradientbyfrequency:filterparameters:).md)
  Returns a new embedding layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/norm)*