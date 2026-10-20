# MigrationAppIdentifier.StoreIdentifier

**Framework**: AppMigrationKit  
**Kind**: struct  
**Role**: Structure

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
- [init(String)](./storeidentifier-swift.struct/init%28_%29.md)
### Type Properties
- [static let googlePlay: MigrationAppIdentifier.StoreIdentifier](./storeidentifier-swift.struct/googleplay.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with identifier properties
- [let storeIdentifier: MigrationAppIdentifier.StoreIdentifier](./storeidentifier-swift.property.md)
  An identifier that indicates the store in which the app resides.
- [let bundleIdentifier: String](./bundleidentifier.md)
  The bundle identifier of the app within the store.
- [let platform: MigrationPlatform](./platform.md)
  The platform in which the app resides.
- [struct MigrationPlatform](../migrationplatform.md)
  A type that identifies the platform used by the other device in a migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationappidentifier/storeidentifier-swift.struct)*