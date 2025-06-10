# insertItems(withIdentifiers:afterItemWithIdentifier:)

**Framework**: AppKit  
**Kind**: method

Inserts the provided items immediately after the item with the specified identifier in the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func insertItems(withIdentifiers identifiers: [Any], afterItemWithIdentifier itemIdentifier: Any)
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to add to the snapshot.
- `itemIdentifier`: The identifier of the item after which to insert the new items.

## See Also

- [func insertItems(withIdentifiers: [Any], beforeItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:beforeitemwithidentifier:).md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], afterSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:aftersectionwithidentifier:).md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], beforeSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:beforesectionwithidentifier:).md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:afteritemwithidentifier:))*