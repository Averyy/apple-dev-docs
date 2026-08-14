# MigrationAppIdentifier.StoreIdentifier

**Framework**: AppMigrationKit  
**Kind**: struct

A type that indicates an app store in which an app resides.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct StoreIdentifier
```

## Topics

### Creating a store identifier instance
- [init(String)](migrationappidentifier/storeidentifier-swift.struct/init(_:).md)
### Type Properties
- [static let googlePlay: MigrationAppIdentifier.StoreIdentifier](migrationappidentifier/storeidentifier-swift.struct/googleplay.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let storeIdentifier: MigrationAppIdentifier.StoreIdentifier](migrationappidentifier/storeidentifier-swift.property.md)
  An identifier that indicates the store in which the app resides.
- [let bundleIdentifier: String](migrationappidentifier/bundleidentifier.md)
  The bundle identifier of the app within the store.
- [let platform: MigrationPlatform](migrationappidentifier/platform.md)
  The platform in which the app resides.
- [struct MigrationPlatform](migrationplatform.md)
  A type that identifies the platform used by the other device in a migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationappidentifier/storeidentifier-swift.struct)*