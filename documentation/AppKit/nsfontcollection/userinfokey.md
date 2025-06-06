# NSFontCollection.UserInfoKey

**Framework**: AppKit  
**Kind**: struct

These constants are used as keys in the [`didChangeNotification`](nsfontcollection/didchangenotification.md) `userInfo` dictionary to indicate the changes that have taken place.

**Availability**:
- macOS ?+

## Declaration

```swift
struct UserInfoKey
```

## Topics

### User Info Keys
- [class let actionUserInfoKey: NSFontCollection.UserInfoKey](nsfontcollection/actionuserinfokey.md)
  An action was taken. See `NSFontCollectionAction Key Values` for the possible values. An `NSString`.
- [class let nameUserInfoKey: NSFontCollection.UserInfoKey](nsfontcollection/nameuserinfokey.md)
  The font collection’s name. If renamed, this is the new name. An `NSString`.
- [class let oldNameUserInfoKey: NSFontCollection.UserInfoKey](nsfontcollection/oldnameuserinfokey.md)
  Included as a value for the [`oldNameUserInfoKey`](nsfontcollection/oldnameuserinfokey.md) key, if present. This is the previous name. An `NSString`.
- [class let visibilityUserInfoKey: NSFontCollection.UserInfoKey](nsfontcollection/visibilityuserinfokey.md)
  The visibly of the font collection. An NSNumber containing a value from the [`NSFontCollection.Visibility`](nsfontcollection/visibility.md) enum.
### Initializers
- [init(rawValue: String)](nsfontcollection/userinfokey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class let didChangeNotification: NSNotification.Name](nsfontcollection/didchangenotification.md)
  Posted whenever a font collection is changed.
- [NSFontCollection.ActionTypeKey](nsfontcollection/actiontypekey.md)
  The following actions are possible values of the [`actionUserInfoKey`](nsfontcollection/actionuserinfokey.md) in the [`didChangeNotification`](nsfontcollection/didchangenotification.md) `userInfo` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/userinfokey)*