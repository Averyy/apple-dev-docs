# BNNSTileBackward(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a tile filter backward to generate an input gradient.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
func BNNSTileBackward(_ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ out_delta: UnsafePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

```c
int BNNSTileBackward(BNNSNDArrayDescriptor *in_delta, const BNNSNDArrayDescriptor *out_delta, const BNNSFilterParameters *filter_params);
```

## Parameters

- `in_delta`: A pointer to the input delta descriptor.
- `out_delta`: A pointer to the output delta descriptor.
- `filter_params`: The filter runtime parameters.

## See Also

### Errors
- [BNNS.Error](./bnns/error.md)
- [func BNNSBandPart(Int32, Int32, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsbandpart%28_,_,_,_,_%29.md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [func BNNSShuffle(BNNSShuffleType, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsshuffle%28_,_,_,_%29.md)
  Rearranges elements in a tensor according to shuffle type.
- [struct BNNSShuffleType](./bnnsshuffletype.md)
  Constants that specify a shuffle type.
- [func BNNSTile(UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnstile%28_,_,_%29.md)
  Generates an output tensor by tiling an input tensor multiple times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstilebackward(_:_:_:))*