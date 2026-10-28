# AxisDirectionConvention.rightUpBack

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Case

The convention that uses a counterclockwise winding order and positions the leading pixel at the top-left corner of the view.

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
case rightUpBack
```

```c
cp_axis_direction_convention_right_up_back
```

## Discussion

This convention positions the left-most pixel at the left edge of the view and the top-most pixel at the top edge of the view, and the system renders with a counterclockwise winding order.

## See Also

### Getting the axis directions
- [AxisDirectionConvention.rightUpForward](./rightupforward.md)
  The convention that uses a clockwise winding order and positions the leading pixel at the top-left corner of the view.
- [AxisDirectionConvention.rightDownBack](./rightdownback.md)
  The convention that uses a counterclockwise winding order and positions the leading pixel at the bottom-left corner of the view.
- [AxisDirectionConvention.rightDownForward](./rightdownforward.md)
  The convention that uses a clockwise winding order and positions the leading pixel at the bottom-left corner of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/axisdirectionconvention/rightupback)*