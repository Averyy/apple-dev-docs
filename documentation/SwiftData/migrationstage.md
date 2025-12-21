# MigrationStage

**Framework**: SwiftData  
**Kind**: enum

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
- [case lightweight(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type)](migrationstage/lightweight(fromversion:toversion:).md)
- [case custom(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type, willMigrate: ((ModelContext) throws -> Void)?, didMigrate: ((ModelContext) throws -> Void)?)](migrationstage/custom(fromversion:toversion:willmigrate:didmigrate:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var stages: [MigrationStage]](schemamigrationplan/stages.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/migrationstage)*