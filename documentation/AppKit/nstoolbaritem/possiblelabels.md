# possibleLabels

**Framework**: AppKit  
**Kind**: property

The set of labels that the item might display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
@MainActor
var possibleLabels: Set<String> { get set }
```

#### Discussion

Use this property to specify all of the labels you might possibly use for the toolbar item. Specify all strings in the current locale. To ensure there’s space for the longest label, the item sizes itself using the strings you provide.

## See Also

- [var label: String](nstoolbaritem/label.md)
  The label that appears for this item in the toolbar.
- [var paletteLabel: String](nstoolbaritem/palettelabel.md)
  The label that appears when the toolbar item is in the customization palette.
- [var title: String](nstoolbaritem/title.md)
  The title of the toolbar item.
- [var toolTip: String?](nstoolbaritem/tooltip.md)
  The tooltip to display when someone hovers over the item in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/possiblelabels)*