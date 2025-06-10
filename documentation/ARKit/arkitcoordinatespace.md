# ARKitCoordinateSpace

**Framework**: ARKit  
**Kind**: struct

An object which represents an ARKit coordinate space.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ARKitCoordinateSpace
```

## Topics

### Instance Properties
- [var ancestorSpace: WorldReferenceCoordinateSpace?](arkitcoordinatespace/ancestorspace.md)
  Returns the parent space of this ARKit coordinate space.
### Instance Methods
- [func ancestorFromSpaceTransformFloat() -> ProjectiveTransform3DFloat](arkitcoordinatespace/ancestorfromspacetransformfloat.md)
  Returns the transformation to ancestor space from this ARKit coordinate space.
### Enumerations
- [ARKitCoordinateSpace.Correction](arkitcoordinatespace/correction.md)
  A correction type to apply on coordinate spaces returned from ARKit APIs.

## Relationships

### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)
- [CoordinateSpace3DFloat](../Spatial/CoordinateSpace3DFloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitcoordinatespace)*