# sectionIdentifier(forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the identifier of the section containing the specified row in the snapshot.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func sectionIdentifier(forRow row: Int) -> SectionIdentifierType?
```

#### Return Value

The section’s identifier, or `nil` if the method doesn’t find an item with the provided item identifier.

## Parameters

- `row`: The row of the section in the table view.

## See Also

### Identifying Items and Sections
- [func itemIdentifier(forRow: Int) -> ItemIdentifierType?](./itemidentifier%28forrow%29.md)
  Returns an identifier for the item at the specified row in the table view.
- [func row(forItemIdentifier: ItemIdentifierType) -> Int?](./row%28foritemidentifier%29.md)
  Returns a row for the item with the specified identifier in the table view.
- [func row(forSectionIdentifier: SectionIdentifierType) -> Int?](./row%28forsectionidentifier%29.md)
  Returns a row for the section with the specified identifier in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/sectionidentifier(forrow:))*