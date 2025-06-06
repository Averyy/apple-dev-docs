# layoutMarginsGuide

**Framework**: AppKit  
**Kind**: property

A layout guide that provides the recommended amount of padding for content inside of a view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var layoutMarginsGuide: NSLayoutGuide { get }
```

#### Discussion

To ensure you pad your view’s content by the correct amount, constrain against the anchors of the layout margins guide on all sides. The system automatically updates the guide when a view becomes the content view.

For views that aren’t the content view, the layout margins guide is equivalent to the system’s standard spacing from the safe area.

## See Also

- [func addLayoutGuide(NSLayoutGuide)](nsview/addlayoutguide(_:).md)
  Adds the provided layout guide to the view.
- [func removeLayoutGuide(NSLayoutGuide)](nsview/removelayoutguide(_:).md)
  Removes the provided layout guide from the view.
- [var layoutGuides: [NSLayoutGuide]](nsview/layoutguides.md)
  The array of layout guide objects owned by this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layoutmarginsguide)*