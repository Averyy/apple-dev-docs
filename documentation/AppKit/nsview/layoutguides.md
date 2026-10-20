# layoutGuides

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of layout guide objects owned by this view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var layoutGuides: [NSLayoutGuide] { get }
```

```objc
@property (copy, readonly) NSArray<NSLayoutGuide *> * layoutGuides;
```

## See Also

### Managing Layout Guides
- [func addLayoutGuide(NSLayoutGuide)](./addlayoutguide%28_%29.md)
  Adds the provided layout guide to the view.
- [func removeLayoutGuide(NSLayoutGuide)](./removelayoutguide%28_%29.md)
  Removes the provided layout guide from the view.
- [var layoutMarginsGuide: NSLayoutGuide](./layoutmarginsguide.md)
  A layout guide that provides the recommended amount of padding for content inside of a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layoutguides)*