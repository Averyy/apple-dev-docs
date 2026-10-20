# BNNS.Error

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
enum Error
```

## Topics

### Enumeration Cases
- [BNNS.Error.arrayDescriptorInvalidData](./error/arraydescriptorinvaliddata.md)
- [BNNS.Error.layerApplyFail](./error/layerapplyfail.md)
- [BNNS.Error.optimizerStepFail](./error/optimizerstepfail.md)
- [BNNS.Error.unableToCreateLayer](./error/unabletocreatelayer.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [func BNNSBandPart(Int32, Int32, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnsbandpart%28_,_,_,_,_%29.md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [func BNNSShuffle(BNNSShuffleType, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnsshuffle%28_,_,_,_%29.md)
  Rearranges elements in a tensor according to shuffle type.
- [struct BNNSShuffleType](../bnnsshuffletype.md)
  Constants that specify a shuffle type.
- [func BNNSTile(UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnstile%28_,_,_%29.md)
  Generates an output tensor by tiling an input tensor multiple times.
- [func BNNSTileBackward(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnstilebackward%28_,_,_%29.md)
  Applies a tile filter backward to generate an input gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/error)*