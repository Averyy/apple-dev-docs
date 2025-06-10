# init(for:migrationPlan:configurations:)

**Framework**: SwiftData  
**Kind**: init

Creates a model container using the specified schema, migration plan, and zero or more configurations.

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
convenience init(for givenSchema: Schema, migrationPlan: (any SchemaMigrationPlan.Type)? = nil, configurations: ModelConfiguration...) throws
```

#### Discussion

> ❗ **Important**: A container must have at least one configuration. If you don’t specify any, the framework creates an instance of [`ModelConfiguration`](modelconfiguration.md) for you by combining your app’s entitlements with the type’s default values.

## Parameters

- `givenSchema`: A schema that maps your app’s model classes to the associated data in the app’s persistent storage. For more information, see  .
- `migrationPlan`: A plan that describes the evolution of your app’s schema and how the container migrates between specific versions. For more information, see  .
- `configurations`: A list of configurations that describe how the container manages the persisted data for specific groups of models. For more information, see  .

## See Also

- [init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: [ModelConfiguration]) throws](modelcontainer/init(for:migrationplan:configurations:)-1czix.md)
  Creates a model container using the specified schema, migration plan, and configurations.
- [convenience init(for: any PersistentModel.Type..., migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-8s4ts.md)
  Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [struct ModelConfiguration](modelconfiguration.md)
  A type that describes the configuration of an app’s schema or specific group of models.
- [class Schema](schema.md)
  An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
- [protocol SchemaMigrationPlan](schemamigrationplan.md)
  An interface for describing the evolution of a schema and how to migrate between specific versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontainer/init(for:migrationplan:configurations:)-qof9)*