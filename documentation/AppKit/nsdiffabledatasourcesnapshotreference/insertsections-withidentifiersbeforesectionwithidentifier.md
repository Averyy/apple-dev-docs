# insertSections(withIdentifiers:beforeSectionWithIdentifier:)

**Framework**: AppKit  
**Kind**: method

Inserts the provided sections immediately before the section with the specified identifier in the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func insertSections(withIdentifiers sectionIdentifiers: [Any], beforeSectionWithIdentifier toSectionIdentifier: Any)
```

## Parameters

- `sectionIdentifiers`: The array of identifiers corresponding to the sections to add to the snapshot.
- `toSectionIdentifier`: The identifier of the section before which to insert the new sections.

## See Also

- [func insertItems(withIdentifiers: [Any], afterItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:afteritemwithidentifier:).md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertItems(withIdentifiers: [Any], beforeItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:beforeitemwithidentifier:).md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], afterSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:aftersectionwithidentifier:).md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:beforesectionwithidentifier:))*