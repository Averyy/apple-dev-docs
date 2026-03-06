# ARKitCoordinateSpace

**Framework**: ARKit  
**Kind**: struct

An object which represents an ARKit coordinate space.

**Availability**:
- visionOS 26.0+

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

## See Also

- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [class ARKitSession](arkitsession.md)
  The main entry point for receiving data from ARKit.
- [protocol DataProvider](dataprovider.md)
  A source of live data from ARKit.
- [enum DataProviderState](dataproviderstate.md)
  The possible states of a data provider.
- [protocol Anchor](anchor.md)
  The identity, location, and orientation of an object in world space.
- [protocol TrackableAnchor](trackableanchor.md)
  An anchor that can gain and lose its tracking state over the course of a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitcoordinatespace)*