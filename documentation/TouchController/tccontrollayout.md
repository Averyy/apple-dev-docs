# TCControlLayout

**Framework**: Touch Controller  
**Kind**: protocol

A protocol defining the controlLayout properties for a control.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol TCControlLayout : NSObjectProtocol
```

## Topics

### Inspecting the control layout
- [var anchor: TCControlLayoutAnchor](tccontrollayout/anchor.md)
  The anchor point of the control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](tccontrollayout/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [var offset: CGPoint](tccontrollayout/offset.md)
  The offset from the anchor point.
- [var position: CGPoint](tccontrollayout/position.md)
  The calculated position of the control.
- [var size: CGSize](tccontrollayout/size.md)
  The size of the control in points.
- [var zIndex: Int](tccontrollayout/zindex.md)
  The z-index of the controlLayout, used for z-ordering.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [TCControl](tccontrol.md)
### Conforming Types
- [TCButton](tcbutton.md)
- [TCDirectionPad](tcdirectionpad.md)
- [TCSwitch](tcswitch.md)
- [TCThrottle](tcthrottle.md)
- [TCThumbstick](tcthumbstick.md)
- [TCTouchpad](tctouchpad.md)

## See Also

- [class TCControlContents](tccontrolcontents.md)
  Represents the visual contents of a touch control.
- [class TCControlImage](tccontrolimage.md)
  Represents an image to be rendered using Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayout)*