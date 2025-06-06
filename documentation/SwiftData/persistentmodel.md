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

- [Adding and editing persistent data in your app](adding-and-editing-persistent-data-in-your-app.md)
  Create a data entry form for collecting and changing data managed by SwiftData.
- [Deleting persistent data from your app](deleting-persistent-data-from-your-app.md)
  Explore different ways to use SwiftData to delete persistent data.
- [Defining data relationships with enumerations and model classes](defining-data-relationships-with-enumerations-and-model-classes.md)
  Create relationships for static and dynamic data stored in your app.
- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md)
  Create and update a persistent store to cache read-only network data.
- [macro Model()](model().md)
  Converts a Swift class into a stored model that’s managed by SwiftData.
- [macro Attribute(Schema.Attribute.Option..., originalName: String?, hashModifier: String?)](attribute(_:originalname:hashmodifier:).md)
  Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.
- [macro Transient()](transient().md)
  Tells SwiftData not to persist the annotated property when managing the owning class.
- [macro Relationship(Schema.Relationship.Option..., deleteRule: Schema.Relationship.DeleteRule, minimumModelCount: Int?, maximumModelCount: Int?, originalName: String?, inverse: AnyKeyPath?, hashModifier: String?)](relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:).md)
  Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentmodel)*