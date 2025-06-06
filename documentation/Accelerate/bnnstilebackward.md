# BNNSTileBackward(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a tile filter backward to generate an input gradient.

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
func BNNSTileBackward(_ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ out_delta: UnsafePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

## Parameters

- `in_delta`: A pointer to the input delta descriptor.
- `out_delta`: A pointer to the output delta descriptor.
- `filter_params`: The filter runtime parameters.

## See Also

- [BNNS.Error](bnns/error.md)
- [func BNNSBandPart(Int32, Int32, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsbandpart(_:_:_:_:_:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [func BNNSShuffle(BNNSShuffleType, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsshuffle(_:_:_:_:).md)
  Rearranges elements in a tensor according to shuffle type.
- [struct BNNSShuffleType](bnnsshuffletype.md)
  Constants that specify a shuffle type.
- [func BNNSTile(UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstile(_:_:_:).md)
  Generates an output tensor by tiling an input tensor multiple times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstilebackward(_:_:_:))*