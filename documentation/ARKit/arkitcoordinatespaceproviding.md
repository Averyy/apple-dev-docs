# ARKitCoordinateSpaceProviding

**Framework**: ARKit  
**Kind**: protocol

A type that provides an ARKit coordinate space with an optional correction applied.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol ARKitCoordinateSpaceProviding
```

## Topics

### Instance Methods
- [func coordinateSpace(correction: ARKitCoordinateSpace.Correction) -> ARKitCoordinateSpace](arkitcoordinatespaceproviding/coordinatespace(correction:).md)
  The coordinate space of this object.

## Relationships

### Conforming Types
- [AccessoryAnchor](accessoryanchor.md)
- [BarcodeAnchor](barcodeanchor.md)
- [CameraRegionAnchor](cameraregionanchor.md)
- [DeviceAnchor](deviceanchor.md)
- [EnvironmentProbeAnchor](environmentprobeanchor.md)
- [FieldOfViewAnchor](fieldofviewanchor.md)
- [HandAnchor](handanchor.md)
- [HandSkeleton.Joint](handskeleton/joint.md)
- [ImageAnchor](imageanchor.md)
- [MeshAnchor](meshanchor.md)
- [ObjectAnchor](objectanchor.md)
- [PlaneAnchor](planeanchor.md)
- [RoomAnchor](roomanchor.md)
- [WorldAnchor](worldanchor.md)

## See Also

- [Setting up access to ARKit data](../visionos/setting-up-access-to-arkit-data.md)
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
- [struct ARKitCoordinateSpace](arkitcoordinatespace.md)
  An object which represents an ARKit coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitcoordinatespaceproviding)*