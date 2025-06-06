# highlightState

**Framework**: AppKit  
**Kind**: property

The highlight state currently applied to the item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var highlightState: NSCollectionViewItem.HighlightState { get set }
```

#### Discussion

The highlight state provides a visual indication of operations happening to items in the collection view. The highlight state normally toggles between the [`NSCollectionViewItem.HighlightState.none`](nscollectionviewitem/highlightstate-swift.enum/none.md) and [`NSCollectionViewItem.HighlightState.forSelection`](nscollectionviewitem/highlightstate-swift.enum/forselection.md) states, but other states may be applied to indicate transient conditions. For example, the [`NSCollectionViewItem.HighlightState.forDeselection`](nscollectionviewitem/highlightstate-swift.enum/fordeselection.md) state is applied during interactive selections when a currently selected item is about to be deselected.

## See Also

- [var isSelected: Bool](nscollectionviewitem/isselected.md)
  A Boolean indicating whether the item is currently selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/highlightstate-swift.property)*