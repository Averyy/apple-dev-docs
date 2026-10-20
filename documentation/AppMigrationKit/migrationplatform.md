# MigrationPlatform

**Framework**: AppMigrationKit  
**Kind**: struct  
**Role**: Structure

A type that identifies the platform used by the other device in a migration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct MigrationPlatform
```

## Topics

### Creating a migration platform instance
- [init(String)](./migrationplatform/init%28_%29.md)
  Creates a migration platform instance from the given raw value string.
### Identifying migration platforms
- [static let android: MigrationPlatform](./migrationplatform/android.md)
  The Android platform, as used in a migration.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting migration request properties
- [let destinationPlatform: MigrationPlatform](./migrationrequestwithoptions/destinationplatform.md)
  The destination platform of the migration request.
- [let options: [OptionsType : Data]](./migrationrequestwithoptions/options.md)
  Export options requested by the destination device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationplatform)*