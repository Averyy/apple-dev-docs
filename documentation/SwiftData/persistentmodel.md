# PersistentModel

**Framework**: SwiftData  
**Kind**: protocol  
**Role**: Protocol

An interface that enables SwiftData to manage a Swift class as a stored model.

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
protocol PersistentModel : AnyObject, Observable, Hashable, Identifiable, SendableMetatype
```

## Mentions

- [Preserving your app’s model data across launches](./preserving-your-apps-model-data-across-launches.md)

## Topics

### Creating a persistent model
- [init(backingData: any BackingData<Self>)](./persistentmodel/init%28backingdata%29.md)
### Identifying the model instance
- [var persistentModelID: PersistentIdentifier](./persistentmodel/persistentmodelid.md)
- [struct PersistentIdentifier](./persistentidentifier.md)
  A type that describes the aggregate identity of a SwiftData model.
- [var modelContext: ModelContext?](./persistentmodel/modelcontext.md)
### Accessing a value by key path
- [func getValue<Value, OtherModel>(forKey: KeyPath<Self, Value>) -> Value](./persistentmodel/getvalue%28forkey%29-299oe.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value>) -> Value](./persistentmodel/getvalue%28forkey%29-3o59k.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value>) -> Value](./persistentmodel/getvalue%28forkey%29-4cs0c.md)
- [func getValue<Value, OtherModel>(forKey: KeyPath<Self, Value>) -> Value](./persistentmodel/getvalue%28forkey%29-5m792.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value?>) -> Value?](./persistentmodel/getvalue%28forkey%29-998oq.md)
- [func getTransformableValue<Value>(forKey: KeyPath<Self, Value>) -> Value](./persistentmodel/gettransformablevalue%28forkey%29.md)
### Modifying a value by key path
- [func setValue<Value, OtherModel>(forKey: KeyPath<Self, Value>, to: Value)](./persistentmodel/setvalue%28forkey,to%29-18176.md)
- [func setValue<Value, OtherModel>(forKey: KeyPath<Self, Value>, to: Value)](./persistentmodel/setvalue%28forkey,to%29-3mmp2.md)
- [func setValue<Value>(forKey: KeyPath<Self, Value?>, to: Value?)](./persistentmodel/setvalue%28forkey,to%29-3uqwc.md)
- [func setValue<Value>(forKey: KeyPath<Self, Value>, to: Value)](./persistentmodel/setvalue%28forkey,to%29-8wepb.md)
- [func setValue<Value>(forKey: KeyPath<Self, Value>, to: Value)](./persistentmodel/setvalue%28forkey,to%29-xt24.md)
- [func setTransformableValue<Value>(forKey: KeyPath<Self, Value>, to: Value)](./persistentmodel/settransformablevalue%28forkey,to%29.md)
### Accessing supplementary information
- [static var schemaMetadata: [Schema.PropertyMetadata]](./persistentmodel/schemametadata.md)
- [var persistentBackingData: any BackingData<Self>](./persistentmodel/persistentbackingdata.md)
- [var hasChanges: Bool](./persistentmodel/haschanges.md)
- [var isDeleted: Bool](./persistentmodel/isdeleted.md)
### Internal
- [Internal symbols](./persistentmodelinternal.md)
  Restricted-use symbols that the framework requires for macro expansion and other internal tasks.
### Associated Types
- [associatedtype Root : PersistentModel = Self](./persistentmodel/root.md)
### Type Methods
- [static func createBackingData<P>() -> some BackingData<P>
](./persistentmodel/createbackingdata%28%29.md)
### Default Implementations
- [Equatable Implementations](./persistentmodel/equatable-implementations.md)
- [Hashable Implementations](./persistentmodel/hashable-implementations.md)

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Observable](../Observation/observable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a model container
- [init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: [ModelConfiguration]) throws](./modelcontainer/init%28for,migrationplan,configurations%29-1czix.md)
  Creates a model container using the specified schema, migration plan, and configurations.
- [convenience init(for: any PersistentModel.Type..., migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](./modelcontainer/init%28for,migrationplan,configurations%29-8s4ts.md)
  Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [convenience init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](./modelcontainer/init%28for,migrationplan,configurations%29-qof9.md)
  Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [struct ModelConfiguration](./modelconfiguration.md)
  A type that describes the configuration of an app’s schema or specific group of models.
- [class Schema](./schema.md)
  An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
- [protocol SchemaMigrationPlan](./schemamigrationplan.md)
  An interface for describing the evolution of a schema and how to migrate between specific versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentmodel)*