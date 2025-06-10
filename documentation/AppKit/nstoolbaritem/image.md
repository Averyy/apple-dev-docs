# image

**Framework**: AppKit  
**Kind**: property

The image to display for the toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var image: NSImage? { get set }
```

#### Discussion

If you assign a custom view to the toolbar item, modifying this property updates the `image` property of the view, if one exists. If the item doesn’t contain a custom view, the toolbar item manages the image content directly.

## See Also

- [var backgroundTintColor: UIColor?](nstoolbaritem/backgroundtintcolor.md)
- [var view: NSView?](nstoolbaritem/view.md)
  The custom view you use to draw the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/image)*