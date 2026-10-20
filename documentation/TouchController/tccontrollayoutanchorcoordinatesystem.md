# TCControlLayoutAnchorCoordinateSystem

**Framework**: Touch Controller  
**Kind**: enum  
**Role**: Enumeration

Defines the coodinate system for an anchor point.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum TCControlLayoutAnchorCoordinateSystem
```

```c
enum TCControlLayoutAnchorCoordinateSystem : NSInteger;
```

## Topics

### Anchors
- [TCControlLayoutAnchorCoordinateSystem.absolute](./tccontrollayoutanchorcoordinatesystem/absolute.md)
  Anchors are positioned according to the absolute edges of the sceren.
- [TCControlLayoutAnchorCoordinateSystem.relative](./tccontrollayoutanchorcoordinatesystem/relative.md)
  Anchors are positioned relative to the device’s screen size.
### Creating a layout anchor
- [init?(rawValue: Int)](./tccontrollayoutanchorcoordinatesystem/init%28rawvalue%29.md)

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
- [enum TCControlLayoutAnchor](./tccontrollayoutanchor.md)
  Defines the anchor point for a control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](./tcbuttondescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayoutanchorcoordinatesystem)*