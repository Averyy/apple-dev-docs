# PKPassLibraryNotificationKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

The user info keys that a pass library notification uses.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct PKPassLibraryNotificationKey
```

## Topics

### Creating a pass library notification key
- [init(rawValue: String)](pkpasslibrarynotificationkey/init(rawvalue:).md)
  Creates a pass library notification key according to the provided raw value.
### Notification keys
- [static let addedPassesUserInfoKey: PKPassLibraryNotificationKey](pkpasslibrarynotificationkey/addedpassesuserinfokey.md)
  An array of added passes.
- [static let passTypeIdentifierUserInfoKey: PKPassLibraryNotificationKey](pkpasslibrarynotificationkey/passtypeidentifieruserinfokey.md)
  The pass’s pass type identifier.
- [static let recoveredPassesUserInfoKey: PKPassLibraryNotificationKey](pkpasslibrarynotificationkey/recoveredpassesuserinfokey.md)
- [static let removedPassInfosUserInfoKey: PKPassLibraryNotificationKey](pkpasslibrarynotificationkey/removedpassinfosuserinfokey.md)
  An array of dictionaries that describes the removed passes.
- [static let replacementPassesUserInfoKey: PKPassLibraryNotificationKey](pkpasslibrarynotificationkey/replacementpassesuserinfokey.md)
  An array of replaced passes.
- [static let serialNumberUserInfoKey: PKPassLibraryNotificationKey](pkpasslibrarynotificationkey/serialnumberuserinfokey.md)
  The pass’s serial number.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct PKPassLibraryNotificationName](pkpasslibrarynotificationname.md)
  The types of notifications that the pass library posts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey)*