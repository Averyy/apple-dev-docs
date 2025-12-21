# init(scalar:)

**Framework**: Core ML  
**Kind**: init

Creates a shaped array slice with exactly one value and zero dimensions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(scalar: Scalar)
```

## Parameters

- `scalar`: A singular scalar value.

## See Also

- [init<S>(scalars: S, shape: [Int])](mlshapedarrayslice/init(scalars:shape:).md)
  Initialize with a sequence and the shape.
- [init(mutating: CVPixelBuffer, shape: [Int])](mlshapedarrayslice/init(mutating:shape:).md)
  Creates a new `MLShapedArraySlice` using a pixel buffer as the backing storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/init(scalar:))*