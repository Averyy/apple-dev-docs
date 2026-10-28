# sceneUserInfoKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key that reflects the new locked state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let sceneUserInfoKey: String
```

```c
extern NSString * const UIPointerLockStateSceneUserInfoKey;
```

## Discussion

The `userInfo` dictionary of the notification contains the [`sceneUserInfoKey`](./sceneuserinfokey.md) key, which reflects the new value of the [`isLocked`](./islocked.md) property.

## See Also

### Updating the Lock State
- [class let didChangeNotification: NSNotification.Name](./didchangenotification.md)
  A notification that posts when the value of the locked state for a scene changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerlockstate/sceneuserinfokey)*