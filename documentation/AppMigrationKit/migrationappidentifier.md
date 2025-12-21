# MigrationAppIdentifier

**Framework**: AppMigrationKit  
**Kind**: struct

A type that identifies an app on a different platform.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct MigrationAppIdentifier
```

## Topics

### Creating a migration app identifier
- [init(storeIdentifier: MigrationAppIdentifier.StoreIdentifier, bundleIdentifier: String, platform: MigrationPlatform)](migrationappidentifier/init(storeidentifier:bundleidentifier:platform:).md)
  Creates a migration app identifier instance.
### Working with identifier properties
- [let storeIdentifier: MigrationAppIdentifier.StoreIdentifier](migrationappidentifier/storeidentifier-swift.property.md)
  An identifier that indicates the store in which the app resides.
- [MigrationAppIdentifier.StoreIdentifier](migrationappidentifier/storeidentifier-swift.struct.md)
  A type that indicates an app store in which an app resides.
- [let bundleIdentifier: String](migrationappidentifier/bundleidentifier.md)
  The bundle identifier of the app within the store.
- [let platform: MigrationPlatform](migrationappidentifier/platform.md)
  The platform in which the app resides.
- [struct MigrationPlatform](migrationplatform.md)
  A type that identifies the platform used by the other device in a migration.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let sourceAppIdentifier: MigrationAppIdentifier](resourcesimportrequest/sourceappidentifier.md)
  The application that exported the content.
- [let sourceVersion: String](resourcesimportrequest/sourceversion.md)
  The data format version provided by the source application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationappidentifier)*