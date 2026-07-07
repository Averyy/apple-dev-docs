# TCControlLayoutAnchorCoordinateSystem

**Framework**: Touch Controller  
**Kind**: enum

Defines the coodinate system for an anchor point.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum TCControlLayoutAnchorCoordinateSystem
```

## Topics

### Anchors
- [TCControlLayoutAnchorCoordinateSystem.absolute](tccontrollayoutanchorcoordinatesystem/absolute.md)
  Anchors are positioned according to the absolute edges of the sceren.
- [TCControlLayoutAnchorCoordinateSystem.relative](tccontrollayoutanchorcoordinatesystem/relative.md)
  Anchors are positioned relative to the device’s screen size.
### Creating a layout anchor
- [init?(rawValue: Int)](tccontrollayoutanchorcoordinatesystem/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var anchor: TCControlLayoutAnchor](tcbuttondescriptor/anchor.md)
  The anchor point that the button’s offset is relative to.
- [enum TCControlLayoutAnchor](tccontrollayoutanchor.md)
  Defines the anchor point for a control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](tcbuttondescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayoutanchorcoordinatesystem)*