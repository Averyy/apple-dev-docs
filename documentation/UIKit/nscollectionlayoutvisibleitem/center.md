# center

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The center point of the item’s frame rectangle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var center: CGPoint { get set }
```

```objc
@property (nonatomic) CGPoint center;
```

## See Also

### Configuring position
- [var frame: CGRect](./frame.md)
  The frame rectangle, which describes the item’s location and size in its section’s coordinate system.
- [var bounds: CGRect](./bounds.md)
  The bounds rectangle, which describes the item’s location and size in its own coordinate system.
- [var transform: CGAffineTransform](./transform.md)
  The transform applied to the item, relative to the center of its bounds.
- [var transform3D: CATransform3D](./transform3d.md)
  The 3D transform applied to the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutvisibleitem/center)*