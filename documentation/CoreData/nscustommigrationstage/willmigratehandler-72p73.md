# willMigrateHandler

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The handler to execute before the stage runs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (copy, nullable) _Bool (^)(NSStagedMigrationManager *, NSCustomMigrationStage *, NSError **) willMigrateHandler;
```

## Discussion

Use this handler to prepare the persistent store’s data for the pending migration. Access the store using the [`container`](../nsstagedmigrationmanager/container.md) property of the handler’s `migrationManager` parameter.

## See Also

### Assigning event handlers
- [didMigrateHandler](./didmigratehandler-36uhx.md)
  The handler to execute after the stage runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage/willmigratehandler-72p73)*