# itemIdentifiersInSection(withIdentifier:)

**Framework**: AppKit  
**Kind**: method

Returns the identifiers of all of the items in the specified section of the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func itemIdentifiersInSection(withIdentifier sectionIdentifier: Any) -> [Any]
```

#### Return Value

An array of identifiers of the items contained in the section.

## Parameters

- `sectionIdentifier`: The identifier of the section of the snapshot.

## See Also

- [var itemIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [var sectionIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func index(ofItemIdentifier: Any) -> Int](nsdiffabledatasourcesnapshotreference/index(ofitemidentifier:).md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func index(ofSectionIdentifier: Any) -> Int](nsdiffabledatasourcesnapshotreference/index(ofsectionidentifier:).md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func sectionIdentifier(forSectionContainingItemIdentifier: Any) -> Any?](nsdiffabledatasourcesnapshotreference/sectionidentifier(forsectioncontainingitemidentifier:).md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/itemidentifiersinsection(withidentifier:))*