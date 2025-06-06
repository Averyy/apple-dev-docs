# MigrationStage.custom(fromVersion:toVersion:willMigrate:didMigrate:)

**Framework**: SwiftData  
**Kind**: case

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
case custom(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type, willMigrate: ((ModelContext) throws -> Void)?, didMigrate: ((ModelContext) throws -> Void)?)
```

## See Also

- [case lightweight(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type)](migrationstage/lightweight(fromversion:toversion:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/migrationstage/custom(fromversion:toversion:willmigrate:didmigrate:))*