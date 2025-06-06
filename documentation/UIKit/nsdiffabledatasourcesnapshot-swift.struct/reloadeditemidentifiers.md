# reloadedItemIdentifiers

**Framework**: UIKit  
**Kind**: property

Identifies the items reloaded by the changes to the snapshot.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var reloadedItemIdentifiers: [ItemIdentifierType] { get }
```

#### Discussion

After you make updates to the snapshot, this method returns an array of identifiers corresponding to the items that the view reloads when you apply the snapshot to your data source.

## See Also

- [func reconfigureItems([ItemIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(_:).md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [func reloadItems([ItemIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/reloaditems(_:).md)
  Reloads the data within the specified items in the snapshot.
- [func reloadSections([SectionIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/reloadsections(_:).md)
  Reloads the data within the specified sections of the snapshot.
- [var reloadedSectionIdentifiers: [SectionIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloadeditemidentifiers)*