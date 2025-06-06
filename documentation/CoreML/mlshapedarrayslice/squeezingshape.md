# squeezingShape()

**Framework**: Core ML  
**Kind**: method

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
func squeezingShape() -> MLShapedArraySlice<Scalar>
```

#### Discussion

The new shape removes 1s in the original shape.

```swift
let original = MLShapedArraySlice<Int32>(scalars: 0..., shape: [1, 2, 1, 2])
let squeezed = original.squeezed()
squeezed.shape // [2, 2]
```

When all the dimensions of the original shape is one, the resultant shaped array is a scalar.

```swift
let original = MLShapedArray<Int32>(scalars: 42, shape: [1, 1])
let squeezed = original.squeezed()
squeezed.scalar // 42
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/squeezingshape())*