# reloadSections(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the data within the specified sections of the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS

## Declaration

```swift
mutating func reloadSections(_ identifiers: [SectionIdentifierType])
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the sections to reload in the snapshot.

## See Also

### Reloading data
- [func reconfigureItems([ItemIdentifierType])](./reconfigureitems%28_%29.md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [ItemIdentifierType]](./reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [func reloadItems([ItemIdentifierType])](./reloaditems%28_%29.md)
  Reloads the data within the specified items in the snapshot.
- [var reloadedItemIdentifiers: [ItemIdentifierType]](./reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [var reloadedSectionIdentifiers: [SectionIdentifierType]](./reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloadsections(_:))*