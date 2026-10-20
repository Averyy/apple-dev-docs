# BNNSShuffleType

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that specify a shuffle type.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSShuffleType
```

```c
typedef enum { ... } BNNSShuffleType;
```

## Topics

### Constants
- [init(UInt32)](./bnnsshuffletype/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnsshuffletype/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnsshuffletype/rawvalue.md)
- [var BNNSShuffleTypePixelShuffleNCHW: BNNSShuffleType](./bnnsshuffletypepixelshufflenchw.md)
  The pixel shuffle for the NCHW (batch, channels, height, width) format, equivalent to depth-to-space in Column Row Depth (CRD) mode.
- [var BNNSShuffleTypePixelUnshuffleNCHW: BNNSShuffleType](./bnnsshuffletypepixelunshufflenchw.md)
  The pixel unshuffle for the NCHW (batch, channels, height, width) format, equivalent to space-to-depth in Column Row Depth (CRD) mode.
- [var BNNSShuffleTypeDepthToSpaceNCHW: BNNSShuffleType](./bnnsshuffletypedepthtospacenchw.md)
- [var BNNSShuffleTypeSpaceToDepthNCHW: BNNSShuffleType](./bnnsshuffletypespacetodepthnchw.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Errors
- [BNNS.Error](./bnns/error.md)
- [func BNNSBandPart(Int32, Int32, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsbandpart%28_,_,_,_,_%29.md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [func BNNSShuffle(BNNSShuffleType, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsshuffle%28_,_,_,_%29.md)
  Rearranges elements in a tensor according to shuffle type.
- [func BNNSTile(UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnstile%28_,_,_%29.md)
  Generates an output tensor by tiling an input tensor multiple times.
- [func BNNSTileBackward(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnstilebackward%28_,_,_%29.md)
  Applies a tile filter backward to generate an input gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsshuffletype)*