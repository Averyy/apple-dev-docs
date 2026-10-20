# passTypeIdentifierUserInfoKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

The pass’s pass type identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let passTypeIdentifierUserInfoKey: PKPassLibraryNotificationKey
```

```c
extern PKPassLibraryNotificationKey const PKPassLibraryPassTypeIdentifierUserInfoKey;
```

## See Also

### Notification keys
- [static let addedPassesUserInfoKey: PKPassLibraryNotificationKey](./addedpassesuserinfokey.md)
  An array of added passes.
- [static let recoveredPassesUserInfoKey: PKPassLibraryNotificationKey](./recoveredpassesuserinfokey.md)
- [static let removedPassInfosUserInfoKey: PKPassLibraryNotificationKey](./removedpassinfosuserinfokey.md)
  An array of dictionaries that describes the removed passes.
- [static let replacementPassesUserInfoKey: PKPassLibraryNotificationKey](./replacementpassesuserinfokey.md)
  An array of replaced passes.
- [static let serialNumberUserInfoKey: PKPassLibraryNotificationKey](./serialnumberuserinfokey.md)
  The pass’s serial number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/passtypeidentifieruserinfokey)*