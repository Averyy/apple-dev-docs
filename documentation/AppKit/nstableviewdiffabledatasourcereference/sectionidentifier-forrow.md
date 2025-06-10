# sectionIdentifier(forRow:)

**Framework**: AppKit  
**Kind**: method

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

- [func itemIdentifier(forRow: Int) -> ItemIdentifierType?](nstableviewdiffabledatasourcereference/itemidentifier(forrow:).md)
  Returns an identifier for the item at the specified row in the table view.
- [func row(forItemIdentifier: ItemIdentifierType) -> Int](nstableviewdiffabledatasourcereference/row(foritemidentifier:).md)
  Returns a row for the item with the specified identifier in the table view.
- [func row(forSectionIdentifier: SectionIdentifierType) -> Int](nstableviewdiffabledatasourcereference/row(forsectionidentifier:).md)
  Returns a row for the section with the specified identifier in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/sectionidentifier(forrow:))*