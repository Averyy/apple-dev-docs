# paletteLabel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The label that appears when the toolbar item is in the customization palette.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var paletteLabel: String { get set }
```

```objc
@property (copy) NSString * paletteLabel;
```

## Discussion

If you support toolbar customizations, you must provide palette labels for your items. In most cases, you can apply the same value to this property and the [`label`](./label.md) property. However, you might use this property to offer a more descriptive string, or to provide a label string when the [`label`](./label.md) property contains an empty string.

## See Also

### Describing the item
- [var possibleLabels: Set<String>](./possiblelabels.md)
  The set of labels that the item might display.
- [var label: String](./label.md)
  The label that appears for this item in the toolbar.
- [var title: String](./title.md)
  The title of the toolbar item.
- [var toolTip: String?](./tooltip.md)
  The tooltip to display when someone hovers over the item in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/palettelabel)*