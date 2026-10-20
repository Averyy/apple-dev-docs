# reloadItems(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the data within the specified items in the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS

## Declaration

```swift
mutating func reloadItems(_ identifiers: [ItemIdentifierType])
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to reload in the snapshot.

## See Also

### Reloading data
- [func reconfigureItems([ItemIdentifierType])](./reconfigureitems%28_%29.md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [ItemIdentifierType]](./reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [var reloadedItemIdentifiers: [ItemIdentifierType]](./reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [func reloadSections([SectionIdentifierType])](./reloadsections%28_%29.md)
  Reloads the data within the specified sections of the snapshot.
- [var reloadedSectionIdentifiers: [SectionIdentifierType]](./reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloaditems(_:))*