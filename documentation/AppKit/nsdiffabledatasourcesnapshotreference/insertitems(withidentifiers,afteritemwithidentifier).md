# insertItems(withIdentifiers:afterItemWithIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts the provided items immediately after the item with the specified identifier in the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func insertItems(withIdentifiers identifiers: [Any], afterItemWithIdentifier itemIdentifier: Any)
```

```objc
- (void) insertItemsWithIdentifiers:(NSArray<id> *) identifiers afterItemWithIdentifier:(ItemIdentifierType) itemIdentifier;
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to add to the snapshot.
- `itemIdentifier`: The identifier of the item after which to insert the new items.

## See Also

### Inserting items and sections
- [func insertItems(withIdentifiers: [Any], beforeItemWithIdentifier: Any)](./insertitems%28withidentifiers,beforeitemwithidentifier%29.md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], afterSectionWithIdentifier: Any)](./insertsections%28withidentifiers,aftersectionwithidentifier%29.md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], beforeSectionWithIdentifier: Any)](./insertsections%28withidentifiers,beforesectionwithidentifier%29.md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:afteritemwithidentifier:))*