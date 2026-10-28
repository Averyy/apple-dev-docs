# reshaped(to:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns a new reshaped shaped array.

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
func reshaped(to newShape: [Int]) -> MLShapedArraySlice<Scalar>
```

Available when `Scalar` conforms to `MLShapedArrayScalar`.

## Discussion

The reshaped array gets scalars of the original array in first-major order. Therefore, the initializer is semantically equivalent to:

```swift
let reshaped = MLShapedArray(scalars: original.scalars, shape: newShape)
```

Usage example:

```swift
let original = MLShapedArraySlice<Int32>(scalars: 0..., shape: [4])
let reshaped = original.reshaped(to: [1, 2, 2])
```

A scalar can be reshaped to and from a shape where the product of dimensions is one.

The method raises a runtime error if the product of dimensions in the new shape is different from the current one.

## Parameters

- `newShape`: The new shape after reshaping.

## See Also

### Shaping the array slice
- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArraySlice<Scalar>](./changinglayout%28to%29.md)
  Returns a copy with the specified buffer layout.
- [func expandingShape(at: Int) -> MLShapedArraySlice<Scalar>](./expandingshape%28at%29.md)
  Returns a new shaped array with expanded dimensions
- [func squeezingShape() -> MLShapedArraySlice<Scalar>](./squeezingshape%28%29.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArraySlice<Scalar>](./transposed%28%29.md)
  Returns a new transposed shaped array
- [func transposed(permutation: [Int]) -> MLShapedArraySlice<Scalar>](./transposed%28permutation%29.md)
  Returns a new transposed shaped array using a custom permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/reshaped(to:))*