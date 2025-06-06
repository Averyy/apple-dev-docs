# CameraZoomRangeLiteral

**Framework**: MapKit JS  
**Kind**: struct

An object literal containing minimum and maximum camera distance in meters.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
dictionary CameraZoomRangeLiteral {
	number minCameraDistance;
	number maxCameraDistance;
};
```

#### Overview

Both `minCameraDistance` and `maxCameraDistance` must be greater than or equal to `0.` The `minCameraDistance` must be lower than or equal to the `maxCameraDistance`.

## Topics

### Setting Distance Constraints
- [minCameraDistance](camerazoomrangeliteral/mincameradistance.md)
  The minimum allowed distance of the camera from the center of the map in meters.
- [maxCameraDistance](camerazoomrangeliteral/maxcameradistance.md)
  The maximum allowed distance of the camera from the center of the map in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/camerazoomrangeliteral)*