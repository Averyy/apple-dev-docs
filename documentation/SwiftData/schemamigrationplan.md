# SchemaMigrationPlan

**Framework**: SwiftData  
**Kind**: protocol

An interface for describing the evolution of a schema and how to migrate between specific versions.

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
protocol SchemaMigrationPlan : SendableMetatype
```

## Topics

### Managing versioned schemas
- [static var schemas: [any VersionedSchema.Type]](schemamigrationplan/schemas.md)
- [protocol VersionedSchema](versionedschema.md)
  An interface for describing a specific version of a schema, including the models it contains.
### Managing migration stages
- [static var stages: [MigrationStage]](schemamigrationplan/stages.md)
- [enum MigrationStage](migrationstage.md)
  Describes a migration between two versions of the same schema.

## Relationships

### Inherits From
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: [ModelConfiguration]) throws](modelcontainer/init(for:migrationplan:configurations:)-1czix.md)
  Creates a model container using the specified schema, migration plan, and configurations.
- [convenience init(for: any PersistentModel.Type..., migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-8s4ts.md)
  Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [convenience init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-qof9.md)
  Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [protocol PersistentModel](persistentmodel.md)
  An interface that enables SwiftData to manage a Swift class as a stored model.
- [struct ModelConfiguration](modelconfiguration.md)
  A type that describes the configuration of an app’s schema or specific group of models.
- [class Schema](schema.md)
  An object that maps model classes to data in the model store, and helps with the migration of that data between releases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schemamigrationplan)*