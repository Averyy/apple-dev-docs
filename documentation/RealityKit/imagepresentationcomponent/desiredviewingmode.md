# desiredViewingMode

**Framework**: RealityKit  
**Kind**: property

The user-selected preferred content viewing mode.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var desiredViewingMode: ImagePresentationComponent.ViewingMode
```

#### Discussion

The `viewingMode` property will update to this value if it is valid for this component’s content, otherwise a suitable fallback will be used.

## See Also

- [ImagePresentationComponent.ViewingMode](imagepresentationcomponent/viewingmode-swift.struct.md)
  Image content’s rendering mode.
- [var viewingMode: ImagePresentationComponent.ViewingMode](imagepresentationcomponent/viewingmode-swift.property.md)
  The currently active viewing mode of the presented image.
- [var availableViewingModes: Set<ImagePresentationComponent.ViewingMode>](imagepresentationcomponent/availableviewingmodes.md)
  The currently valid viewing modes for the image being presented.
- [static func supportedViewingModes(for: CGImageSource) -> Set<ImagePresentationComponent.ViewingMode>](imagepresentationcomponent/supportedviewingmodes(for:)-7za1y.md)
  The viewing modes supported by the provided image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/desiredviewingmode)*