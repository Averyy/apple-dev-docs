# expandingShape(at:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

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

Available when `Scalar` conforms to `MLShapedArrayScalar`.

#### Discussion

The shape of the new `MLShapedArray` gets a new dimension of 1 at the specified axis index.

```swift
let original = MLShapedArray<Int32>(scalars: 0..., shape: [2, 3])
let expanded = original.expandingShape(at: 0)
expanded.shape // [1, 2, 3]
```

## See Also

### Shaping the array
- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArray<Scalar>](./changinglayout%28to%29.md)
  Returns a copy with the specified buffer layout.
- [func reshaped(to: [Int]) -> MLShapedArray<Scalar>](./reshaped%28to%29.md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArray<Scalar>](./squeezingshape%28%29.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArray<Scalar>](./transposed%28%29.md)
  Returns a new transposed shaped array.
- [func transposed(permutation: [Int]) -> MLShapedArray<Scalar>](./transposed%28permutation%29.md)
  Returns a transposed shaped array using a custom permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/expandingshape(at:))*