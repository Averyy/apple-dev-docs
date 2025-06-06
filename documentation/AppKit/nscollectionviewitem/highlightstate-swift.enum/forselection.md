# NSCollectionViewItem.HighlightState.forSelection

**Framework**: AppKit  
**Kind**: case

The selected highlight state. This type of highlight is applied when an item is selected. During interactive highlighting, this state is also applied to indicate that the item will become highlighted.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case forSelection
```

## See Also

- [NSCollectionViewItem.HighlightState.none](nscollectionviewitem/highlightstate-swift.enum/none.md)
  No highlight state.
- [NSCollectionViewItem.HighlightState.forDeselection](nscollectionviewitem/highlightstate-swift.enum/fordeselection.md)
  The deselection highlight state. During interactive selection, this state is used to indicate that the item will become deselected when interactions end. After interactions end, the highlight state returns to [`NSCollectionViewItem.HighlightState.none`](nscollectionviewitem/highlightstate-swift.enum/none.md).
- [NSCollectionViewItem.HighlightState.asDropTarget](nscollectionviewitem/highlightstate-swift.enum/asdroptarget.md)
  The drop target highlight state. This type of highlight is applied when the item is the target of a drop operation on the collection view. After the drop operation completes, the highlight state returns to [`NSCollectionViewItem.HighlightState.none`](nscollectionviewitem/highlightstate-swift.enum/none.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/highlightstate-swift.enum/forselection)*