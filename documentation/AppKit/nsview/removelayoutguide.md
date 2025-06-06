# removeLayoutGuide(_:)

**Framework**: AppKit  
**Kind**: method

Removes the provided layout guide from the view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func removeLayoutGuide(_ guide: NSLayoutGuide)
```

#### Discussion

This method removes the provided layout guide from the view’s [`layoutGuides`](nsview/layoutguides.md) array. It also sets the guide’s [`owningView`](nslayoutguide/owningview.md) property to `nil`. Finally, it removes any constraints to the layout guide.

Layout guides cannot participate in Auto Layout constraints unless they are added by a view in the view hierarchy.

## Parameters

- `guide`: The layout guide to be removed.

## See Also

- [func addLayoutGuide(NSLayoutGuide)](nsview/addlayoutguide(_:).md)
  Adds the provided layout guide to the view.
- [var layoutGuides: [NSLayoutGuide]](nsview/layoutguides.md)
  The array of layout guide objects owned by this view.
- [var layoutMarginsGuide: NSLayoutGuide](nsview/layoutmarginsguide.md)
  A layout guide that provides the recommended amount of padding for content inside of a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removelayoutguide(_:))*