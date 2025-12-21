# transposed()

**Framework**: Core ML  
**Kind**: method

Returns a new transposed shaped array.

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
func transposed() -> MLShapedArray<Scalar>
```

#### Discussion

This is equivalent to `transposed(permutation:)` where `permutation:` parameter is `[shape.count-1, shape.count-2, ..., 0]`, which reverses the shape.

```swift
let original = MLShapedArray<Int32>(scalars: 0..., shape: [1, 2, 3])
let transposed = original.transposed()
transposed.shape // [3, 2, 1]
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
- [func transposed(permutation: [Int]) -> MLShapedArray<Scalar>](mlshapedarray/transposed(permutation:).md)
  Returns a transposed shaped array using a custom permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/transposed())*