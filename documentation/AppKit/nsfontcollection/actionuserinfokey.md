# actionUserInfoKey

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An action was taken. See `NSFontCollectionAction Key Values` for the possible values. An `NSString`.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let actionUserInfoKey: NSFontCollection.UserInfoKey
```

```c
extern NSFontCollectionUserInfoKey const NSFontCollectionActionKey;
```

## See Also

### User Info Keys
- [class let nameUserInfoKey: NSFontCollection.UserInfoKey](./nameuserinfokey.md)
  The font collection’s name. If renamed, this is the new name. An `NSString`.
- [class let oldNameUserInfoKey: NSFontCollection.UserInfoKey](./oldnameuserinfokey.md)
  Included as a value for the [`oldNameUserInfoKey`](./oldnameuserinfokey.md) key, if present. This is the previous name. An `NSString`.
- [class let visibilityUserInfoKey: NSFontCollection.UserInfoKey](./visibilityuserinfokey.md)
  The visibly of the font collection. An NSNumber containing a value from the [`NSFontCollection.Visibility`](./visibility.md) enum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/actionuserinfokey)*