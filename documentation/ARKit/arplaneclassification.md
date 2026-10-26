# ARPlaneClassification

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Possible characterizations of real-world surfaces represented by plane anchors.

**Availability**:
- iOS
- iPadOS

## Declaration

```c
enum ARPlaneClassification : NSInteger;
```

#### Overview

You get values of this type from a plane anchor’s [`classification`](./arplaneanchor/classification-2hi2p.md) property, identifying the likely type of real-world surface for a detected plane anchor.

## Topics

### Plane Classifications
- [ARPlaneClassificationNone](./arplaneclassification/arplaneclassificationnone.md)
  No classification is available for the plane anchor.
- [ARPlaneClassificationWall](./arplaneclassification/arplaneclassificationwall.md)
  The plane anchor represents a real-world wall or similar large vertical surface.
- [ARPlaneClassificationFloor](./arplaneclassification/arplaneclassificationfloor.md)
  The plane anchor represents a real-world floor, ground plane, or similar large horizontal surface.
- [ARPlaneClassificationCeiling](./arplaneclassification/arplaneclassificationceiling.md)
  The plane anchor represents a real-world ceiling or similar overhead horizontal surface.
- [ARPlaneClassificationTable](./arplaneclassification/arplaneclassificationtable.md)
  The plane anchor represents a real-world table, desk, bar, or similar flat surface.
- [ARPlaneClassificationSeat](./arplaneclassification/arplaneclassificationseat.md)
  The plane anchor represents a real-world chair, stool, bench or similar flat surface.
- [ARPlaneClassificationDoor](./arplaneclassification/arplaneclassificationdoor.md)
  The plane anchor represents a real-world door, or similar archway.
- [ARPlaneClassificationWindow](./arplaneclassification/arplaneclassificationwindow.md)
  The plane anchor fits the description of a real-world window.

## See Also

### Classifying a Plane
- [class var isClassificationSupported: Bool](./arplaneanchor/isclassificationsupported.md)
  A Boolean value that indicates whether plane classification is available on the current device.
- [classification](./arplaneanchor/classification-2hi2p.md)
  A general characterization of what kind of real-world surface the plane anchor represents.
- [classificationStatus](./arplaneanchor/classificationstatus.md)
  The current state of ARKit’s process for classifying the plane anchor.
- [ARPlaneClassificationStatus](./arplaneclassificationstatus.md)
  Possible states of ARKit’s process for classifying plane anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassification)*