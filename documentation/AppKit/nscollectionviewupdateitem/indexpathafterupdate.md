# indexPathAfterUpdate

**Framework**: AppKit  
**Kind**: property

The index path of the item after the update.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var indexPathAfterUpdate: IndexPath? { get }
```

#### Discussion

The value of this property is `nil` for an action of type [`NSCollectionView.UpdateAction.delete`](nscollectionview/updateaction/delete.md).

## See Also

- [var indexPathBeforeUpdate: IndexPath?](nscollectionviewupdateitem/indexpathbeforeupdate.md)
  The index path of the item before the update.
- [var updateAction: NSCollectionView.UpdateAction](nscollectionviewupdateitem/updateaction.md)
  The action being performed on the item.
- [NSCollectionView.UpdateAction](nscollectionview/updateaction.md)
  Constants indicating the type of action being performed on an item.
- [NSCollectionView.ScrollDirection](nscollectionview/scrolldirection.md)
  Constants indicating the scrolling direction for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewupdateitem/indexpathafterupdate)*