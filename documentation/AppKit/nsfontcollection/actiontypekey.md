# NSFontCollection.ActionTypeKey

**Framework**: AppKit  
**Kind**: struct

The following actions are possible values of the [`actionUserInfoKey`](nsfontcollection/actionuserinfokey.md) in the [`didChangeNotification`](nsfontcollection/didchangenotification.md) `userInfo` method.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ActionTypeKey
```

## Topics

### Action Key Types
- [static let shown: NSFontCollection.ActionTypeKey](nsfontcollection/actiontypekey/shown.md)
  The font collection was shown.
- [static let hidden: NSFontCollection.ActionTypeKey](nsfontcollection/actiontypekey/hidden.md)
  The font collection was hidden.
- [static let renamed: NSFontCollection.ActionTypeKey](nsfontcollection/actiontypekey/renamed.md)
  The font collection was renamed.
### Initializers
- [init(rawValue: String)](nsfontcollection/actiontypekey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class let didChangeNotification: NSNotification.Name](nsfontcollection/didchangenotification.md)
  Posted whenever a font collection is changed.
- [NSFontCollection.UserInfoKey](nsfontcollection/userinfokey.md)
  These constants are used as keys in the [`didChangeNotification`](nsfontcollection/didchangenotification.md) `userInfo` dictionary to indicate the changes that have taken place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/actiontypekey)*