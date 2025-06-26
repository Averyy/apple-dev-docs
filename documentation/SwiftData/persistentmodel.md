# PersistentModel

**Framework**: SwiftData  
**Kind**: protocol

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
protocol PersistentModel : AnyObject, Observable, Hashable, Identifiable
```

## Mentions

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

## Topics

### Creating a persistent model
- [init(backingData: any BackingData<Self>)](persistentmodel/init(backingdata:).md)
### Identifying the model instance
- [var persistentModelID: PersistentIdentifier](persistentmodel/persistentmodelid.md)
- [struct PersistentIdentifier](persistentidentifier.md)
  A type that describes the aggregate identity of a SwiftData model.
- [var modelContext: ModelContext?](persistentmodel/modelcontext.md)
### Accessing a value by key path
- [func getValue<Value, OtherModel>(forKey: KeyPath<Self, Value>) -> Value](persistentmodel/getvalue(forkey:)-299oe.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value>) -> Value](persistentmodel/getvalue(forkey:)-3o59k.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value>) -> Value](persistentmodel/getvalue(forkey:)-4cs0c.md)
- [func getValue<Value, OtherModel>(forKey: KeyPath<Self, Value>) -> Value](persistentmodel/getvalue(forkey:)-5m792.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value?>) -> Value?](persistentmodel/getvalue(forkey:)-998oq.md)
- [func getTransformableValue<Value>(forKey: KeyPath<Self, Value>) -> Value](persistentmodel/gettransformablevalue(forkey:).md)
### Modifying a value by key path
- [func setValue<Value, OtherModel>(forKey: KeyPath<Self, Value>, to: Value)](persistentmodel/setvalue(forkey:to:)-18176.md)
- [func setValue<Value, OtherModel>(forKey: KeyPath<Self, Value>, to: Value)](persistentmodel/setvalue(forkey:to:)-3mmp2.md)
- [func setValue<Value>(forKey: KeyPath<Self, Value?>, to: Value?)](persistentmodel/setvalue(forkey:to:)-3uqwc.md)
- [func setValue<Value>(forKey: KeyPath<Self, Value>, to: Value)](persistentmodel/setvalue(forkey:to:)-8wepb.md)
- [func setValue<Value>(forKey: KeyPath<Self, Value>, to: Value)](persistentmodel/setvalue(forkey:to:)-xt24.md)
- [func setTransformableValue<Value>(forKey: KeyPath<Self, Value>, to: Value)](persistentmodel/settransformablevalue(forkey:to:).md)
### Accessing supplementary information
- [static var schemaMetadata: [Schema.PropertyMetadata]](persistentmodel/schemametadata.md)
- [var persistentBackingData: any BackingData<Self>](persistentmodel/persistentbackingdata.md)
- [var hasChanges: Bool](persistentmodel/haschanges.md)
- [var isDeleted: Bool](persistentmodel/isdeleted.md)
### Internal
- [Internal symbols](persistentmodelinternal.md)
  Restricted-use symbols that the framework requires for macro expansion and other internal tasks.
### Associated Types
- [associatedtype Root : PersistentModel = Self](persistentmodel/root.md)
### Type Methods
- [static func createBackingData<P>() -> some BackingData<P>
](persistentmodel/createbackingdata.md)
### Default Implementations
- [Equatable Implementations](persistentmodel/equatable-implementations.md)
- [Hashable Implementations](persistentmodel/hashable-implementations.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)

## See Also

- [init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: [ModelConfiguration]) throws](modelcontainer/init(for:migrationplan:configurations:)-1czix.md)
  Creates a model container using the specified schema, migration plan, and configurations.
- [convenience init(for: any PersistentModel.Type..., migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-8s4ts.md)
  Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [convenience init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-qof9.md)
  Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [struct ModelConfiguration](modelconfiguration.md)
  A type that describes the configuration of an app’s schema or specific group of models.
- [class Schema](schema.md)
  An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
- [protocol SchemaMigrationPlan](schemamigrationplan.md)
  An interface for describing the evolution of a schema and how to migrate between specific versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentmodel)*