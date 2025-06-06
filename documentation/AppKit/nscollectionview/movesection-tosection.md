# moveSection(_:toSection:)

**Framework**: AppKit  
**Kind**: method

Moves a section from its current location to a new location.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func moveSection(_ section: Int, toSection newSection: Int)
```

#### Discussion

Use this method to reorganize sections and their contained items. Always update your data source object before calling this method. Calling this method kicks off an update (and possible animations) to move the specified section to its new location. Specifically, the collection view asks the layout object for any updated layout attributes related to the new sections or any existing sections. If the layout attributes of any visible items changed, those changes are animated into place.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](nscollectionview/performbatchupdates(_:completionhandler:).md) method.

## Parameters

- `section`: The index of the section that you want to move.
- `newSection`: The new index at which to insert the section.

## See Also

- [func insertSections(IndexSet)](nscollectionview/insertsections(_:).md)
  Inserts new sections at the specified indexes.
- [func deleteSections(IndexSet)](nscollectionview/deletesections(_:).md)
  Deletes the specified sections and their contained items.
- [func toggleSectionCollapse(Any)](nscollectionview/togglesectioncollapse(_:).md)
  Collapses the section in which the sender resides into a single horizontally scrollable row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/movesection(_:tosection:))*