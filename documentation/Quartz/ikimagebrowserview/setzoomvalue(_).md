# setZoomValue(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the zoom value.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setZoomValue(_ aValue: Float)
```

```objc
- (void) setZoomValue:(float) aValue;
```

#### Discussion

You must use `setZoomValue` or [`setCellSize(_:)`](./setcellsize%28_%29.md), but not both. Setting the zoom value changes the cell size, and vice versa.

## Parameters

- `aValue`: The zoom value. This value should be greater or equal to zero and less or equal than one. A zoom value of zero corresponds to the minimum size (40x40 pixels). A zoom value of one means images fits the browser bounds. Other values are interpolated.

## See Also

### Related Documentation
- [func setCellSize(NSSize)](./setcellsize%28_%29.md)
  Sets the cell  size.
### Zooming and Resizing
- [func zoomValue() -> Float](./zoomvalue%28%29.md)
  Returns the current zoom value.
- [func setContentResizingMask(Int)](./setcontentresizingmask%28_%29.md)
  Determines how the receiver resizes its content when zooming.
- [func contentResizingMask() -> Int](./contentresizingmask%28%29.md)
  Returns the receiver’s content resizing mask, which determines how its content is resized while zooming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setzoomvalue(_:))*