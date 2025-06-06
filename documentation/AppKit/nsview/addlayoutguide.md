# addLayoutGuide(_:)

**Framework**: AppKit  
**Kind**: method

Adds the provided layout guide to the view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func addLayoutGuide(_ guide: NSLayoutGuide)
```

#### Discussion

This method adds the provided layout guide to the end of the view’s [`layoutGuides`](nsview/layoutguides.md) array. It also assigns the view to the guide’s [`owningView`](nslayoutguide/owningview.md) property. Each guide can have only one owning view.

After the guide has been added to a view, it can participate in Auto Layout constraints with that view’s hierarchy.

## Parameters

- `guide`: The layout guide to be added.

## See Also

- [func removeLayoutGuide(NSLayoutGuide)](nsview/removelayoutguide(_:).md)
  Removes the provided layout guide from the view.
- [var layoutGuides: [NSLayoutGuide]](nsview/layoutguides.md)
  The array of layout guide objects owned by this view.
- [var layoutMarginsGuide: NSLayoutGuide](nsview/layoutmarginsguide.md)
  A layout guide that provides the recommended amount of padding for content inside of a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addlayoutguide(_:))*