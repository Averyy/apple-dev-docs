# reloadItems(withIdentifiers:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the data within the specified items in the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func reloadItems(withIdentifiers identifiers: [Any])
```

```objc
- (void) reloadItemsWithIdentifiers:(NSArray<id> *) identifiers;
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to reload in the snapshot.

## See Also

### Reloading data
- [func reconfigureItems(withIdentifiers: [Any])](./reconfigureitems%28withidentifiers%29.md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [Any]](./reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [var reloadedItemIdentifiers: [Any]](./reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [func reloadSections(withIdentifiers: [Any])](./reloadsections%28withidentifiers%29.md)
  Reloads the data within the specified sections of the snapshot.
- [var reloadedSectionIdentifiers: [Any]](./reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/reloaditems(withidentifiers:))*