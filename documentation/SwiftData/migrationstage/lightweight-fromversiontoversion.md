# MigrationStage.lightweight(fromVersion:toVersion:)

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
case lightweight(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type)
```

## See Also

- [case custom(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type, willMigrate: ((ModelContext) throws -> Void)?, didMigrate: ((ModelContext) throws -> Void)?)](migrationstage/custom(fromversion:toversion:willmigrate:didmigrate:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/migrationstage/lightweight(fromversion:toversion:))*