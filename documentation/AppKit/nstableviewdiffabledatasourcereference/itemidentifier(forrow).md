# itemIdentifier(forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an identifier for the item at the specified row in the table view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func itemIdentifier(forRow row: Int) -> ItemIdentifierType?
```

```objc
- (ItemIdentifierType) itemIdentifierForRow:(NSInteger) row;
```

## Return Value

The item’s identifier, or `nil` if the method doesn’t find an item at the provided row.

## Parameters

- `row`: The row of the item in the table view.

## See Also

### Identifying Items and Sections
- [func row(forItemIdentifier: ItemIdentifierType) -> Int](./row%28foritemidentifier%29.md)
  Returns a row for the item with the specified identifier in the table view.
- [func sectionIdentifier(forRow: Int) -> SectionIdentifierType?](./sectionidentifier%28forrow%29.md)
  Returns the identifier of the section containing the specified row in the snapshot.
- [func row(forSectionIdentifier: SectionIdentifierType) -> Int](./row%28forsectionidentifier%29.md)
  Returns a row for the section with the specified identifier in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/itemidentifier(forrow:))*