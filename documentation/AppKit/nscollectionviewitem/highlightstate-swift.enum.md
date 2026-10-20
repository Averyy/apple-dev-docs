# NSCollectionViewItem.HighlightState

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the type of highlight applied to an item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum HighlightState
```

```c
enum NSCollectionViewItemHighlightState : NSInteger;
```

## Topics

### Constants
- [NSCollectionViewItem.HighlightState.none](./highlightstate-swift.enum/none.md)
  No highlight state.
- [NSCollectionViewItem.HighlightState.forSelection](./highlightstate-swift.enum/forselection.md)
  The selected highlight state. This type of highlight is applied when an item is selected. During interactive highlighting, this state is also applied to indicate that the item will become highlighted.
- [NSCollectionViewItem.HighlightState.forDeselection](./highlightstate-swift.enum/fordeselection.md)
  The deselection highlight state. During interactive selection, this state is used to indicate that the item will become deselected when interactions end. After interactions end, the highlight state returns to [`NSCollectionViewItem.HighlightState.none`](./highlightstate-swift.enum/none.md).
- [NSCollectionViewItem.HighlightState.asDropTarget](./highlightstate-swift.enum/asdroptarget.md)
  The drop target highlight state. This type of highlight is applied when the item is the target of a drop operation on the collection view. After the drop operation completes, the highlight state returns to [`NSCollectionViewItem.HighlightState.none`](./highlightstate-swift.enum/none.md).
### Initializers
- [init?(rawValue: Int)](./highlightstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/highlightstate-swift.enum)*