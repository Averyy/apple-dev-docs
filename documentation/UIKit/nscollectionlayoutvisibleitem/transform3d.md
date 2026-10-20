# transform3D

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The 3D transform applied to the item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var transform3D: CATransform3D { get set }
```

```objc
@property (nonatomic) CATransform3D transform3D;
```

## See Also

### Configuring position
- [var frame: CGRect](./frame.md)
  The frame rectangle, which describes the item’s location and size in its section’s coordinate system.
- [var bounds: CGRect](./bounds.md)
  The bounds rectangle, which describes the item’s location and size in its own coordinate system.
- [var center: CGPoint](./center.md)
  The center point of the item’s frame rectangle.
- [var transform: CGAffineTransform](./transform.md)
  The transform applied to the item, relative to the center of its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutvisibleitem/transform3d)*