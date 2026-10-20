# availableViewingModes

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The currently valid viewing modes for the image being presented.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var availableViewingModes: Set<ImagePresentationComponent.ViewingMode> { get }
```

#### Discussion

> **Note**: This property returns the set of modes that are *currently* available. The returned set of modes will not contain spatial 3D viewing modes if the component is presenting a `Spatial3DImage` that has not yet generated its spatial 3D representation.

## See Also

### Setting and discovering viewing modes
- [ImagePresentationComponent.ViewingMode](./viewingmode-swift.struct.md)
  Image content’s rendering mode.
- [var viewingMode: ImagePresentationComponent.ViewingMode](./viewingmode-swift.property.md)
  The currently active viewing mode of the presented image.
- [var desiredViewingMode: ImagePresentationComponent.ViewingMode](./desiredviewingmode.md)
  The user-selected preferred content viewing mode.
- [static func supportedViewingModes(for: CGImageSource) -> Set<ImagePresentationComponent.ViewingMode>](./supportedviewingmodes%28for%29-7za1y.md)
  The viewing modes supported by the provided image source.
- [static func supportedViewingModes(for: CGImageSource) -> Set<ImagePresentationComponent.ViewingMode>](./supportedviewingmodes%28for%29-7za1y.md)
  The viewing modes supported by the provided image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/availableviewingmodes)*