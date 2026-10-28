# supportedViewingModes(for:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

The viewing modes supported by the provided spatial 3D image.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
static func supportedViewingModes(for spatial3DImage: ImagePresentationComponent.Spatial3DImage) -> Set<ImagePresentationComponent.ViewingMode>
```

**Other overloads**:

```swift
static func supportedViewingModes(for imageSource: CGImageSource) -> Set<ImagePresentationComponent.ViewingMode>
```

## Discussion

> **Note**: This property returns the set of modes that are *currently* available. The returned set of modes will not contain spatial 3D viewing modes if a spatial 3D representation has not yet been generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/supportedviewingmodes(for:)-4emjx)*