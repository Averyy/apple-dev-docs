# NSCustomMigrationStage

**Framework**: Core Data  
**Kind**: class

An object that enables you to participate in the migration between two versions of the same model.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class NSCustomMigrationStage
```

#### Overview

Use [`NSCustomMigrationStage`](nscustommigrationstage.md) when you have two versions of a model that Core Data can’t automatically migrate. Custom migration stages enable you to participate in the migration process by assigning handlers that the stage invokes before and after it runs. The handlers provide an opportunity to prepare the persistent store’s data for the upcoming changes before the stage runs, and perform any cleanup tasks afterward.

For example, to support a migration that changes an optional attribute to be nonoptional, you might assign a handler to the stage’s [`willMigrateHandler`](nscustommigrationstage/willmigratehandler-5wead.md) property that sets any `nil` instances of that attribute to a default value, thereby ensuring the migration succeeds. To access the store you’re migrating, use the [`container`](nsstagedmigrationmanager/container.md) property of the migration manager that Core Data provides to every handler.

## Topics

### Creating a custom migration stage
- [convenience init(migratingFrom: NSManagedObjectModelReference, to: NSManagedObjectModelReference)](nscustommigrationstage/init(migratingfrom:to:).md)
  Creates a custom migration stage with the specified source and destination model references.
- [class NSManagedObjectModelReference](nsmanagedobjectmodelreference.md)
  An object that describes a specific version of an object model.
### Accessing model references
- [var currentModel: NSManagedObjectModelReference](nscustommigrationstage/currentmodel.md)
  The reference that represents the migration’s source model.
- [var nextModel: NSManagedObjectModelReference](nscustommigrationstage/nextmodel.md)
  The reference that represents the migration’s destination model.
### Assigning event handlers
- [var willMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage) throws -> Void)?](nscustommigrationstage/willmigratehandler-5wead.md)
  The handler to execute before the stage runs.
- [var didMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage) throws -> Void)?](nscustommigrationstage/didmigratehandler-2zbss.md)
  The handler to execute after the stage runs.

## Relationships

### Inherits From
- [NSMigrationStage](nsmigrationstage.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSLightweightMigrationStage](nslightweightmigrationstage.md)
  An object that describes a series of models suitable for lightweight migration.
- [class NSMigrationStage](nsmigrationstage.md)
  An abstract base class for describing an individual stage of a migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage)*