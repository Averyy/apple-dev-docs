# reloadItems(at:)

**Framework**: AppKit  
**Kind**: method

Reloads only the specified items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func reloadItems(at indexPaths: Set<IndexPath>)
```

#### Discussion

Call this method to update specific items in your collection view. You call this method when the underlying data for those items changes and you want to update the visual appearance of those items. When you call this method, the collection view discards the specified items and asks your data source to provide new ones. For efficiency, the collection view requests only the items that are visible.

## Parameters

- `indexPaths`: The index paths of the specific items that you want to reload. Specifying   for this parameter raises an exception.

## See Also

- [func reloadData()](nscollectionview/reloaddata.md)
  Reloads all of the data for the collection view.
- [func reloadSections(IndexSet)](nscollectionview/reloadsections(_:).md)
  Reloads the data in the specified sections of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/reloaditems(at:))*