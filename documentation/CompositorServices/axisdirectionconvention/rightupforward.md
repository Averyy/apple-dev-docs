# AxisDirectionConvention.rightUpForward

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Case

The convention that uses a clockwise winding order and positions the leading pixel at the top-left corner of the view.

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
case rightUpForward
```

```c
cp_axis_direction_convention_right_up_forward
```

## Discussion

This convention positions the left-most pixel at the left edge of the view and the top-most pixel at the top edge of the view, and the system renders with a clockwise winding order.

## See Also

### Getting the axis directions
- [AxisDirectionConvention.rightUpBack](./rightupback.md)
  The convention that uses a counterclockwise winding order and positions the leading pixel at the top-left corner of the view.
- [AxisDirectionConvention.rightDownBack](./rightdownback.md)
  The convention that uses a counterclockwise winding order and positions the leading pixel at the bottom-left corner of the view.
- [AxisDirectionConvention.rightDownForward](./rightdownforward.md)
  The convention that uses a clockwise winding order and positions the leading pixel at the bottom-left corner of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/axisdirectionconvention/rightupforward)*