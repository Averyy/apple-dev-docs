# bounds

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The bounds rectangle, which describes the item’s location and size in its own coordinate system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var bounds: CGRect { get }
```

## See Also

- [var frame: CGRect](nscollectionlayoutvisibleitem/frame.md)
  The frame rectangle, which describes the item’s location and size in its section’s coordinate system.
- [var center: CGPoint](nscollectionlayoutvisibleitem/center.md)
  The center point of the item’s frame rectangle.
- [var transform: CGAffineTransform](nscollectionlayoutvisibleitem/transform.md)
  The transform applied to the item, relative to the center of its bounds.
- [var transform3D: CATransform3D](nscollectionlayoutvisibleitem/transform3d.md)
  The 3D transform applied to the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutvisibleitem/bounds)*