# AccessorySecurity.Error

**Framework**: Accessory Transport Extension  
**Kind**: enum

Errors that can occur during cryptographic operations.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
enum Error
```

## Topics

### Identifying key material errors
- [AccessorySecurity.Error.missingKeyMaterial](accessorysecurity/error/missingkeymaterial.md)
  An error that indicates required key material is missing.
- [AccessorySecurity.Error.missingSecret](accessorysecurity/error/missingsecret.md)
  An error that indicates a required secret is missing.
### Identifying cryptographic operation errors
- [AccessorySecurity.Error.encryptionFailed(_:)](accessorysecurity/error/encryptionfailed(_:).md)
  An error that indicates encryption failed.
- [AccessorySecurity.Error.decryptionFailed(_:)](accessorysecurity/error/decryptionfailed(_:).md)
  An error that indicates decryption failed.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity/error)*