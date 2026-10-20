# MigrationStage.custom(fromVersion:toVersion:willMigrate:didMigrate:)

**Framework**: SwiftData  
**Kind**: case  
**Role**: Case

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
@preconcurrency
case custom(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type, willMigrate: (@Sendable (ModelContext) throws -> Void)?, didMigrate: (@Sendable (ModelContext) throws -> Void)?)
```

## See Also

### Migration stages
- [case lightweight(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type)](./lightweight%28fromversion,toversion%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/migrationstage/custom(fromversion:toversion:willmigrate:didmigrate:))*