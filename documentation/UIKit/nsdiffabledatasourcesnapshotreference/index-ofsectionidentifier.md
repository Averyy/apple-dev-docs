# index(ofSectionIdentifier:)

**Framework**: UIKit  
**Kind**: method

Returns the index of the section of the snapshot with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func index(ofSectionIdentifier sectionIdentifier: Any) -> Int
```

#### Return Value

The index of the section of the snapshot, or `NSNotFound` if the section with the specified identifier doesn’t exist in the snapshot. This index value is 0-based.

## Parameters

- `sectionIdentifier`: The identifier of the section of the snapshot.

## See Also

- [var itemIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [var sectionIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func index(ofItemIdentifier: Any) -> Int](nsdiffabledatasourcesnapshotreference/index(ofitemidentifier:).md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func itemIdentifiersInSection(withIdentifier: Any) -> [Any]](nsdiffabledatasourcesnapshotreference/itemidentifiersinsection(withidentifier:).md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(forSectionContainingItemIdentifier: Any) -> Any?](nsdiffabledatasourcesnapshotreference/sectionidentifier(forsectioncontainingitemidentifier:).md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/index(ofsectionidentifier:))*