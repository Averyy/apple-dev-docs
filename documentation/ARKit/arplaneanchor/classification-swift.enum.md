# ARPlaneAnchor.Classification

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Possible characterizations of real-world surfaces represented by plane anchors.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
enum Classification
```

#### Overview

You get values of this type from a plane anchor’s [`classification`](./classification-2r4x8.md) property, identifying both the likely type of real-world surface for a detected plane anchor and the state of ARKit’s plane classification process.

## Topics

### Plane Classifications
- [ARPlaneAnchor.Classification.wall](./classification-swift.enum/wall.md)
  The plane anchor represents a real-world wall or similar large vertical surface.
- [ARPlaneAnchor.Classification.floor](./classification-swift.enum/floor.md)
  The plane anchor represents a real-world floor, ground plane, or similar large horizontal surface.
- [ARPlaneAnchor.Classification.ceiling](./classification-swift.enum/ceiling.md)
  The plane anchor represents a real-world ceiling or similar overhead horizontal surface.
- [ARPlaneAnchor.Classification.table](./classification-swift.enum/table.md)
  The plane anchor represents a real-world table, desk, bar, or similar flat surface.
- [ARPlaneAnchor.Classification.seat](./classification-swift.enum/seat.md)
  The plane anchor represents a real-world chair, stool, bench or similar flat surface.
- [ARPlaneAnchor.Classification.door](./classification-swift.enum/door.md)
  The plane anchor represents a real-world door or similar vertical surface.
- [ARPlaneAnchor.Classification.window](./classification-swift.enum/window.md)
  The plane anchor represents a real-world window or similar vertical surface.
### Missing Classification Status
- [case none(ARPlaneAnchor.Classification.Status)](./classification-swift.enum/none%28_%29.md)
  No classification is available for the plane anchor.
- [ARPlaneAnchor.Classification.Status](./classification-swift.enum/status.md)
  Reasons ARKit is unable to classify a plane.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Classifying a Plane
- [class var isClassificationSupported: Bool](./isclassificationsupported.md)
  A Boolean value that indicates whether plane classification is available on the current device.
- [var classification: ARPlaneAnchor.Classification](./classification-2r4x8.md)
  A general characterization of what kind of real-world surface the plane anchor represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-swift.enum)*