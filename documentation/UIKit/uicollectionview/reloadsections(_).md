# reloadSections(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the data in the specified sections of the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func reloadSections(_ sections: IndexSet)
```

```objc
- (void) reloadSections:(NSIndexSet *) sections;
```

#### Discussion

Call this method to selectively reload only the items in the specified sections. This causes the collection view to discard any cells associated with those items and redisplay them. This method also discards any placeholders in the specified sections.

## Parameters

- `sections`: The indexes of the sections to reload.

## See Also

### Reloading content
- [var hasUncommittedUpdates: Bool](./hasuncommittedupdates.md)
  A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [func reconfigureItems(at: [IndexPath])](./reconfigureitems%28at%29.md)
  Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads all of the data for the collection view.
- [func reloadItems(at: [IndexPath])](./reloaditems%28at%29.md)
  Reloads just the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reloadsections(_:))*