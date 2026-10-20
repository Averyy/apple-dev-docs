# MigrationStage

**Framework**: SwiftData  
**Kind**: enum  
**Role**: Enumeration

Describes a migration between two versions of the same schema.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
enum MigrationStage
```

## Topics

### Migration stages
- [case lightweight(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type)](./migrationstage/lightweight%28fromversion,toversion%29.md)
- [case custom(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type, willMigrate: ((ModelContext) throws -> Void)?, didMigrate: ((ModelContext) throws -> Void)?)](./migrationstage/custom%28fromversion,toversion,willmigrate,didmigrate%29.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing migration stages
- [static var stages: [MigrationStage]](./schemamigrationplan/stages.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/migrationstage)*