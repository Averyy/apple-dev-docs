# isSelected

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the item is currently selected.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isSelected: Bool { get set }
```

```objc
@property (getter=isSelected) BOOL selected;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the item is selected or [`false`](../../Swift/false.md) when it is not.

## See Also

### Managing the Selection and Highlight States
- [var highlightState: NSCollectionViewItem.HighlightState](./highlightstate-swift.property.md)
  The highlight state currently applied to the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/isselected)*