# didChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when the value of the locked state for a scene changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let didChangeNotification: NSNotification.Name
```

#### Discussion

This notification is sent when the value in the [`isLocked`](uipointerlockstate/islocked.md) property changes. The `userInfo` dictionary of the notification contains the [`sceneUserInfoKey`](uipointerlockstate/sceneuserinfokey.md) key, which reflects the new value of the [`isLocked`](uipointerlockstate/islocked.md) property.

## See Also

- [class let sceneUserInfoKey: String](uipointerlockstate/sceneuserinfokey.md)
  A key that reflects the new locked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerlockstate/didchangenotification)*