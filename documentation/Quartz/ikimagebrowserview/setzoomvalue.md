# setZoomValue(_:)

**Framework**: Quartz  
**Kind**: method

Sets the zoom value.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setZoomValue(_ aValue: Float)
```

#### Discussion

You must use `setZoomValue` or [`setCellSize(_:)`](ikimagebrowserview/setcellsize(_:).md), but not both. Setting the zoom value changes the cell size, and vice versa.

## Parameters

- `aValue`: The zoom value. This value should be greater or equal to zero and less or equal than one. A zoom value of zero corresponds to the minimum size (40x40 pixels). A zoom value of one means images fits the browser bounds. Other values are interpolated.

## See Also

- [func setCellSize(NSSize)](ikimagebrowserview/setcellsize(_:).md)
  Sets the cell  size.
- [func zoomValue() -> Float](ikimagebrowserview/zoomvalue.md)
  Returns the current zoom value.
- [func setContentResizingMask(Int)](ikimagebrowserview/setcontentresizingmask(_:).md)
  Determines how the receiver resizes its content when zooming.
- [func contentResizingMask() -> Int](ikimagebrowserview/contentresizingmask.md)
  Returns the receiver’s content resizing mask, which determines how its content is resized while zooming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setzoomvalue(_:))*