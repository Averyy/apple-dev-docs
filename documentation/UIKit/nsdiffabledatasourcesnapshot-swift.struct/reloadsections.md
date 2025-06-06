# reloadSections(_:)

**Framework**: UIKit  
**Kind**: method

Reloads the data within the specified sections of the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
mutating func reloadSections(_ identifiers: [SectionIdentifierType])
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the sections to reload in the snapshot.

## See Also

- [func reconfigureItems([ItemIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(_:).md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [func reloadItems([ItemIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/reloaditems(_:).md)
  Reloads the data within the specified items in the snapshot.
- [var reloadedItemIdentifiers: [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [var reloadedSectionIdentifiers: [SectionIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloadsections(_:))*