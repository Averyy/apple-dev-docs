# reconfiguredItemIdentifiers

**Framework**: UIKit  
**Kind**: property

Identifies the items reconfigured by the changes to the snapshot.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var reconfiguredItemIdentifiers: [Any] { get }
```

#### Discussion

After you make updates to the snapshot, this method returns an array of identifiers corresponding to the items that the view reconfigures when you apply the snapshot to your data source.

## See Also

- [func reconfigureItems(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers:).md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [func reloadItems(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/reloaditems(withidentifiers:).md)
  Reloads the data within the specified items in the snapshot.
- [var reloadedItemIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [func reloadSections(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/reloadsections(withidentifiers:).md)
  Reloads the data within the specified sections of the snapshot.
- [var reloadedSectionIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/reconfigureditemidentifiers)*