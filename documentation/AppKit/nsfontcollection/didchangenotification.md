# didChangeNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever a font collection is changed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didChangeNotification: NSNotification.Name
```

#### Discussion

The notification’s object is the font collection that was affected. The notification’s `userInfo` dictionary contains information about the the collection change containing the keys defined in [`NSFontCollection.UserInfoKey`](nsfontcollection/userinfokey.md) and the corresponding values.

## See Also

- [NSFontCollection.UserInfoKey](nsfontcollection/userinfokey.md)
  These constants are used as keys in the [`didChangeNotification`](nsfontcollection/didchangenotification.md) `userInfo` dictionary to indicate the changes that have taken place.
- [NSFontCollection.ActionTypeKey](nsfontcollection/actiontypekey.md)
  The following actions are possible values of the [`actionUserInfoKey`](nsfontcollection/actionuserinfokey.md) in the [`didChangeNotification`](nsfontcollection/didchangenotification.md) `userInfo` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/didchangenotification)*