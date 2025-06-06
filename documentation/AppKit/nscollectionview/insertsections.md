# insertSections(_:)

**Framework**: AppKit  
**Kind**: method

Inserts new sections at the specified indexes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func insertSections(_ sections: IndexSet)
```

#### Discussion

This method tells the collection view to insert the specified sections and update itself. Always update your data source object before calling this method. Calling this method kicks off an update (and possible animations) to add the new sections. Specifically, the collection view asks the layout object for any updated layout attributes related to the new sections or any existing sections. If the layout attributes of any visible items changed, those changes are animated into place.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](nscollectionview/performbatchupdates(_:completionhandler:).md) method.

## Parameters

- `sections`: An index set containing the indexes at which you want to insert new sections. This parameter must not be  .

## See Also

- [func moveSection(Int, toSection: Int)](nscollectionview/movesection(_:tosection:).md)
  Moves a section from its current location to a new location.
- [func deleteSections(IndexSet)](nscollectionview/deletesections(_:).md)
  Deletes the specified sections and their contained items.
- [func toggleSectionCollapse(Any)](nscollectionview/togglesectioncollapse(_:).md)
  Collapses the section in which the sender resides into a single horizontally scrollable row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/insertsections(_:))*