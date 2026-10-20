# navigationItemShouldBeginRenaming(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate whether the navigation item supports renaming.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func navigationItemShouldBeginRenaming(_: UINavigationItem) -> Bool
```

#### Return Value

[`true`](../../Swift/true.md) to support renaming and show Rename in the title menu; otherwise, [`false`](../../Swift/false.md).

#### Discussion

UIKit calls this method when the navigation bar’s title menu becomes visible to validate whether to show Rename as part of that menu. Implement this method to determine whether to display the Rename menu element and support the rename process.

## Default Implementations

### UINavigationItemRenameDelegate Implementations
- [func navigationItemShouldBeginRenaming(UINavigationItem) -> Bool](./navigationitemshouldbeginrenaming%28_%29-7kane.md)

## See Also

### Determining rename support
- [func navigationItem(UINavigationItem, shouldEndRenamingWith: String) -> Bool](./navigationitem%28_,shouldendrenamingwith%29.md)
  Asks the delegate whether to continue or abandon the rename process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitemshouldbeginrenaming(_:))*