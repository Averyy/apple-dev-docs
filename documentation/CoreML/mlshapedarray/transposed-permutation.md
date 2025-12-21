# transposed(permutation:)

**Framework**: Core ML  
**Kind**: method

Returns a transposed shaped array using a custom permutation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func transposed(permutation axes: [Int]) -> MLShapedArray<Scalar>
```

#### Discussion

Use this method to convert, for example, the image data layout from `[C, H, W]` to `[C, W, H]`, where `C` is channel, `W` is width, and `H` is height.

```swift
// The source tensor has 3 channels, 128 x 64 image in [C, H, W] layout.
let imageCHW = MLShapedArray<Int32>(scalars: pixelValues,
                                    shape: [3, 64, 128])
let imageCWH = imageCHW.transposed(permutation: [0, 2, 1])
imageCHW.shape // [3, 64, 128]
imageCWH.shape // [3, 128, 64]
```

The shape (`shape_out`) is transposed from the input shape (`shape_in`) as follows.

```swift
shape_out[i]
  == permutation.map { shape_in[$0] }
```

The scalar value of the output shaped array (`array_out`) is related to the input shaped array (`array_in`) as follows.

```swift
array_out(scalarAt: permutation.map { indices[$0] })
  == array_in[scalarAt: indices]]
```

## See Also

- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArray<Scalar>](mlshapedarray/changinglayout(to:).md)
  Returns a copy with the specified buffer layout.
- [func expandingShape(at: Int) -> MLShapedArray<Scalar>](mlshapedarray/expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions.
- [func reshaped(to: [Int]) -> MLShapedArray<Scalar>](mlshapedarray/reshaped(to:).md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArray<Scalar>](mlshapedarray/squeezingshape.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArray<Scalar>](mlshapedarray/transposed.md)
  Returns a new transposed shaped array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/transposed(permutation:))*