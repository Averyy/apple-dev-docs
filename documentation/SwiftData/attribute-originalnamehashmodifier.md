# Attribute(_:originalName:hashModifier:)

**Framework**: SwiftData  
**Kind**: macro

Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.

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
(peer) macro Attribute(_ options: Schema.Attribute.Option..., originalName: String? = nil, hashModifier: String? = nil)
```

## Mentions

- [Fetching and filtering time-based model changes](fetching-and-filtering-time-based-model-changes.md)
- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

#### Overview

The framework’s default behavior for managing a model class’s stored properties is suitable for most use cases. However, if you need to alter the persistence behavior of a particular property, annotate it with the `@Attribute` macro. For example, you may want to avoid conflicts in your model data by specifying that an attribute’s value is unique across all instances of that model.

```swift
@Model
class RemoteImage {
    @Attribute(.unique) var sourceURL: URL
    var data: Data
    
    init(sourceURL: URL, data: Data = Data()) {
        self.sourceURL = sourceURL
        self.data = data
    }
}
```

## Parameters

- `options`: A list of options to apply to the attached property to customize its behavior. For possible values, see  .
- `originalName`: The previous name of the attribute, if it’s different to the one in the current schema version. The default value is  .
- `hashModifier`: A unique hash value that represents the most recent version of the attached property. The default value is  .

## See Also

- [macro Model()](model().md)
  Converts a Swift class into a stored model that’s managed by SwiftData.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/attribute(_:originalname:hashmodifier:))*