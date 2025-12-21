# aspectRatio(for:)

**Framework**: RealityKit  
**Kind**: method

The aspect ratio of the image this component will present for the requested viewing mode.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func aspectRatio(for viewingMode: ImagePresentationComponent.ViewingMode) -> Float?
```

#### Return Value

Returns `nil` if the requested viewing mode is not in the component’s `availableViewingModes` set.

## See Also

- [var screenImageDimension: SIMD2<Float>](imagepresentationcomponent/screenimagedimension.md)
  The image resolution of the currently presented image, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/aspectratio(for:))*