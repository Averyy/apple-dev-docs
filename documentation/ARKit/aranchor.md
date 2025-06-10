# ARAnchor

**Framework**: ARKit  
**Kind**: class

An object that specifies the position and orientation of an item in the physical environment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARAnchor
```

## Mentions

- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)
- [Providing 3D Virtual Content with SceneKit](providing-3d-virtual-content-with-scenekit.md)
- [Providing 2D Virtual Content with SpriteKit](providing-2d-virtual-content-with-spritekit.md)

#### Overview

To track the static positions and orientations of real or virtual objects relative to the camera, create anchor objects and use the [`add(anchor:)`](arsession/add(anchor:).md) method to add them to your AR session.

> 💡 **Tip**:  Adding an anchor to the session helps ARKit to optimize world-tracking accuracy in the area around that anchor, so that virtual objects appear to stay in place relative to the real world. If a virtual object moves, remove the corresponding anchor from the old position and add one at the new position.

Some ARKit features automatically add special anchors to a session. World-tracking sessions can add [`ARPlaneAnchor`](arplaneanchor.md), [`ARObjectAnchor`](arobjectanchor.md), and [`ARImageAnchor`](arimageanchor.md) objects if you enable the corresponding features; face-tracking sessions add [`ARFaceAnchor`](arfaceanchor.md) objects.

##### Subclassing Notes

In addition to creating your own `ARAnchor` instances to track the real-world positions of your virtual content, you can also subclass `ARAnchor` to associate custom data with anchors you create. Ensure that your anchor classes behave correctly when ARKit updates frames or saves and loads anchors in an [`ARWorldMap`](arworldmap.md):

- Anchor subclasses must fullfill the requirements of the [`ARAnchorCopying`](aranchorcopying.md) protocol. ARKit calls [`init(anchor:)`](aranchorcopying/init(anchor:).md) (on a background thread) to copy instances of your anchor class from each [`ARFrame`](arframe.md) to the next. Your implementation of this initializer should copy the values of any custom properties your subclass adds.
- Anchor subclasses must also adopt the [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) protocol. Override [`encode(with:)`](https://developer.apple.com/documentation/Foundation/NSCoding/encode(with:)) and doc://com.apple.documentation/documentation/oslog/oslogentry/init(coder:) to save and restore the values your subclass’ custom properties when ARKit saves and loads them in a world map.
- Anchors are considered equal based on their [`identifier`](aranchor/identifier.md) property.
- Only anchors that do not adopt [`ARTrackable`](artrackable.md) are included when you save a world map.

## Topics

### Creating Anchors
- [init(transform: simd_float4x4)](aranchor/init(transform:).md)
  Creates a new anchor object with the specified transform.
- [init(name: String, transform: simd_float4x4)](aranchor/init(name:transform:).md)
  Creates a new anchor object with the specified transform and a descriptive name.
- [var name: String?](aranchor/name.md)
  A descriptive name for the anchor.
### Tracking Anchors
- [var identifier: UUID](aranchor/identifier.md)
  A unique identifier for the anchor.
- [var sessionIdentifier: UUID?](aranchor/sessionidentifier.md)
  The unique identifier of the session that owns this anchor.
- [var transform: simd_float4x4](aranchor/transform.md)
  A matrix encoding the position, orientation, and scale of the anchor relative to the world coordinate space of the AR session the anchor is placed in.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ARAppClipCodeAnchor](arappclipcodeanchor.md)
- [ARBodyAnchor](arbodyanchor.md)
- [AREnvironmentProbeAnchor](arenvironmentprobeanchor.md)
- [ARFaceAnchor](arfaceanchor.md)
- [ARGeoAnchor](argeoanchor.md)
- [ARImageAnchor](arimageanchor.md)
- [ARMeshAnchor](armeshanchor.md)
- [ARObjectAnchor](arobjectanchor.md)
- [ARParticipantAnchor](arparticipantanchor.md)
- [ARPlaneAnchor](arplaneanchor.md)
### Conforms To
- [ARAnchorCopying](aranchorcopying.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Verifying Device Support and User Permission](verifying-device-support-and-user-permission.md)
  Check whether your app can use ARKit and respect user privacy at runtime.
- [class ARSession](arsession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.
- [ARKit in iOS](arkit-in-ios.md)
  Integrate iOS device camera and motion features to produce augmented reality experiences in your app or game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor)*