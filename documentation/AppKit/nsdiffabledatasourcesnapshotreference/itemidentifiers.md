# itemIdentifiers

**Framework**: AppKit  
**Kind**: property

The identifiers of all of the items in the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var itemIdentifiers: [Any] { get }
```

## See Also

- [var sectionIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func index(ofItemIdentifier: Any) -> Int](nsdiffabledatasourcesnapshotreference/index(ofitemidentifier:).md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func index(ofSectionIdentifier: Any) -> Int](nsdiffabledatasourcesnapshotreference/index(ofsectionidentifier:).md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiersInSection(withIdentifier: Any) -> [Any]](nsdiffabledatasourcesnapshotreference/itemidentifiersinsection(withidentifier:).md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(forSectionContainingItemIdentifier: Any) -> Any?](nsdiffabledatasourcesnapshotreference/sectionidentifier(forsectioncontainingitemidentifier:).md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/itemidentifiers)*