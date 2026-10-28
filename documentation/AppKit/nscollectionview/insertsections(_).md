# insertSections(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts new sections at the specified indexes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func insertSections(_ sections: IndexSet)
```

```objc
- (void) insertSections:(NSIndexSet *) sections;
```

## Discussion

This method tells the collection view to insert the specified sections and update itself. Always update your data source object before calling this method. Calling this method kicks off an update (and possible animations) to add the new sections. Specifically, the collection view asks the layout object for any updated layout attributes related to the new sections or any existing sections. If the layout attributes of any visible items changed, those changes are animated into place.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](./performbatchupdates%28_,completionhandler%29.md) method.

## Parameters

- `sections`: An index set containing the indexes at which you want to insert new sections. This parameter must not be `nil`.

## See Also

### Inserting, Moving, Deleting, and Collapsing Sections
- [func moveSection(Int, toSection: Int)](./movesection%28_,tosection%29.md)
  Moves a section from its current location to a new location.
- [func deleteSections(IndexSet)](./deletesections%28_%29.md)
  Deletes the specified sections and their contained items.
- [func toggleSectionCollapse(Any)](./togglesectioncollapse%28_%29.md)
  Collapses the section in which the sender resides into a single horizontally scrollable row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/insertsections(_:))*