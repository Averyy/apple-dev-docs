# visibilityUserInfoKey

**Framework**: AppKit  
**Kind**: property

The visibly of the font collection. An NSNumber containing a value from the [`NSFontCollection.Visibility`](nsfontcollection/visibility.md) enum.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let visibilityUserInfoKey: NSFontCollection.UserInfoKey
```

## See Also

- [class let actionUserInfoKey: NSFontCollection.UserInfoKey](nsfontcollection/actionuserinfokey.md)
  An action was taken. See `NSFontCollectionAction Key Values` for the possible values. An `NSString`.
- [class let nameUserInfoKey: NSFontCollection.UserInfoKey](nsfontcollection/nameuserinfokey.md)
  The font collection’s name. If renamed, this is the new name. An `NSString`.
- [class let oldNameUserInfoKey: NSFontCollection.UserInfoKey](nsfontcollection/oldnameuserinfokey.md)
  Included as a value for the [`oldNameUserInfoKey`](nsfontcollection/oldnameuserinfokey.md) key, if present. This is the previous name. An `NSString`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/visibilityuserinfokey)*