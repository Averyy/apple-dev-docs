# hasUncommittedUpdates

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var hasUncommittedUpdates: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasUncommittedUpdates;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), avoid making any significant changes to the collection view. Specifically, don’t reload the collection view’s data, as doing so deletes all placeholders and recreates items from the data source.

## See Also

### Reloading content
- [func reconfigureItems(at: [IndexPath])](./reconfigureitems%28at%29.md)
  Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads all of the data for the collection view.
- [func reloadSections(IndexSet)](./reloadsections%28_%29.md)
  Reloads the data in the specified sections of the collection view.
- [func reloadItems(at: [IndexPath])](./reloaditems%28at%29.md)
  Reloads just the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/hasuncommittedupdates)*