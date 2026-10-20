# anchor

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The anchor point of the control.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var anchor: TCControlLayoutAnchor { get set }
```

```objc
@property (nonatomic, assign) TCControlLayoutAnchor anchor;
```

## See Also

### Inspecting the control layout
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](./anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [var offset: CGPoint](./offset.md)
  The offset from the anchor point.
- [var position: CGPoint](./position.md)
  The calculated position of the control.
- [var size: CGSize](./size.md)
  The size of the control in points.
- [var zIndex: Int](./zindex.md)
  The z-index of the controlLayout, used for z-ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayout/anchor)*