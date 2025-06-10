# view

**Framework**: AppKit  
**Kind**: property

The custom view you use to draw the toolbar item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var view: NSView? { get set }
```

#### Discussion

Many properties of [`NSToolbarItem`](nstoolbaritem.md) automatically forward changes to the associated custom [`NSView`](nsview.md) object, if the view has a property or accessor method with a matching name.

## See Also

- [var image: UIImage?](nstoolbaritem/image.md)
  The image to display for the toolbar item.
- [var backgroundTintColor: UIColor?](nstoolbaritem/backgroundtintcolor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/view)*