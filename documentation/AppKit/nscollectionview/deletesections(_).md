# deleteSections(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deletes the specified sections and their contained items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func deleteSections(_ sections: IndexSet)
```

```objc
- (void) deleteSections:(NSIndexSet *) sections;
```

#### Discussion

Use this method to delete entire sections and their contained items. Always update your data source object before calling this method. Calling this method kicks off an update (and possible animations) to delete the specified sections. Specifically, the collection view asks the layout object for the final layout attributes for any deleted sections and may also ask for updated layout attributes for any remaining sections. If the layout attributes of any visible items changed, those changes are animated into place.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](./performbatchupdates%28_,completionhandler%29.md) method.

## Parameters

- `sections`: An index set containing the indexes of the sections that you want to delete. This parameter must not be `nil`.

## See Also

### Inserting, Moving, Deleting, and Collapsing Sections
- [func insertSections(IndexSet)](./insertsections%28_%29.md)
  Inserts new sections at the specified indexes.
- [func moveSection(Int, toSection: Int)](./movesection%28_,tosection%29.md)
  Moves a section from its current location to a new location.
- [func toggleSectionCollapse(Any)](./togglesectioncollapse%28_%29.md)
  Collapses the section in which the sender resides into a single horizontally scrollable row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/deletesections(_:))*