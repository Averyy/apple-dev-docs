# reloadedItemIdentifiers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Identifies the items reloaded by the changes to the snapshot.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var reloadedItemIdentifiers: [Any] { get }
```

```objc
@property (nonatomic, readonly) NSArray<id> * reloadedItemIdentifiers;
```

## Discussion

After you make updates to the snapshot, this method returns an array of identifiers corresponding to the items that the view reloads when you apply the snapshot to your data source.

## See Also

### Reloading data
- [func reconfigureItems(withIdentifiers: [Any])](./reconfigureitems%28withidentifiers%29.md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [Any]](./reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [func reloadItems(withIdentifiers: [Any])](./reloaditems%28withidentifiers%29.md)
  Reloads the data within the specified items in the snapshot.
- [func reloadSections(withIdentifiers: [Any])](./reloadsections%28withidentifiers%29.md)
  Reloads the data within the specified sections of the snapshot.
- [var reloadedSectionIdentifiers: [Any]](./reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/reloadeditemidentifiers)*