# updateAction

**Framework**: AppKit  
**Kind**: property

The action being performed on the item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var updateAction: NSCollectionView.UpdateAction { get }
```

#### Discussion

For a list of relevant actions, see [`NSCollectionView.UpdateAction`](nscollectionview/updateaction.md).

## See Also

- [var indexPathBeforeUpdate: IndexPath?](nscollectionviewupdateitem/indexpathbeforeupdate.md)
  The index path of the item before the update.
- [var indexPathAfterUpdate: IndexPath?](nscollectionviewupdateitem/indexpathafterupdate.md)
  The index path of the item after the update.
- [NSCollectionView.UpdateAction](nscollectionview/updateaction.md)
  Constants indicating the type of action being performed on an item.
- [NSCollectionView.ScrollDirection](nscollectionview/scrolldirection.md)
  Constants indicating the scrolling direction for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewupdateitem/updateaction)*