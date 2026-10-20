# changedTypesAddedUserInfoKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

With the notification named [`changedNotification`](./changednotification.md), use this key to access the added representation types. These types are stored as an array in the notification’s `userInfo` dictionary.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
nonisolated
class let changedTypesAddedUserInfoKey: String
```

```c
extern NSString * const UIPasteboardChangedTypesAddedKey;
```

## See Also

### Constants
- [class let changedTypesRemovedUserInfoKey: String](./changedtypesremoveduserinfokey.md)
  With the notification named [`changedNotification`](./changednotification.md), use this key to access the removed representation types. These types are stored as an array in the notification’s `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/changedtypesaddeduserinfokey)*