# didMigrateHandler

**Framework**: Core Data  
**Kind**: property

The handler to execute after the stage runs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+
- Swift 5.8+

## Declaration

```swift
var didMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage) throws -> Void)? { get set }
```

#### Discussion

Use this handler to perform any cleanup tasks on the persistent store’s data after the migration has run. Access the store using the [`container`](nsstagedmigrationmanager/container.md) property of the handler’s `migrationManager` parameter.

## See Also

- [var willMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage) throws -> Void)?](nscustommigrationstage/willmigratehandler-5wead.md)
  The handler to execute before the stage runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage/didmigratehandler-2zbss)*