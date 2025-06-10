# transform

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The transform applied to the item, relative to the center of its bounds.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var transform: CGAffineTransform { get set }
```

## See Also

- [var frame: CGRect](nscollectionlayoutvisibleitem/frame.md)
  The frame rectangle, which describes the item’s location and size in its section’s coordinate system.
- [var bounds: CGRect](nscollectionlayoutvisibleitem/bounds.md)
  The bounds rectangle, which describes the item’s location and size in its own coordinate system.
- [var center: CGPoint](nscollectionlayoutvisibleitem/center.md)
  The center point of the item’s frame rectangle.
- [var transform3D: CATransform3D](nscollectionlayoutvisibleitem/transform3d.md)
  The 3D transform applied to the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutvisibleitem/transform)*