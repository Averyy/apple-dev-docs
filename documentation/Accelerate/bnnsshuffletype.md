# BNNSShuffleType

**Framework**: Accelerate  
**Kind**: struct

Constants that specify a shuffle type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSShuffleType
```

## Topics

### Constants
- [init(UInt32)](bnnsshuffletype/init(_:).md)
- [init(rawValue: UInt32)](bnnsshuffletype/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsshuffletype/rawvalue.md)
- [var BNNSShuffleTypePixelShuffleNCHW: BNNSShuffleType](bnnsshuffletypepixelshufflenchw.md)
  The pixel shuffle for the NCHW (batch, channels, height, width) format, equivalent to depth-to-space in Column Row Depth (CRD) mode.
- [var BNNSShuffleTypePixelUnshuffleNCHW: BNNSShuffleType](bnnsshuffletypepixelunshufflenchw.md)
  The pixel unshuffle for the NCHW (batch, channels, height, width) format, equivalent to space-to-depth in Column Row Depth (CRD) mode.
- [var BNNSShuffleTypeDepthToSpaceNCHW: BNNSShuffleType](bnnsshuffletypedepthtospacenchw.md)
- [var BNNSShuffleTypeSpaceToDepthNCHW: BNNSShuffleType](bnnsshuffletypespacetodepthnchw.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [BNNS.Error](bnns/error.md)
- [func BNNSBandPart(Int32, Int32, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsbandpart(_:_:_:_:_:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [func BNNSShuffle(BNNSShuffleType, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsshuffle(_:_:_:_:).md)
  Rearranges elements in a tensor according to shuffle type.
- [func BNNSTile(UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstile(_:_:_:).md)
  Generates an output tensor by tiling an input tensor multiple times.
- [func BNNSTileBackward(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstilebackward(_:_:_:).md)
  Applies a tile filter backward to generate an input gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsshuffletype)*