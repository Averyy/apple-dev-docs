# changingLayout(to:)

**Framework**: Core ML  
**Kind**: method

Returns a copy with the specified buffer layout.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func changingLayout(to bufferLayout: MLShapedArrayBufferLayout) -> MLShapedArray<Scalar>
```

#### Discussion

The returned shaped array will have `.strides` property according to the requested layout.

The function may return a heap-memory backed shaped array even if `self` is backed by a pixel buffer.

```swift
let source = MLShapedArray<Int32>(scalars: 0..., shape: [2, 2])

// Returns a new MLShapedArray with the specified strides.
_ = source.changingLayout(to: .custom(strides: [4, 1]))

// Returns a new MLShapedArray with the first-major contiguous layout.
_ = source.changingLayout(to: .firstMajorContiguous)

// Returns a new MLShapedArray with the last-major contiguous layout.
_ = source.changingLayout(to: .lastMajorContiguous)
```

The `withUnsafeShapedBufferPointer` function provides read-only access to the underlying buffer of the layout.

The `withUnsafeMutableShapedBufferPointer(body:)` function may provide a buffer of different layout due to copy-on-write. Use `withUnsafeMutableShapedBufferPointer(bufferLayout:body:)` if you need a specific buffer layout.

It raises a precondition error if the custom strides and the shape have different ranks.

## Parameters

- `bufferLayout`: The desired buffer layout.

## See Also

- [func expandingShape(at: Int) -> MLShapedArray<Scalar>](mlshapedarray/expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions.
- [func reshaped(to: [Int]) -> MLShapedArray<Scalar>](mlshapedarray/reshaped(to:).md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArray<Scalar>](mlshapedarray/squeezingshape.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArray<Scalar>](mlshapedarray/transposed.md)
  Returns a new transposed shaped array.
- [func transposed(permutation: [Int]) -> MLShapedArray<Scalar>](mlshapedarray/transposed(permutation:).md)
  Returns a transposed shaped array using a custom permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/changinglayout(to:))*