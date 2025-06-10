# insertSections(withIdentifiers:afterSectionWithIdentifier:)

**Framework**: UIKit  
**Kind**: method

Inserts the provided sections immediately after the section with the specified identifier in the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func insertSections(withIdentifiers sectionIdentifiers: [Any], afterSectionWithIdentifier toSectionIdentifier: Any)
```

## Parameters

- `sectionIdentifiers`: The array of identifiers corresponding to the sections to add to the snapshot.
- `toSectionIdentifier`: The identifier of the section after which to insert the new sections.

## See Also

- [func insertItems(withIdentifiers: [Any], afterItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:afteritemwithidentifier:).md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertItems(withIdentifiers: [Any], beforeItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:beforeitemwithidentifier:).md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], beforeSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:beforesectionwithidentifier:).md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:aftersectionwithidentifier:))*