# title

**Framework**: AppKit  
**Kind**: property

The title of the toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
var title: String { get set }
```

#### Discussion

If you assign a custom view to the toolbar item, modifying this property updates the [`title`](nstoolbaritem/title.md) property of the view if one exists. If the toolbar item contains a button, modifying this property updates the button title. If the item doesn’t contain a custom view, the toolbar item manages the content directly.

> **Note**:  In macOS 12 and earlier, [`NSToolbarItem`](nstoolbaritem.md) doesn’t support custom views in Mac apps built with Mac Catalyst.

## See Also

- [var possibleLabels: Set<String>](nstoolbaritem/possiblelabels.md)
  The set of labels that the item might display.
- [var label: String](nstoolbaritem/label.md)
  The label that appears for this item in the toolbar.
- [var paletteLabel: String](nstoolbaritem/palettelabel.md)
  The label that appears when the toolbar item is in the customization palette.
- [var toolTip: String?](nstoolbaritem/tooltip.md)
  The tooltip to display when someone hovers over the item in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/title)*