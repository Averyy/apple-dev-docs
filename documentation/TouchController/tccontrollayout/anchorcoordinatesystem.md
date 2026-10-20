# anchorCoordinateSystem

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The coordinate system for the control’s anchor point.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem { get set }
```

```objc
@property (nonatomic, assign) TCControlLayoutAnchorCoordinateSystem anchorCoordinateSystem;
```

## See Also

### Inspecting the control layout
- [var anchor: TCControlLayoutAnchor](./anchor.md)
  The anchor point of the control.
- [var offset: CGPoint](./offset.md)
  The offset from the anchor point.
- [var position: CGPoint](./position.md)
  The calculated position of the control.
- [var size: CGSize](./size.md)
  The size of the control in points.
- [var zIndex: Int](./zindex.md)
  The z-index of the controlLayout, used for z-ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayout/anchorcoordinatesystem)*