# didChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSNotificationName const UIPointerLockStateDidChangeNotification;
```

## Discussion

This notification is sent when the value in the [`isLocked`](./islocked.md) property changes. The `userInfo` dictionary of the notification contains the [`sceneUserInfoKey`](./sceneuserinfokey.md) key, which reflects the new value of the [`isLocked`](./islocked.md) property.

## See Also

### Updating the Lock State
- [class let sceneUserInfoKey: String](./sceneuserinfokey.md)
  A key that reflects the new locked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerlockstate/didchangenotification)*