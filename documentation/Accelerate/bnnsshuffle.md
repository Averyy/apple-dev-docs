# BNNSShuffle(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Rearranges elements in a tensor according to shuffle type.

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
func BNNSShuffle(_ type: BNNSShuffleType, _ input: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

Use [`BNNSShuffle(_:_:_:_:)`](bnnsshuffle(_:_:_:_:).md) to rearrange the elements in a tensor between the depth dimension and blocks of 2D spatial data.

Pass a shuffle type of [`BNNSShuffleTypePixelShuffleNCHW`](bnnsshuffletypepixelshufflenchw.md) to specify that the function rearranges elements in a tensor of shape `(N,C×r×r,H,W)` to a tensor of shape `(N,C,H×r,W×r)`, where `r` is an upscale factor.

Pass [`BNNSShuffleTypePixelUnshuffleNCHW`](bnnsshuffletypepixelunshufflenchw.md) to specify that the function elements in a tensor of shape `(N,C,H×r,W×r)` to a tensor of shape `(N,C×r×r,H,W)`, where `r` is a downscale factor.

## Parameters

- `type`: A constant that specifies the shuffle type.
- `input`: A pointer to the input descriptor.
- `output`: A pointer to the output descriptor.
- `filter_params`: The filter runtime parameters.

## See Also

- [BNNS.Error](bnns/error.md)
- [func BNNSBandPart(Int32, Int32, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsbandpart(_:_:_:_:_:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [struct BNNSShuffleType](bnnsshuffletype.md)
  Constants that specify a shuffle type.
- [func BNNSTile(UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstile(_:_:_:).md)
  Generates an output tensor by tiling an input tensor multiple times.
- [func BNNSTileBackward(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstilebackward(_:_:_:).md)
  Applies a tile filter backward to generate an input gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsshuffle(_:_:_:_:))*