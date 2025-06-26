# Model()

**Framework**: SwiftData  
**Kind**: macro

Converts a Swift class into a stored model that’s managed by SwiftData.

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
@attached
(member, conformances: Observable, PersistentModel, Sendable, names: named(_$backingData), named(persistentBackingData), named(schemaMetadata), named(init), named(_$observationRegistrar), named(_SwiftDataNoType), named(access), named(withMutation)) @attached(memberAttribute) @attached(extension, conformances: Observable, PersistentModel, Sendable) macro Model()
```

## Mentions

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

#### Overview

Annotate your model classes with the `@Model` macro to make them persistable. At build time, the macro expands to provide conformance to the [`PersistentModel`](persistentmodel.md) and [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocols.

```swift
@Model
class RemoteImage {
    var sourceURL: URL
    var data: Data
    
    init(sourceURL: URL, data: Data = Data()) {
        self.sourceURL = sourceURL
        self.data = data
    }
}
```

For more information about defining models, see [`Preserving your app’s model data across launches`](preserving-your-apps-model-data-across-launches.md).

## See Also

- [macro Attribute(Schema.Attribute.Option..., originalName: String?, hashModifier: String?)](attribute(_:originalname:hashmodifier:).md)
  Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.
- [macro Unique<T>([PartialKeyPath<T>]...)](unique(_:).md)
  Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances.
- [macro Index<T>([PartialKeyPath<T>]...)](index(_:)-74ia2.md)
  Specifies the key-paths that SwiftData uses to create one or more binary indices for the associated model.
- [macro Index<T>(Schema.Index<T>.Types<T>...)](index(_:)-7d4z0.md)
  Specifies the key-paths that SwiftData uses to create one or more indicies for the associated model, where each index is either binary or R-tree.
- [Defining data relationships with enumerations and model classes](defining-data-relationships-with-enumerations-and-model-classes.md)
  Create relationships for static and dynamic data stored in your app.
- [macro Relationship(Schema.Relationship.Option..., deleteRule: Schema.Relationship.DeleteRule, minimumModelCount: Int?, maximumModelCount: Int?, originalName: String?, inverse: AnyKeyPath?, hashModifier: String?)](relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:).md)
  Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.
- [macro Transient()](transient().md)
  Tells SwiftData not to persist the annotated property when managing the owning class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/model())*