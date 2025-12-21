# new CameraZoomRange(min, max)

**Framework**: MapKit JS  
**Kind**: init

Creates an instance of a camera zoom range object with the specified numeric arguments that specify minimum and maximum camera distances.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
constructor(min: number, max: number);
```

#### Discussion

Calling the constructor with minimal camera distance and maximum camera distance creates a [`CameraZoomRange`](camerazoomrange.md) instance that constrains the camera.

Both `minCameraDistance` and `maxCameraDistance` must be greater than or equal to `0.` The `minCameraDistance` must be less than or equal to the `maxCameraDistance`.

## See Also

- [new CameraZoomRange()](camerazoomrange/camerazoomrangeconstructor.md)
  Constructs an instance of a camera zoom range object with no minimum or maximum camera distance.
- [new CameraZoomRange(rangeParams)](camerazoomrange/camerazoomrangeconstructor1.md)
  Creates an instance of a camera zoom range object with an object literal.
- [interface CameraZoomRangeConstructorOptions](camerazoomrangeconstructoroptions.md)
  Initialization options for the camera zoom range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/camerazoomrange/camerazoomrangeconstructor2)*