# changingLayout(to:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns a copy with the specified buffer layout.

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
func changingLayout(to bufferLayout: MLShapedArrayBufferLayout) -> MLShapedArraySlice<Scalar>
```

Available when `Scalar` conforms to `MLShapedArrayScalar`.

#### Discussion

The returned shaped array slice will have `.strides` property according to the requested layout.

The function may return a heap-memory backed shaped array even if `self` is backed by a pixel buffer.

```swift
let source = MLShapedArray<Int32>(scalars: 0..., shape: [4, 4])
let slice = source[1...2, 1...2] // slice.shape == [2, 2]

// Returns a new MLShapedArraySlice with the specified strides.
_ = slice.changingLayout(to: .custom(strides: [3, 1]))

// Returns a new MLShapedArraySlice with the first-major contiguous layout.
_ = source.changingLayout(to: .firstMajorContiguous) // strides = [2, 1]

// Returns a new MLShapedArraySlice with the last-major contiguous layout.
_ = source.changingLayout(to: .lastMajorContiguous) // strides = [1, 2]
```

The `withUnsafeShapedBufferPointer` function provides read-only access to the underlying buffer of the layout.

The `withUnsafeMutableShapedBufferPointer(body:)` function may provide a buffer of different layout due to copy-on-write. Use `withUnsafeMutableShapedBufferPointer(bufferLayout:body:)` if you need a specific buffer layout.

It raises a precondition error if the custom strides and the shape have different ranks.

## Parameters

- `bufferLayout`: The desired buffer layout.

## See Also

### Shaping the array slice
- [func expandingShape(at: Int) -> MLShapedArraySlice<Scalar>](./expandingshape%28at%29.md)
  Returns a new shaped array with expanded dimensions
- [func reshaped(to: [Int]) -> MLShapedArraySlice<Scalar>](./reshaped%28to%29.md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArraySlice<Scalar>](./squeezingshape%28%29.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArraySlice<Scalar>](./transposed%28%29.md)
  Returns a new transposed shaped array
- [func transposed(permutation: [Int]) -> MLShapedArraySlice<Scalar>](./transposed%28permutation%29.md)
  Returns a new transposed shaped array using a custom permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/changinglayout(to:))*