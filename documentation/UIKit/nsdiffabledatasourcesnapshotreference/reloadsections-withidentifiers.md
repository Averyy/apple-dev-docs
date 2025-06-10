# reloadSections(withIdentifiers:)

**Framework**: UIKit  
**Kind**: method

Reloads the data within the specified sections of the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func reloadSections(withIdentifiers sectionIdentifiers: [Any])
```

## Parameters

- `sectionIdentifiers`: The array of identifiers corresponding to the sections to reload in the snapshot.

## See Also

- [func reconfigureItems(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers:).md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [func reloadItems(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/reloaditems(withidentifiers:).md)
  Reloads the data within the specified items in the snapshot.
- [var reloadedItemIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [var reloadedSectionIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/reloadsections(withidentifiers:))*