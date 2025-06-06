# ARTrackable

**Framework**: ARKit  
**Kind**: protocol

An interface for objects that track the location of real-world objects or locations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol ARTrackable : NSObjectProtocol
```

#### Overview

This protocol is adopted by ARKit classes, such as the [`ARFaceAnchor`](arfaceanchor.md) class, that represent moving objects in a scene.

ARKit automatically manages representations of such objects in an active AR session, ensuring that changes in the real-world object’s position and orientation (the [`transform`](aranchor/transform.md) property for anchors) are reflected in corresponding ARKit objects. The [`isTracked`](artrackable/istracked.md) property indicates whether the current transform is valid with respect to movement of the real-world object.

Trackable anchor classes affect other ARKit behaviors:

- The [`getCurrentWorldMap(completionHandler:)`](arsession/getcurrentworldmap(completionhandler:).md) method automatically includes only non-trackable anchors in the [`ARWorldMap`](arworldmap.md) it creates. (After you create a world map, you can add other anchors to it if you choose.)
- [`ARSCNView`](arscnview.md) and [`ARSKView`](arskview.md) automatically hide the nodes for anchors whose [`isTracked`](artrackable/istracked.md) property is [`false`](https://developer.apple.com/documentation/swift/false).
- World-tracking sessions use non-trackable anchors to optimize tracking quality in the area around each anchor. Trackable anchors do not affect world tracking.

## Topics

### Monitoring Tracking State
- [var isTracked: Bool](artrackable/istracked.md)
  A Boolean value that indicates whether the object’s transform is valid.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [ARAppClipCodeAnchor](arappclipcodeanchor.md)
- [ARBodyAnchor](arbodyanchor.md)
- [ARFaceAnchor](arfaceanchor.md)
- [ARGeoAnchor](argeoanchor.md)
- [ARImageAnchor](arimageanchor.md)

## See Also

- [class ARAnchor](aranchor.md)
  An object that specifies the position and orientation of an item in the physical environment.
- [protocol ARAnchorCopying](aranchorcopying.md)
  Support for custom anchor subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackable)*