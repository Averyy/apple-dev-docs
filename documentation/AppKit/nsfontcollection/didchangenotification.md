# didChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever a font collection is changed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSFontCollectionDidChangeNotification;
```

#### Discussion

The notification’s object is the font collection that was affected. The notification’s `userInfo` dictionary contains information about the the collection change containing the keys defined in [`NSFontCollection.UserInfoKey`](./userinfokey.md) and the corresponding values.

To observe this notification using Swift concurrency, use [`NSFontCollection.DidChangeMessage`](./didchangemessage.md).

## See Also

### Responding to Changes
- [NSFontCollection.UserInfoKey](./userinfokey.md)
  These constants are used as keys in the [`didChangeNotification`](./didchangenotification.md) `userInfo` dictionary to indicate the changes that have taken place.
- [NSFontCollection.ActionTypeKey](./actiontypekey.md)
  The following actions are possible values of the [`actionUserInfoKey`](./actionuserinfokey.md) in the [`didChangeNotification`](./didchangenotification.md) `userInfo` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/didchangenotification)*