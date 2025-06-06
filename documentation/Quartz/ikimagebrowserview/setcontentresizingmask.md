# setContentResizingMask(_:)

**Framework**: Quartz  
**Kind**: method

Determines how the receiver resizes its content when zooming.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setContentResizingMask(_ mask: Int)
```

## Parameters

- `mask`: A resizing mask. You specify a mask by combining any of the following options using the C bitwise   operator:  ,  . Other values are ignored.

## See Also

- [func setZoomValue(Float)](ikimagebrowserview/setzoomvalue(_:).md)
  Sets the zoom value.
- [func zoomValue() -> Float](ikimagebrowserview/zoomvalue.md)
  Returns the current zoom value.
- [func contentResizingMask() -> Int](ikimagebrowserview/contentresizingmask.md)
  Returns the receiver’s content resizing mask, which determines how its content is resized while zooming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setcontentresizingmask(_:))*