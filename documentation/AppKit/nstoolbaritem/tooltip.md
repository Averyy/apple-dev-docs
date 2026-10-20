# toolTip

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tooltip to display when someone hovers over the item in the toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var toolTip: String? { get set }
```

```objc
@property (copy, nullable) NSString * toolTip;
```

## See Also

### Describing the item
- [var possibleLabels: Set<String>](./possiblelabels.md)
  The set of labels that the item might display.
- [var label: String](./label.md)
  The label that appears for this item in the toolbar.
- [var paletteLabel: String](./palettelabel.md)
  The label that appears when the toolbar item is in the customization palette.
- [var title: String](./title.md)
  The title of the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/tooltip)*