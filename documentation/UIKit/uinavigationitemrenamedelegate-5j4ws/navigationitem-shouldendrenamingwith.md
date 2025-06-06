# navigationItem(_:shouldEndRenamingWith:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate whether to continue or abandon the rename process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func navigationItem(_: UINavigationItem, shouldEndRenamingWith title: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to continue the rename process; [`false`](https://developer.apple.com/documentation/swift/false) to cancel the rename process.

#### Discussion

Implement this method to return [`false`](https://developer.apple.com/documentation/swift/false) to prevent renaming.

> ❗ **Important**:  UIKit might not call this method in certain situations, like when the system pushes a new navigation item onto the navigation bar. In these situations, UIKit calls [`navigationItem(_:didEndRenamingWith:)`](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:didendrenamingwith:).md) instead. Therefore, make sure to implement [`navigationItem(_:didEndRenamingWith:)`](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:didendrenamingwith:).md) to handle the cases when [`navigationItem(_:shouldEndRenamingWith:)`](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:shouldendrenamingwith:).md) returns [`false`](https://developer.apple.com/documentation/swift/false).

 UIKit might not call this method in certain situations, like when the system pushes a new navigation item onto the navigation bar. In these situations, UIKit calls [`navigationItem(_:didEndRenamingWith:)`](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:didendrenamingwith:).md) instead. Therefore, make sure to implement [`navigationItem(_:didEndRenamingWith:)`](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:didendrenamingwith:).md) to handle the cases when [`navigationItem(_:shouldEndRenamingWith:)`](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:shouldendrenamingwith:).md) returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `title`: The new title of the navigation item.

## See Also

- [func navigationItemShouldBeginRenaming(UINavigationItem) -> Bool](uinavigationitemrenamedelegate-5j4ws/navigationitemshouldbeginrenaming(_:).md)
  Asks the delegate whether the navigation item supports renaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:shouldendrenamingwith:))*