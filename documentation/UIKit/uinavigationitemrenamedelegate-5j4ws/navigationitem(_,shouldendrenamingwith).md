# navigationItem(_:shouldEndRenamingWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate whether to continue or abandon the rename process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func navigationItem(_: UINavigationItem, shouldEndRenamingWith title: String) -> Bool
```

## Return Value

[`true`](../../Swift/true.md) to continue the rename process; [`false`](../../Swift/false.md) to cancel the rename process.

## Discussion

Implement this method to return [`false`](../../Swift/false.md) to prevent renaming.

> ❗ **Important**:  UIKit might not call this method in certain situations, like when the system pushes a new navigation item onto the navigation bar. In these situations, UIKit calls [`navigationItem(_:didEndRenamingWith:)`](./navigationitem%28_,didendrenamingwith%29.md) instead. Therefore, make sure to implement [`navigationItem(_:didEndRenamingWith:)`](./navigationitem%28_,didendrenamingwith%29.md) to handle the cases when [`navigationItem(_:shouldEndRenamingWith:)`](./navigationitem%28_,shouldendrenamingwith%29.md) returns [`false`](../../Swift/false.md).

## Parameters

- `_`: The navigation item attempting to continue the rename process.
- `title`: The new title of the navigation item.

## Default Implementations

### UINavigationItemRenameDelegate Implementations
- [func navigationItem(UINavigationItem, shouldEndRenamingWith: String) -> Bool](./navigationitem%28_,shouldendrenamingwith%29-5ld6b.md)

## See Also

### Determining rename support
- [func navigationItemShouldBeginRenaming(UINavigationItem) -> Bool](./navigationitemshouldbeginrenaming%28_%29.md)
  Asks the delegate whether the navigation item supports renaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:shouldendrenamingwith:))*