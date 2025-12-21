# new CameraZoomRange(rangeParams)

**Framework**: MapKit JS  
**Kind**: init

Creates an instance of a camera zoom range object with an object literal.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
constructor(rangeParams: CameraZoomRangeConstructorOptions);
```

#### Discussion

Calling the constructor with an [`CameraZoomRangeConstructorOptions`](camerazoomrangeconstructoroptions.md) object literal creates a [`CameraZoomRange`](camerazoomrange.md) instance that constrains the camera.

Both [`minCameraDistance`](camerazoomrangeconstructoroptions/mincameradistance.md) and [`maxCameraDistance`](camerazoomrangeconstructoroptions/maxcameradistance.md) must be greater than or equal to `0.` The [`minCameraDistance`](camerazoomrangeconstructoroptions/mincameradistance.md) must be lower than or equal to the [`maxCameraDistance`](camerazoomrangeconstructoroptions/maxcameradistance.md).

## See Also

- [new CameraZoomRange()](camerazoomrange/camerazoomrangeconstructor.md)
  Constructs an instance of a camera zoom range object with no minimum or maximum camera distance.
- [new CameraZoomRange(min, max)](camerazoomrange/camerazoomrangeconstructor2.md)
  Creates an instance of a camera zoom range object with the specified numeric arguments that specify minimum and maximum camera distances.
- [interface CameraZoomRangeConstructorOptions](camerazoomrangeconstructoroptions.md)
  Initialization options for the camera zoom range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/camerazoomrange/camerazoomrangeconstructor1)*