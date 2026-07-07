# TCDirectionPadDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a directional pad.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCDirectionPadDescriptor
```

## Topics

### Creating the descriptor
- [init()](tcdirectionpaddescriptor/init.md)
  Creates a new instance with default values.
### Inspecting the descriptor
- [var compositeLabel: TCControlLabel?](tcdirectionpaddescriptor/compositelabel.md)
  A composite control label.
- [var downContents: TCControlContents?](tcdirectionpaddescriptor/downcontents.md)
  The contents for the down button.
- [var downLabel: TCControlLabel?](tcdirectionpaddescriptor/downlabel.md)
  The label for the down button, if the control is not a composite direction pad.
- [var highlightDuration: TimeInterval](tcdirectionpaddescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var inputIsMutuallyExclusive: Bool](tcdirectionpaddescriptor/inputismutuallyexclusive.md)
  A Boolean value that indicates whether the control has mutally exclusive input.
- [var isDigital: Bool](tcdirectionpaddescriptor/isdigital.md)
  A Boolean value that indicates whether the control behaves as a digital button.
- [var isRadial: Bool](tcdirectionpaddescriptor/isradial.md)
  A Boolean value that indicates whether the control behaves as a swipeable radial button.
- [var leftContents: TCControlContents?](tcdirectionpaddescriptor/leftcontents.md)
  The contents for the left button.
- [var leftLabel: TCControlLabel?](tcdirectionpaddescriptor/leftlabel.md)
  The label for the left button, if the control is not a composite direction pad.
- [var offset: CGPoint](tcdirectionpaddescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var rightContents: TCControlContents?](tcdirectionpaddescriptor/rightcontents.md)
  The contents for the right button.
- [var rightLabel: TCControlLabel?](tcdirectionpaddescriptor/rightlabel.md)
  The label for the right button, if the control is not a composite direction pad.
- [var size: CGSize](tcdirectionpaddescriptor/size.md)
  The size (width, height) of the direction pad in points.
- [var upContents: TCControlContents?](tcdirectionpaddescriptor/upcontents.md)
  The contents for the up button.
- [var upLabel: TCControlLabel?](tcdirectionpaddescriptor/uplabel.md)
  The label for the up button, if the control isn’t a composite direction pad.
- [var zIndex: Int](tcdirectionpaddescriptor/zindex.md)
  The z-index of the direction pad. A lower z-index is drawn first.
### Accessing the anchor
- [var anchor: TCControlLayoutAnchor](tcdirectionpaddescriptor/anchor.md)
  The anchor point that the direction pad’s offset is relative to.
- [enum TCControlLayoutAnchor](tccontrollayoutanchor.md)
  Defines the anchor point for a control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](tcdirectionpaddescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [enum TCControlLayoutAnchorCoordinateSystem](tccontrollayoutanchorcoordinatesystem.md)
  Defines the coodinate system for an anchor point.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcdirectionpaddescriptor/collidershape.md)
  The shape of collider to use for the direction pad.
- [enum TCColliderShape](tccollidershape.md)
  Defines the shape of a control collider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func addDirectionPad(descriptor: TCDirectionPadDescriptor) -> TCDirectionPad](tctouchcontroller/adddirectionpad(descriptor:).md)
  Creates a new direction pad control with the provided descriptor, and adds it to the touch controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcdirectionpaddescriptor)*