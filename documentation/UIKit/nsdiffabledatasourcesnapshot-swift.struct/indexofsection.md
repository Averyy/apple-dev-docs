# indexOfSection(_:)

**Framework**: UIKit  
**Kind**: method

Returns the index of the section of the snapshot with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func indexOfSection(_ identifier: SectionIdentifierType) -> Int?
```

#### Return Value

The index of the section of the snapshot, or `nil` if the section with the specified identifier doesn’t exist in the snapshot. This index value is 0-based.

## Parameters

- `identifier`: The identifier of the section of the snapshot.

## See Also

- [var itemIdentifiers: [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [var sectionIdentifiers: [SectionIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func indexOfItem(ItemIdentifierType) -> Int?](nsdiffabledatasourcesnapshot-swift.struct/indexofitem(_:).md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func itemIdentifiers(inSection: SectionIdentifierType) -> [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers(insection:).md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(containingItem: ItemIdentifierType) -> SectionIdentifierType?](nsdiffabledatasourcesnapshot-swift.struct/sectionidentifier(containingitem:).md)
  Returns the identifier of the section containing the specified item in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/indexofsection(_:))*