# sceneUserInfoKey

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

The `userInfo` dictionary of the notification contains the [`sceneUserInfoKey`](uipointerlockstate/sceneuserinfokey.md) key, which reflects the new value of the [`isLocked`](uipointerlockstate/islocked.md) property.

## See Also

- [class let didChangeNotification: NSNotification.Name](uipointerlockstate/didchangenotification.md)
  A notification that posts when the value of the locked state for a scene changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerlockstate/sceneuserinfokey)*