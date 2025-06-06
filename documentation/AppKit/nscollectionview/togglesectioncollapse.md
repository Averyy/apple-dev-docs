# toggleSectionCollapse(_:)

**Framework**: AppKit  
**Kind**: method

Collapses the section in which the sender resides into a single horizontally scrollable row.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@IBAction
@MainActor func toggleSectionCollapse(_ sender: Any)
```

#### Discussion

The icon view in Finder offers this type of collapsible section behavior when users choose the Show Less and Show More buttons. To enable this behavior, your header view must conform to the `NSCollectionViewSectionHeaderView` protocol, because the collection view uses the `sectionCollapseButton` property to identify the button that controls the collapse action.

## Parameters

- `sender`: The object that requested the action.

## See Also

- [func insertSections(IndexSet)](nscollectionview/insertsections(_:).md)
  Inserts new sections at the specified indexes.
- [func moveSection(Int, toSection: Int)](nscollectionview/movesection(_:tosection:).md)
  Moves a section from its current location to a new location.
- [func deleteSections(IndexSet)](nscollectionview/deletesections(_:).md)
  Deletes the specified sections and their contained items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/togglesectioncollapse(_:))*