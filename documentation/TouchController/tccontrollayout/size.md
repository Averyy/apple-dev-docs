# size

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The size of the control in points.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var size: CGSize { get set }
```

```objc
@property (nonatomic, assign) CGSize size;
```

## See Also

### Inspecting the control layout
- [var anchor: TCControlLayoutAnchor](./anchor.md)
  The anchor point of the control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](./anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [var offset: CGPoint](./offset.md)
  The offset from the anchor point.
- [var position: CGPoint](./position.md)
  The calculated position of the control.
- [var zIndex: Int](./zindex.md)
  The z-index of the controlLayout, used for z-ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayout/size)*