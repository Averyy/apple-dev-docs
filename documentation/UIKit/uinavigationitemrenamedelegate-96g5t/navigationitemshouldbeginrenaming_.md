# navigationItemShouldBeginRenaming:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the navigation item supports renaming.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (BOOL) navigationItemShouldBeginRenaming:(UINavigationItem *) navigationItem;
```

#### Return Value

[`true`](../../Swift/true.md) to support renaming and show Rename in the title menu; otherwise, [`false`](../../Swift/false.md).

#### Discussion

UIKit calls this method when the navigation bar’s title menu becomes visible to validate whether to show Rename as part of that menu. Implement this method to determine whether to display the Rename menu element and support the rename process.

## Parameters

- `navigationItem`: The navigation item asking whether to support renaming.

## See Also

### Determining rename support
- [- navigationItem:shouldEndRenamingWithTitle:](./navigationitem_shouldendrenamingwithtitle_.md)
  Asks the delegate whether to continue or abandon the rename process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitemshouldbeginrenaming:)*