# sectionIdentifier(forSectionContainingItemIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the identifier of the section containing the specified item in the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func sectionIdentifier(forSectionContainingItemIdentifier itemIdentifier: Any) -> Any?
```

```objc
- (SectionIdentifierType) sectionIdentifierForSectionContainingItemIdentifier:(ItemIdentifierType) itemIdentifier;
```

## Return Value

The identifier of the section containing the specified item, or `nil` if the specified item doesn’t exist in any section of the snapshot.

## Parameters

- `itemIdentifier`: The identifier of the item contained in the section of the snapshot.

## See Also

### Identifying items and sections
- [var itemIdentifiers: [Any]](./itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [var sectionIdentifiers: [Any]](./sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func index(ofItemIdentifier: Any) -> Int](./index%28ofitemidentifier%29.md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func index(ofSectionIdentifier: Any) -> Int](./index%28ofsectionidentifier%29.md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiersInSection(withIdentifier: Any) -> [Any]](./itemidentifiersinsection%28withidentifier%29.md)
  Returns the identifiers of all of the items in the specified section of the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/sectionidentifier(forsectioncontainingitemidentifier:))*