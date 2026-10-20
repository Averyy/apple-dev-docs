# NSFontCollection.ActionTypeKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The following actions are possible values of the [`actionUserInfoKey`](./actionuserinfokey.md) in the [`didChangeNotification`](./didchangenotification.md) `userInfo` method.

**Availability**:
- macOS

## Declaration

```swift
struct ActionTypeKey
```

```c
typedef NSString * NSFontCollectionActionTypeKey;
```

## Topics

### Action Key Types
- [static let shown: NSFontCollection.ActionTypeKey](./actiontypekey/shown.md)
  The font collection was shown.
- [static let hidden: NSFontCollection.ActionTypeKey](./actiontypekey/hidden.md)
  The font collection was hidden.
- [static let renamed: NSFontCollection.ActionTypeKey](./actiontypekey/renamed.md)
  The font collection was renamed.
### Initializers
- [init(rawValue: String)](./actiontypekey/init%28rawvalue%29.md)

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
- [NSFontCollection.UserInfoKey](./userinfokey.md)
  These constants are used as keys in the [`didChangeNotification`](./didchangenotification.md) `userInfo` dictionary to indicate the changes that have taken place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/actiontypekey)*