# expandingShape(at:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns a new shaped array with expanded dimensions

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
func expandingShape(at axis: Int) -> MLShapedArraySlice<Scalar>
```

Available when `Scalar` conforms to `MLShapedArrayScalar`.

#### Discussion

The shape of the new `MLShapedArraySlice` gets a new dimension of 1 at the specified axis index.

```swift
let original = MLShapedArraySlice<Int32>(scalars: 0..., shape: [2, 3])
let expanded = original.expanded(alongAxis: 0)
expanded.shape // [1, 2, 3]
```

## See Also

### Shaping the array slice
- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArraySlice<Scalar>](./changinglayout%28to%29.md)
  Returns a copy with the specified buffer layout.
- [func reshaped(to: [Int]) -> MLShapedArraySlice<Scalar>](./reshaped%28to%29.md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArraySlice<Scalar>](./squeezingshape%28%29.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArraySlice<Scalar>](./transposed%28%29.md)
  Returns a new transposed shaped array
- [func transposed(permutation: [Int]) -> MLShapedArraySlice<Scalar>](./transposed%28permutation%29.md)
  Returns a new transposed shaped array using a custom permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/expandingshape(at:))*