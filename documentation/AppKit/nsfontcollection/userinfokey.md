# NSFontCollection.UserInfoKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

These constants are used as keys in the [`didChangeNotification`](./didchangenotification.md) `userInfo` dictionary to indicate the changes that have taken place.

**Availability**:
- macOS

## Declaration

```swift
struct UserInfoKey
```

```c
typedef NSString * NSFontCollectionUserInfoKey;
```

## Topics

### User Info Keys
- [class let actionUserInfoKey: NSFontCollection.UserInfoKey](./actionuserinfokey.md)
  An action was taken. See `NSFontCollectionAction Key Values` for the possible values. An `NSString`.
- [class let nameUserInfoKey: NSFontCollection.UserInfoKey](./nameuserinfokey.md)
  The font collection’s name. If renamed, this is the new name. An `NSString`.
- [class let oldNameUserInfoKey: NSFontCollection.UserInfoKey](./oldnameuserinfokey.md)
  Included as a value for the [`oldNameUserInfoKey`](./oldnameuserinfokey.md) key, if present. This is the previous name. An `NSString`.
- [class let visibilityUserInfoKey: NSFontCollection.UserInfoKey](./visibilityuserinfokey.md)
  The visibly of the font collection. An NSNumber containing a value from the [`NSFontCollection.Visibility`](./visibility.md) enum.
### Initializers
- [init(rawValue: String)](./userinfokey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding to Changes
- [class let didChangeNotification: NSNotification.Name](./didchangenotification.md)
  Posted whenever a font collection is changed.
- [NSFontCollection.ActionTypeKey](./actiontypekey.md)
  The following actions are possible values of the [`actionUserInfoKey`](./actionuserinfokey.md) in the [`didChangeNotification`](./didchangenotification.md) `userInfo` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/userinfokey)*