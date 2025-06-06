# deleteSections(_:)

**Framework**: AppKit  
**Kind**: method

Deletes the specified sections and their contained items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func deleteSections(_ sections: IndexSet)
```

#### Discussion

Use this method to delete entire sections and their contained items. Always update your data source object before calling this method. Calling this method kicks off an update (and possible animations) to delete the specified sections. Specifically, the collection view asks the layout object for the final layout attributes for any deleted sections and may also ask for updated layout attributes for any remaining sections. If the layout attributes of any visible items changed, those changes are animated into place.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](nscollectionview/performbatchupdates(_:completionhandler:).md) method.

## Parameters

- `sections`: An index set containing the indexes of the sections that you want to delete. This parameter must not be  .

## See Also

- [func insertSections(IndexSet)](nscollectionview/insertsections(_:).md)
  Inserts new sections at the specified indexes.
- [func moveSection(Int, toSection: Int)](nscollectionview/movesection(_:tosection:).md)
  Moves a section from its current location to a new location.
- [func toggleSectionCollapse(Any)](nscollectionview/togglesectioncollapse(_:).md)
  Collapses the section in which the sender resides into a single horizontally scrollable row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/deletesections(_:))*