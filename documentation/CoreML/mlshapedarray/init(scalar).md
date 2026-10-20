# init(scalar:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a shaped array with exactly one value and zero dimensions.

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

### Creating a shaped array
- [init<S>(scalars: S, shape: [Int])](./init%28scalars,shape%29.md)
  Initialize with a sequence and the shape.
- [init(mutating: CVPixelBuffer, shape: [Int])](./init%28mutating,shape%29.md)
  Creates a new `MLShapedArray` using a pixel buffer as the backing storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/init(scalar:))*