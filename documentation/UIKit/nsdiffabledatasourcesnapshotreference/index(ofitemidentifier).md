# index(ofItemIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the item in the snapshot with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func index(ofItemIdentifier itemIdentifier: Any) -> Int
```

```objc
- (NSInteger) indexOfItemIdentifier:(ItemIdentifierType) itemIdentifier;
```

## Return Value

The index of the item in the snapshot, or `NSNotFound` if the item with the specified identifier doesn’t exist in the snapshot. This index value is 0-based.

## Parameters

- `itemIdentifier`: The identifier of the item in the snapshot.

## See Also

### Identifying items and sections
- [var itemIdentifiers: [Any]](./itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [var sectionIdentifiers: [Any]](./sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func index(ofSectionIdentifier: Any) -> Int](./index%28ofsectionidentifier%29.md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiersInSection(withIdentifier: Any) -> [Any]](./itemidentifiersinsection%28withidentifier%29.md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(forSectionContainingItemIdentifier: Any) -> Any?](./sectionidentifier%28forsectioncontainingitemidentifier%29.md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/index(ofitemidentifier:))*