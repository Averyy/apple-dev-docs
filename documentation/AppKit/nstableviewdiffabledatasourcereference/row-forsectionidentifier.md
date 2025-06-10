# row(forSectionIdentifier:)

**Framework**: AppKit  
**Kind**: method

Returns a row for the section with the specified identifier in the table view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func row(forSectionIdentifier identifier: SectionIdentifierType) -> Int
```

#### Return Value

The item’s section, or `nil` if the method doesn’t find an item with the provided item identifier.

## Parameters

- `identifier`: The identifier of the section in the table view.

## See Also

- [func itemIdentifier(forRow: Int) -> ItemIdentifierType?](nstableviewdiffabledatasourcereference/itemidentifier(forrow:).md)
  Returns an identifier for the item at the specified row in the table view.
- [func row(forItemIdentifier: ItemIdentifierType) -> Int](nstableviewdiffabledatasourcereference/row(foritemidentifier:).md)
  Returns a row for the item with the specified identifier in the table view.
- [func sectionIdentifier(forRow: Int) -> SectionIdentifierType?](nstableviewdiffabledatasourcereference/sectionidentifier(forrow:).md)
  Returns the identifier of the section containing the specified row in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/row(forsectionidentifier:))*