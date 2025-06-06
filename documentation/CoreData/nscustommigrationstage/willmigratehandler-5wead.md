# willMigrateHandler

**Framework**: Core Data  
**Kind**: property

The handler to execute before the stage runs.

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
var willMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage) throws -> Void)? { get set }
```

#### Discussion

Use this handler to prepare the persistent store’s data for the pending migration. Access the store using the [`container`](nsstagedmigrationmanager/container.md) property of the handler’s `migrationManager` parameter.

## See Also

- [var didMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage) throws -> Void)?](nscustommigrationstage/didmigratehandler-2zbss.md)
  The handler to execute after the stage runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage/willmigratehandler-5wead)*