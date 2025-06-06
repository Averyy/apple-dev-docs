# ARAnchorCopying

**Framework**: ARKit  
**Kind**: protocol

Support for custom anchor subclasses.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol ARAnchorCopying : NSCopying
```

#### Overview

An [`ARAnchor`](aranchor.md) (or an instance of any anchor subclass) represents a position and orientation in world space, and optionally associates extra information with that point (like a name, or plane or image detection data). Each time ARKit generates an [`ARFrame`](arframe.md) object (describing the current environment as of a specific frame of live camera video), ARKit updates the [`anchors`](arframe/anchors.md) associated with the session as of that moment. Because anchor objects are immutable, ARKit must copy them to make changes from one [`ARFrame`](arframe.md) to the next.

If you create your own ARAnchor subclass, you must implement the [`init(anchor:)`](aranchorcopying/init(anchor:).md) initializer required by this protocol. To ensure that any custom information in your subclass is maintained between successive frames, your implementation should copy any custom properties it declares.

## Topics

### Copying Anchors
- [init(anchor: ARAnchor)](aranchorcopying/init(anchor:).md)
  Initializes a new anchor by copying custom information from another anchor.

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
### Conforming Types
- [ARAnchor](aranchor.md)
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

## See Also

- [class ARAnchor](aranchor.md)
  An object that specifies the position and orientation of an item in the physical environment.
- [protocol ARTrackable](artrackable.md)
  An interface for objects that track the location of real-world objects or locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchorcopying)*