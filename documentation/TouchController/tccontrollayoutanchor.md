# TCControlLayoutAnchor

**Framework**: Touch Controller  
**Kind**: enum  
**Role**: Enumeration

Defines the anchor point for a control.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum TCControlLayoutAnchor
```

```c
enum TCControlLayoutAnchor : NSInteger;
```

## Topics

### Anchors
- [TCControlLayoutAnchor.bottomCenter](./tccontrollayoutanchor/bottomcenter.md)
  Anchors to the bottom-center, relative to the screen size.
- [TCControlLayoutAnchor.bottomLeft](./tccontrollayoutanchor/bottomleft.md)
  Anchors to the bottom-left corner, relative to the screen size.
- [TCControlLayoutAnchor.bottomRight](./tccontrollayoutanchor/bottomright.md)
  Anchors to the bottom-right corner, relative to the screen size.
- [TCControlLayoutAnchor.center](./tccontrollayoutanchor/center.md)
  Anchors to the center, relative to the screen size.
- [TCControlLayoutAnchor.centerLeft](./tccontrollayoutanchor/centerleft.md)
  Anchors to the center-left, relative to the screen size.
- [TCControlLayoutAnchor.centerRight](./tccontrollayoutanchor/centerright.md)
  Anchors to the center-right, relative to the screen size.
- [TCControlLayoutAnchor.topCenter](./tccontrollayoutanchor/topcenter.md)
  Anchors to the top-center, relative to the screen size.
- [TCControlLayoutAnchor.topLeft](./tccontrollayoutanchor/topleft.md)
  Anchors to the top-left corner, relative to the screen size.
- [TCControlLayoutAnchor.topRight](./tccontrollayoutanchor/topright.md)
  Anchors to the top-right corner, relative to the screen size.
### Creating a layout anchor
- [init?(rawValue: Int)](./tccontrollayoutanchor/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing the anchor
- [var anchor: TCControlLayoutAnchor](./tcbuttondescriptor/anchor.md)
  The anchor point that the button’s offset is relative to.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](./tcbuttondescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [enum TCControlLayoutAnchorCoordinateSystem](./tccontrollayoutanchorcoordinatesystem.md)
  Defines the coodinate system for an anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayoutanchor)*