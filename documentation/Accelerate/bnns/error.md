# BNNS.Error

**Framework**: Accelerate  
**Kind**: enum

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
enum Error
```

## Topics

### Enumeration Cases
- [BNNS.Error.arrayDescriptorInvalidData](bnns/error/arraydescriptorinvaliddata.md)
- [BNNS.Error.layerApplyFail](bnns/error/layerapplyfail.md)
- [BNNS.Error.optimizerStepFail](bnns/error/optimizerstepfail.md)
- [BNNS.Error.unableToCreateLayer](bnns/error/unabletocreatelayer.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func BNNSBandPart(Int32, Int32, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsbandpart(_:_:_:_:_:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [func BNNSShuffle(BNNSShuffleType, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsshuffle(_:_:_:_:).md)
  Rearranges elements in a tensor according to shuffle type.
- [struct BNNSShuffleType](bnnsshuffletype.md)
  Constants that specify a shuffle type.
- [func BNNSTile(UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstile(_:_:_:).md)
  Generates an output tensor by tiling an input tensor multiple times.
- [func BNNSTileBackward(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstilebackward(_:_:_:).md)
  Applies a tile filter backward to generate an input gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/error)*