# ARPlaneClassificationStatus

**Framework**: ARKit  
**Kind**: enum

Possible states of ARKit’s process for classifying plane anchors.

## Declaration

```swift
enum ARPlaneClassificationStatus : NSInteger;
```

#### Overview

You get values of this type from a plane anchor’s [`classificationStatus`](arplaneanchor/classificationstatus.md) property, describing the state of ARKit’s plane classification process.

## Topics

### Classification Status
- [ARPlaneClassificationStatusNotAvailable](arplaneclassificationstatus/arplaneclassificationstatusnotavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneClassificationStatusUndetermined](arplaneclassificationstatus/arplaneclassificationstatusundetermined.md)
  ARKit has not yet produced a classification for the plane anchor.
- [ARPlaneClassificationStatusUnknown](arplaneclassificationstatus/arplaneclassificationstatusunknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.
- [ARPlaneClassificationStatusKnown](arplaneclassificationstatus/arplaneclassificationstatusknown.md)
  ARKit has completed its classfication process for the plane anchor.

## See Also

- [ar_plane_alignment_t](ar_plane_alignment_t.md)
  The kinds of alignment — horizontal or vertical — that a plane anchor can have.
- [ar_plane_classification_t](ar_plane_classification_t.md)
  The kinds of object classification a plane anchor can have.
- [ar_plane_classification_ceiling](ar_plane_classification_t/ar_plane_classification_ceiling.md)
  A ceiling.
- [ar_plane_classification_door](ar_plane_classification_t/ar_plane_classification_door.md)
  A door.
- [ar_plane_classification_floor](ar_plane_classification_t/ar_plane_classification_floor.md)
  A floor.
- [ar_plane_classification_seat](ar_plane_classification_t/ar_plane_classification_seat.md)
  A seat.
- [ar_plane_classification_status_not_available](ar_plane_classification_t/ar_plane_classification_status_not_available.md)
  A plane classification is currently unavailable.
- [ar_plane_classification_status_undetermined](ar_plane_classification_t/ar_plane_classification_status_undetermined.md)
  A plane classification is undetermined.
- [ar_plane_classification_status_unknown](ar_plane_classification_t/ar_plane_classification_status_unknown.md)
  A plane classification isn’t one of the known classes.
- [ar_plane_classification_table](ar_plane_classification_t/ar_plane_classification_table.md)
  A table.
- [ar_plane_classification_wall](ar_plane_classification_t/ar_plane_classification_wall.md)
  A wall.
- [ar_plane_classification_window](ar_plane_classification_t/ar_plane_classification_window.md)
  A window.
- [ar_plane_anchor_get_alignment](ar_plane_anchor_get_alignment.md)
  Gets the alignment — horizontal or vertical — of a plane anchor relative to gravity.
- [ar_plane_anchor_get_geometry](ar_plane_anchor_get_geometry.md)
  Gets the shape of a plane anchor.
- [ar_plane_anchor_get_plane_classification](ar_plane_anchor_get_plane_classification.md)
  Gets the kind of real-world object that ARKit determines the plane anchor might be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassificationstatus)*