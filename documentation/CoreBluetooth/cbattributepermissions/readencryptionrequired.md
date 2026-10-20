# readEncryptionRequired

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Type Property

A permission that indicates only trusted devices can read the attribute’s value.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var readEncryptionRequired: CBAttributePermissions { get }
```

```c
CBAttributePermissionsReadEncryptionRequired
```

## See Also

### Permissions
- [static var readable: CBAttributePermissions](./readable.md)
  A permission that indicates a peripheral can read the attribute’s value.
- [static var writeable: CBAttributePermissions](./writeable.md)
  A permission that indicates a peripheral can write the attribute’s value.
- [static var writeEncryptionRequired: CBAttributePermissions](./writeencryptionrequired.md)
  A permission that indicates only trusted devices can write the attribute’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/readencryptionrequired)*