# highlightState

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The highlight state currently applied to the item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var highlightState: NSCollectionViewItem.HighlightState { get set }
```

```objc
@property NSCollectionViewItemHighlightState highlightState;
```

#### Discussion

The highlight state provides a visual indication of operations happening to items in the collection view. The highlight state normally toggles between the [`NSCollectionViewItem.HighlightState.none`](./highlightstate-swift.enum/none.md) and [`NSCollectionViewItem.HighlightState.forSelection`](./highlightstate-swift.enum/forselection.md) states, but other states may be applied to indicate transient conditions. For example, the [`NSCollectionViewItem.HighlightState.forDeselection`](./highlightstate-swift.enum/fordeselection.md) state is applied during interactive selections when a currently selected item is about to be deselected.

## See Also

### Managing the Selection and Highlight States
- [var isSelected: Bool](./isselected.md)
  A Boolean indicating whether the item is currently selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/highlightstate-swift.property)*