# NSCollectionViewItem.HighlightState

**Framework**: AppKit  
**Kind**: enum

Constants indicating the type of highlight applied to an item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum HighlightState
```

## Topics

### Constants
- [NSCollectionViewItem.HighlightState.none](nscollectionviewitem/highlightstate-swift.enum/none.md)
  No highlight state.
- [NSCollectionViewItem.HighlightState.forSelection](nscollectionviewitem/highlightstate-swift.enum/forselection.md)
  The selected highlight state. This type of highlight is applied when an item is selected. During interactive highlighting, this state is also applied to indicate that the item will become highlighted.
- [NSCollectionViewItem.HighlightState.forDeselection](nscollectionviewitem/highlightstate-swift.enum/fordeselection.md)
  The deselection highlight state. During interactive selection, this state is used to indicate that the item will become deselected when interactions end. After interactions end, the highlight state returns to [`NSCollectionViewItem.HighlightState.none`](nscollectionviewitem/highlightstate-swift.enum/none.md).
- [NSCollectionViewItem.HighlightState.asDropTarget](nscollectionviewitem/highlightstate-swift.enum/asdroptarget.md)
  The drop target highlight state. This type of highlight is applied when the item is the target of a drop operation on the collection view. After the drop operation completes, the highlight state returns to [`NSCollectionViewItem.HighlightState.none`](nscollectionviewitem/highlightstate-swift.enum/none.md).
### Initializers
- [init?(rawValue: Int)](nscollectionviewitem/highlightstate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/highlightstate-swift.enum)*