# ARObjectAnchor

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

An anchor for a real-world 3D object that ARKit detects in the physical environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
class ARObjectAnchor
```

```objc
@interface ARObjectAnchor : ARAnchor
```

## Overview

When you run a world-tracking AR session and specify [`ARReferenceObject`](./arreferenceobject.md) objects for the session configuration’s [`detectionObjects`](./arworldtrackingconfiguration/detectionobjects.md) or [`trackingObjects`](./arworldtrackingconfiguration/trackingobjects.md) property, ARKit searches for those objects in the real-world environment. When the session recognizes an object, it automatically adds to its list of anchors an [`ARObjectAnchor`](./arobjectanchor.md) for each match.

For objects loaded from a `.referenceobject` file, use [`isTracked`](./artrackable/istracked.md) to determine whether ARKit is currently tracking the object. ARKit keeps the anchor in the session even when tracking is temporarily lost, so check [`isTracked`](./artrackable/istracked.md) before relying on the anchor’s transform. For objects loaded from the older `.arobject` format, [`isTracked`](./artrackable/istracked.md) always returns `true` and doesn’t reflect tracking state.

To place virtual 3D content that matches the position or size of the detected object, use the anchor’s inherited [`transform`](./aranchor/transform.md) property together with the [`center`](./arreferenceobject/center.md) and [`extent`](./arreferenceobject/extent.md) of the anchor’s [`referenceObject`](./arobjectanchor/referenceobject.md). Starting in iOS 27, you can also render the trained model directly: if the reference object’s [`usdzFile`](./arreferenceobject/usdzfile.md) URL is non-nil, load that USDZ file and overlay it on the real object.

## Topics

### Instance Properties
- [var isTracked: Bool](./arobjectanchor/istracked.md)
  A Boolean value indicating whether the anchor is currently being tracked.
- [var referenceObject: ARReferenceObject](./arobjectanchor/referenceobject.md)
  The detected object referenced by the object anchor.

## Relationships

### Inherits From
- [ARAnchor](./aranchor.md)
### Conforms To
- [ARAnchorCopying](./aranchorcopying.md)
- [ARTrackable](./artrackable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Object Tracking
- [Using a reference object with ARKit in iOS](../visionOS/using-a-reference-object-with-arkit-in-ios.md)
  Track a real-world object in your iOS app by using a reference-object file.
- [class ARReferenceObject](./arreferenceobject.md)
  A 3D object that ARKit can detect or track in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arobjectanchor)*