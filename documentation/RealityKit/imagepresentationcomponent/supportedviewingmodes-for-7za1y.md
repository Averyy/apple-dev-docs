# supportedViewingModes(for:)

**Framework**: RealityKit  
**Kind**: method

The viewing modes supported by the provided image source.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func supportedViewingModes(for imageSource: CGImageSource) -> Set<ImagePresentationComponent.ViewingMode>
```

#### Discussion

> **Note**: This method returns the viewing modes that will be supported if you initialize an `ImagePresentationComponent` with this image source directly via `init(imageSource: CGImageSource)`.

The returned set of viewing modes will never include the `.spatial3D` or `.spatial3DImmersive` viewing modes, which are only supported when initializing an `ImagePresentationComponent` with a `Spatial3DImage`.

## See Also

- [ImagePresentationComponent.ViewingMode](imagepresentationcomponent/viewingmode-swift.struct.md)
  Image content’s rendering mode.
- [var viewingMode: ImagePresentationComponent.ViewingMode](imagepresentationcomponent/viewingmode-swift.property.md)
  The currently active viewing mode of the presented image.
- [var desiredViewingMode: ImagePresentationComponent.ViewingMode](imagepresentationcomponent/desiredviewingmode.md)
  The user-selected preferred content viewing mode.
- [var availableViewingModes: Set<ImagePresentationComponent.ViewingMode>](imagepresentationcomponent/availableviewingmodes.md)
  The currently valid viewing modes for the image being presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/supportedviewingmodes(for:)-7za1y)*