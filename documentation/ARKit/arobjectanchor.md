# ARObjectAnchor

**Framework**: ARKit  
**Kind**: class

An anchor for a real-world 3D object that ARKit detects in the physical environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARObjectAnchor
```

#### Overview

When you run a world-tracking AR session and specify [`ARReferenceObject`](arreferenceobject.md) objects for the session configuration’s [`detectionObjects`](arworldtrackingconfiguration/detectionobjects.md) property, ARKit searches for those objects in the real-world environment. When the session recognizes an object, it automatically adds to its list of anchors an [`ARObjectAnchor`](arobjectanchor.md) for each detected object.

To place virtual 3D content that matches the position or size of the detected object, use the anchor’s inherited [`transform`](aranchor/transform.md) property together with the [`center`](arreferenceobject/center.md) and [`extent`](arreferenceobject/extent.md) of the anchor’s [`referenceObject`](arobjectanchor/referenceobject.md).

## Topics

### Identifying Detected Objects
- [var referenceObject: ARReferenceObject](arobjectanchor/referenceobject.md)
  The detected object referenced by the object anchor.

## Relationships

### Inherits From
- [ARAnchor](aranchor.md)
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

## See Also

- [Visualizing and interacting with a reconstructed scene](visualizing-and-interacting-with-a-reconstructed-scene.md)
  Estimate the shape of the physical environment using a polygonal mesh.
- [Scanning and Detecting 3D Objects](scanning-and-detecting-3d-objects.md)
  Record spatial features of real-world objects, then use the results to find those objects in the user’s environment and trigger AR content.
- [class ARReferenceObject](arreferenceobject.md)
  The description of a 3D object that you want ARKit to detect in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arobjectanchor)*