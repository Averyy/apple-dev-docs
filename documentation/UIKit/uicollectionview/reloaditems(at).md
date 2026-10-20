# reloadItems(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads just the items at the specified index paths.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func reloadItems(at indexPaths: [IndexPath])
```

```objc
- (void) reloadItemsAtIndexPaths:(NSArray<NSIndexPath *> *) indexPaths;
```

#### Discussion

Call this method to selectively reload only the specified items. This causes the collection view to discard any cells associated with those items and redisplay them.

## Parameters

- `indexPaths`: An array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects identifying the items you want to update.

## See Also

### Reloading content
- [var hasUncommittedUpdates: Bool](./hasuncommittedupdates.md)
  A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [func reconfigureItems(at: [IndexPath])](./reconfigureitems%28at%29.md)
  Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads all of the data for the collection view.
- [func reloadSections(IndexSet)](./reloadsections%28_%29.md)
  Reloads the data in the specified sections of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reloaditems(at:))*