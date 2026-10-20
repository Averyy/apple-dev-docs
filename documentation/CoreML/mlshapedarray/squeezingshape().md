# squeezingShape()

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns a new squeezed shaped array.

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
func squeezingShape() -> MLShapedArray<Scalar>
```

Available when `Scalar` conforms to `MLShapedArrayScalar`.

#### Discussion

The new shape removes 1s in the original shape.

```swift
let original = MLShapedArray<Int32>(scalars: 0..., shape: [1, 2, 1, 2])
let squeezed = original.squeezingShape()
squeezed.shape // [2, 2]
```

When all the dimensions of the original shape is one, the resultant shaped array is a scalar.

```swift
let original = MLShapedArray<Int32>(scalars: 42, shape: [1, 1])
let squeezed = original.squeezingShape()
squeezed.scalar // 42
```

## See Also

### Shaping the array
- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArray<Scalar>](./changinglayout%28to%29.md)
  Returns a copy with the specified buffer layout.
- [func expandingShape(at: Int) -> MLShapedArray<Scalar>](./expandingshape%28at%29.md)
  Returns a new shaped array with expanded dimensions.
- [func reshaped(to: [Int]) -> MLShapedArray<Scalar>](./reshaped%28to%29.md)
  Returns a new reshaped shaped array.
- [func transposed() -> MLShapedArray<Scalar>](./transposed%28%29.md)
  Returns a new transposed shaped array.
- [func transposed(permutation: [Int]) -> MLShapedArray<Scalar>](./transposed%28permutation%29.md)
  Returns a transposed shaped array using a custom permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/squeezingshape())*