# Anchor

**Framework**: ARKit  
**Kind**: protocol

The identity, location, and orientation of an object in world space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
protocol Anchor : CustomStringConvertible, Identifiable, Sendable
```

## Topics

### Inspecting an anchor
- [var id: UUID](anchor/id.md)
  A unique identifier that distinguishes this anchor from all other anchors.
- [var timestamp: TimeInterval](anchor/timestamp.md)
- [var originFromAnchorTransform: simd_float4x4](anchor/originfromanchortransform.md)
  The position and orientation of this anchor in world space.
### Tracking anchors over time
- [struct AnchorUpdate](anchorupdate.md)
  Information about the event that updated an anchor.
- [struct AnchorUpdateSequence](anchorupdatesequence.md)
  An asynchronous sequence of updates to anchors.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
### Inherited By
- [TrackableAnchor](trackableanchor.md)
### Conforming Types
- [BarcodeAnchor](barcodeanchor.md)
- [DeviceAnchor](deviceanchor.md)
- [EnvironmentProbeAnchor](environmentprobeanchor.md)
- [HandAnchor](handanchor.md)
- [ImageAnchor](imageanchor.md)
- [MeshAnchor](meshanchor.md)
- [ObjectAnchor](objectanchor.md)
- [PlaneAnchor](planeanchor.md)
- [RoomAnchor](roomanchor.md)
- [WorldAnchor](worldanchor.md)

## See Also

- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [class ARKitSession](arkitsession.md)
  The main entry point for receiving data from ARKit.
- [protocol DataProvider](dataprovider.md)
  A source of live data from ARKit.
- [ARKit in visionOS](arkit-in-visionos.md)
  Create immersive augmented reality experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchor)*