# sectionIdentifiers

**Framework**: AppKit  
**Kind**: property

The identifiers of all of the sections in the snapshot.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
var sectionIdentifiers: [SectionIdentifierType] { get }
```

## See Also

- [var itemIdentifiers: [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [func indexOfItem(ItemIdentifierType) -> Int?](nsdiffabledatasourcesnapshot-swift.struct/indexofitem(_:).md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func indexOfSection(SectionIdentifierType) -> Int?](nsdiffabledatasourcesnapshot-swift.struct/indexofsection(_:).md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiers(inSection: SectionIdentifierType) -> [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers(insection:).md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(containingItem: ItemIdentifierType) -> SectionIdentifierType?](nsdiffabledatasourcesnapshot-swift.struct/sectionidentifier(containingitem:).md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/sectionidentifiers)*