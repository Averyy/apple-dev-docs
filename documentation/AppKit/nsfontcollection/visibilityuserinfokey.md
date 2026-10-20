# visibilityUserInfoKey

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The visibly of the font collection. An NSNumber containing a value from the [`NSFontCollection.Visibility`](./visibility.md) enum.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let visibilityUserInfoKey: NSFontCollection.UserInfoKey
```

```c
extern NSFontCollectionUserInfoKey const NSFontCollectionVisibilityKey;
```

## See Also

### User Info Keys
- [class let actionUserInfoKey: NSFontCollection.UserInfoKey](./actionuserinfokey.md)
  An action was taken. See `NSFontCollectionAction Key Values` for the possible values. An `NSString`.
- [class let nameUserInfoKey: NSFontCollection.UserInfoKey](./nameuserinfokey.md)
  The font collection’s name. If renamed, this is the new name. An `NSString`.
- [class let oldNameUserInfoKey: NSFontCollection.UserInfoKey](./oldnameuserinfokey.md)
  Included as a value for the [`oldNameUserInfoKey`](./oldnameuserinfokey.md) key, if present. This is the previous name. An `NSString`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/visibilityuserinfokey)*