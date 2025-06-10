# availableViewingModes

**Framework**: RealityKit  
**Kind**: property

The currently valid viewing modes for the image being presented.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var availableViewingModes: Set<ImagePresentationComponent.ViewingMode> { get }
```

#### Discussion

> **Note**: This property returns the set of modes that are  available. The returned set of modes will not contain spatial 3D viewing modes if the component is presenting a `Spatial3DImage` that has not yet generated its spatial 3D representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/availableviewingmodes)*