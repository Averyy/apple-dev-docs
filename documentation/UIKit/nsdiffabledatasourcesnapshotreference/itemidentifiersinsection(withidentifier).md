# itemIdentifiersInSection(withIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the identifiers of all of the items in the specified section of the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func itemIdentifiersInSection(withIdentifier sectionIdentifier: Any) -> [Any]
```

```objc
- (NSArray<id> *) itemIdentifiersInSectionWithIdentifier:(SectionIdentifierType) sectionIdentifier;
```

## Return Value

An array of identifiers of the items contained in the section.

## Parameters

- `sectionIdentifier`: The identifier of the section of the snapshot.

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
- [func sectionIdentifier(forSectionContainingItemIdentifier: Any) -> Any?](./sectionidentifier%28forsectioncontainingitemidentifier%29.md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/itemidentifiersinsection(withidentifier:))*