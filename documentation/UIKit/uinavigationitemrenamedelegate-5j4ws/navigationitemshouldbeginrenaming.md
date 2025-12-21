# navigationItemShouldBeginRenaming(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate whether the navigation item supports renaming.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func navigationItemShouldBeginRenaming(_: UINavigationItem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to support renaming and show Rename in the title menu; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

UIKit calls this method when the navigation bar’s title menu becomes visible to validate whether to show Rename as part of that menu. Implement this method to determine whether to display the Rename menu element and support the rename process.

## See Also

- [func navigationItem(UINavigationItem, shouldEndRenamingWith: String) -> Bool](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:shouldendrenamingwith:).md)
  Asks the delegate whether to continue or abandon the rename process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitemshouldbeginrenaming(_:))*