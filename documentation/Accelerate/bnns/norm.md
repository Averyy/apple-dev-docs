# BNNS.Norm

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe norm types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
@frozen
struct Norm
```

## Topics

### Norm Types
- [static var taxicab: BNNS.Norm](./norm/taxicab.md)
  A constant that represents the taxicab norm.
- [static var l1: BNNS.Norm](./norm/l1.md)
  A constant that represents the L1 norm.
- [static var euclidean: BNNS.Norm](./norm/euclidean.md)
  A constant that represents the Euclidean norm.
- [static var l2: BNNS.Norm](./norm/l2.md)
  A constant that represents the L2 norm.
- [static var maximum: BNNS.Norm](./norm/maximum.md)
  A constant that represents the maximum norm.
- [static var lInfinity: BNNS.Norm](./norm/linfinity.md)
  A constant that represents the maximum norm.
### Raw Values
- [init(rawValue: Float)](./norm/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [var rawValue: Float](./norm/rawvalue.md)
  The corresponding value of the raw type.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an Embedding Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, dictionary: BNNSNDArrayDescriptor, paddingIndex: Int, maximumNorm: Float, normType: BNNS.Norm, scalesGradientByFrequency: Bool, filterParameters: BNNSFilterParameters?)](./embeddinglayer/init%28input,output,dictionary,paddingindex,maximumnorm,normtype,scalesgradientbyfrequency,filterparameters%29.md)
  Returns a new embedding layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/norm)*