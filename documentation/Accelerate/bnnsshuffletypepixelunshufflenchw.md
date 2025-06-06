# BNNSShuffleTypePixelUnshuffleNCHW

**Framework**: Accelerate  
**Kind**: var

The pixel unshuffle for the NCHW (batch, channels, height, width) format, equivalent to space-to-depth in Column Row Depth (CRD) mode.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var BNNSShuffleTypePixelUnshuffleNCHW: BNNSShuffleType { get }
```

#### Discussion

Use this shuffle type to reverse the pixel shuffle operation by rearranging elements in a tensor of shape `(N,C,H×r,W×r)` to a tensor of shape `(N,C×rxr,H,W)`, where `r` is a downscale factor

## See Also

- [init(UInt32)](bnnsshuffletype/init(_:).md)
- [init(rawValue: UInt32)](bnnsshuffletype/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsshuffletype/rawvalue.md)
- [var BNNSShuffleTypePixelShuffleNCHW: BNNSShuffleType](bnnsshuffletypepixelshufflenchw.md)
  The pixel shuffle for the NCHW (batch, channels, height, width) format, equivalent to depth-to-space in Column Row Depth (CRD) mode.
- [var BNNSShuffleTypeDepthToSpaceNCHW: BNNSShuffleType](bnnsshuffletypedepthtospacenchw.md)
- [var BNNSShuffleTypeSpaceToDepthNCHW: BNNSShuffleType](bnnsshuffletypespacetodepthnchw.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsshuffletypepixelunshufflenchw)*