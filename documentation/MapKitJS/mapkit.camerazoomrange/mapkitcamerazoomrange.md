# mapkit.CameraZoomRange

**Framework**: MapKit JS  
**Kind**: init

Describes the minimum and maximum camera distance in meters.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
new mapkit.CameraZoomRange(
	CameraZoomRangeConstructorOptions|number minCameraDistance,
	optional number maxCameraDistance
);
```

#### Discussion

Both [`minCameraDistance`](mapkit.camerazoomrange/mincameradistance.md) and [`maxCameraDistance`](mapkit.camerazoomrange/maxcameradistance.md) must be greater than or equal to `0.` The [`minCameraDistance`](mapkit.camerazoomrange/mincameradistance.md) must be lower than or equal to the [`maxCameraDistance`](mapkit.camerazoomrange/maxcameradistance.md).

## See Also

- [CameraZoomRangeConstructorOptions](camerazoomrangeconstructoroptions.md)
  Initialization options for the camera zoom range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.camerazoomrange/mapkit.camerazoomrange)*