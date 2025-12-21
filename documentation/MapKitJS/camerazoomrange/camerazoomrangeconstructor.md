# new CameraZoomRange()

**Framework**: MapKit JS  
**Kind**: init

Constructs an instance of a camera zoom range object with no minimum or maximum camera distance.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
constructor();
```

#### Discussion

The zoom range describes the minimum and maximum camera distance in meters.

> **Note**: Calling the constructor with no arguments creates a [`CameraZoomRange`](camerazoomrange.md) instance that doesn’t constrain the camera.

## See Also

- [new CameraZoomRange(rangeParams)](camerazoomrange/camerazoomrangeconstructor1.md)
  Creates an instance of a camera zoom range object with an object literal.
- [new CameraZoomRange(min, max)](camerazoomrange/camerazoomrangeconstructor2.md)
  Creates an instance of a camera zoom range object with the specified numeric arguments that specify minimum and maximum camera distances.
- [interface CameraZoomRangeConstructorOptions](camerazoomrangeconstructoroptions.md)
  Initialization options for the camera zoom range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/camerazoomrange/camerazoomrangeconstructor)*