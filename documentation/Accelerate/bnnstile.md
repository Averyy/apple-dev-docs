# BNNSTile(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Generates an output tensor by tiling an input tensor multiple times.

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
func BNNSTile(_ input: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

Use [`BNNSTile(_:_:_:)`](bnnstile(_:_:_:).md) to tile generate a tensor by repeating tiled copies of the input tensor. The dimensions of the output tensor must be an integer multiple of the corresponding dimension of the input tensor.

For example, the following code tiles a 2 x 3 matrix three times along the first dimension and twice along the second dimension:

```swift
let values: [Float] = [1.0, 2.0, 3.0,
                       4.0, 5.0, 6.0]

var inputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: values,
    shape: .matrixRowMajor(2, 3))

var outputDescriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .matrixRowMajor(6, 6))

BNNSTile(&inputDescriptor, &outputDescriptor, nil)

inputDescriptor.deallocate()
outputDescriptor.deallocate()
```

On return, `outputDescriptor` contains the following values:

```swift
[ 1.0, 2.0, 3.0,  1.0, 2.0, 3.0,
  4.0, 5.0, 6.0,  4.0, 5.0, 6.0,

  1.0, 2.0, 3.0,  1.0, 2.0, 3.0,
  4.0, 5.0, 6.0,  4.0, 5.0, 6.0,

  1.0, 2.0, 3.0,  1.0, 2.0, 3.0,
  4.0, 5.0, 6.0,  4.0, 5.0, 6.0 ]
```

## Parameters

- `input`: A pointer to the input descriptor.
- `output`: A pointer to the output descriptor.
- `filter_params`: The filter runtime parameters.

## See Also

- [BNNS.Error](bnns/error.md)
- [func BNNSBandPart(Int32, Int32, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsbandpart(_:_:_:_:_:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [func BNNSShuffle(BNNSShuffleType, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsshuffle(_:_:_:_:).md)
  Rearranges elements in a tensor according to shuffle type.
- [struct BNNSShuffleType](bnnsshuffletype.md)
  Constants that specify a shuffle type.
- [func BNNSTileBackward(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstilebackward(_:_:_:).md)
  Applies a tile filter backward to generate an input gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstile(_:_:_:))*