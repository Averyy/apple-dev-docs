# navigationItem:shouldEndRenamingWithTitle:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to continue or abandon the rename process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (BOOL) navigationItem:(UINavigationItem *) navigationItem shouldEndRenamingWithTitle:(NSString *) title;
```

## Return Value

[`true`](../../Swift/true.md) to continue the rename process; [`false`](../../Swift/false.md) to cancel the rename process.

## Discussion

Implement this method to return [`false`](../../Swift/false.md) to prevent renaming.

> ❗ **Important**:  UIKit might not call this method in certain situations, like when the system pushes a new navigation item onto the navigation bar. In these situations, UIKit calls [`navigationItem:didEndRenamingWithTitle:`](./navigationitem_didendrenamingwithtitle_.md) instead. Therefore, make sure to implement [`navigationItem:didEndRenamingWithTitle:`](./navigationitem_didendrenamingwithtitle_.md) to handle the cases when [`navigationItem:shouldEndRenamingWithTitle:`](./navigationitem_shouldendrenamingwithtitle_.md) returns [`false`](../../Swift/false.md).

## Parameters

- `navigationItem`: The navigation item attempting to continue the rename process.
- `title`: The new title of the navigation item.

## See Also

### Determining rename support
- [- navigationItemShouldBeginRenaming:](./navigationitemshouldbeginrenaming_.md)
  Asks the delegate whether the navigation item supports renaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem:shouldendrenamingwithtitle:)*