# itemIdentifiers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The identifiers of all of the items in the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS

## Declaration

```swift
var itemIdentifiers: [ItemIdentifierType] { get }
```

## See Also

### Identifying items and sections
- [var sectionIdentifiers: [SectionIdentifierType]](./sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func indexOfItem(ItemIdentifierType) -> Int?](./indexofitem%28_%29.md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func indexOfSection(SectionIdentifierType) -> Int?](./indexofsection%28_%29.md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiers(inSection: SectionIdentifierType) -> [ItemIdentifierType]](./itemidentifiers%28insection%29.md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(containingItem: ItemIdentifierType) -> SectionIdentifierType?](./sectionidentifier%28containingitem%29.md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers)*