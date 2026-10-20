# NSCollectionViewItem.HighlightState.forDeselection

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The deselection highlight state. During interactive selection, this state is used to indicate that the item will become deselected when interactions end. After interactions end, the highlight state returns to [`NSCollectionViewItem.HighlightState.none`](./none.md).

**Availability**:
- macOS 10.11+

## Declaration

```swift
case forDeselection
```

```c
NSCollectionViewItemHighlightForDeselection
```

## See Also

### Constants
- [NSCollectionViewItem.HighlightState.none](./none.md)
  No highlight state.
- [NSCollectionViewItem.HighlightState.forSelection](./forselection.md)
  The selected highlight state. This type of highlight is applied when an item is selected. During interactive highlighting, this state is also applied to indicate that the item will become highlighted.
- [NSCollectionViewItem.HighlightState.asDropTarget](./asdroptarget.md)
  The drop target highlight state. This type of highlight is applied when the item is the target of a drop operation on the collection view. After the drop operation completes, the highlight state returns to [`NSCollectionViewItem.HighlightState.none`](./none.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/highlightstate-swift.enum/fordeselection)*