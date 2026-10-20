# sectionIdentifiers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The identifiers of all of the sections in the snapshot.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
var sectionIdentifiers: [SectionIdentifierType] { get }
```

## See Also

### Identifying Items and Sections
- [var itemIdentifiers: [ItemIdentifierType]](./itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [func indexOfItem(ItemIdentifierType) -> Int?](./indexofitem%28_%29.md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func indexOfSection(SectionIdentifierType) -> Int?](./indexofsection%28_%29.md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiers(inSection: SectionIdentifierType) -> [ItemIdentifierType]](./itemidentifiers%28insection%29.md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(containingItem: ItemIdentifierType) -> SectionIdentifierType?](./sectionidentifier%28containingitem%29.md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/sectionidentifiers)*