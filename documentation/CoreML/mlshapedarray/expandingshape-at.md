# expandingShape(at:)

**Framework**: Core ML  
**Kind**: method

Returns a new shaped array with expanded dimensions.

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
func expandingShape(at axis: Int) -> MLShapedArray<Scalar>
```

#### Discussion

The shape of the new `MLShapedArray` gets a new dimension of 1 at the specified axis index.

```swift
let original = MLShapedArray<Int32>(scalars: 0..., shape: [2, 3])
let expanded = original.expandingShape(at: 0)
expanded.shape // [1, 2, 3]
```

## See Also

- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArray<Scalar>](mlshapedarray/changinglayout(to:).md)
  Returns a copy with the specified buffer layout.
- [func reshaped(to: [Int]) -> MLShapedArray<Scalar>](mlshapedarray/reshaped(to:).md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArray<Scalar>](mlshapedarray/squeezingshape.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArray<Scalar>](mlshapedarray/transposed.md)
  Returns a new transposed shaped array.
- [func transposed(permutation: [Int]) -> MLShapedArray<Scalar>](mlshapedarray/transposed(permutation:).md)
  Returns a transposed shaped array using a custom permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/expandingshape(at:))*