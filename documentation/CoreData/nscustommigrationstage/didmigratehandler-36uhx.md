# didMigrateHandler

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The handler to execute after the stage runs.

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
@property (copy, nullable) _Bool (^)(NSStagedMigrationManager *, NSCustomMigrationStage *, NSError **) didMigrateHandler;
```

## Discussion

Use this handler to perform any cleanup tasks on the persistent store’s data after the migration has run. Access the store using the [`container`](../nsstagedmigrationmanager/container.md) property of the handler’s `migrationManager` parameter.

## See Also

### Assigning event handlers
- [willMigrateHandler](./willmigratehandler-72p73.md)
  The handler to execute before the stage runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage/didmigratehandler-36uhx)*