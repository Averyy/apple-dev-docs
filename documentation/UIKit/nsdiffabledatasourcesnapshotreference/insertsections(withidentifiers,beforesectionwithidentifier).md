# insertSections(withIdentifiers:beforeSectionWithIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts the provided sections immediately before the section with the specified identifier in the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func insertSections(withIdentifiers sectionIdentifiers: [Any], beforeSectionWithIdentifier toSectionIdentifier: Any)
```

```objc
- (void) insertSectionsWithIdentifiers:(NSArray<id> *) sectionIdentifiers beforeSectionWithIdentifier:(SectionIdentifierType) toSectionIdentifier;
```

## Parameters

- `sectionIdentifiers`: The array of identifiers corresponding to the sections to add to the snapshot.
- `toSectionIdentifier`: The identifier of the section before which to insert the new sections.

## See Also

### Inserting items and sections
- [func insertItems(withIdentifiers: [Any], afterItemWithIdentifier: Any)](./insertitems%28withidentifiers,afteritemwithidentifier%29.md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertItems(withIdentifiers: [Any], beforeItemWithIdentifier: Any)](./insertitems%28withidentifiers,beforeitemwithidentifier%29.md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], afterSectionWithIdentifier: Any)](./insertsections%28withidentifiers,aftersectionwithidentifier%29.md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:beforesectionwithidentifier:))*