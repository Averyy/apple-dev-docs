# layoutMarginsGuide

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A layout guide that provides the recommended amount of padding for content inside of a view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var layoutMarginsGuide: NSLayoutGuide { get }
```

```objc
@property (strong, readonly) NSLayoutGuide * layoutMarginsGuide;
```

## Discussion

To ensure you pad your view’s content by the correct amount, constrain against the anchors of the layout margins guide on all sides. The system automatically updates the guide when a view becomes the content view.

For views that aren’t the content view, the layout margins guide is equivalent to the system’s standard spacing from the safe area.

## See Also

### Managing Layout Guides
- [func addLayoutGuide(NSLayoutGuide)](./addlayoutguide%28_%29.md)
  Adds the provided layout guide to the view.
- [func removeLayoutGuide(NSLayoutGuide)](./removelayoutguide%28_%29.md)
  Removes the provided layout guide from the view.
- [var layoutGuides: [NSLayoutGuide]](./layoutguides.md)
  The array of layout guide objects owned by this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layoutmarginsguide)*