# Index(_:)

**Framework**: SwiftData  
**Kind**: macro

Specifies the key-paths that SwiftData uses to create one or more indicies for the associated model, where each index is either binary or R-tree.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
@freestanding
(declaration) macro Index<T>(_ indices: Schema.Index<T>.Types<T>...) where T : PersistentModel
```

## See Also

- [macro Model()](model().md)
  Converts a Swift class into a stored model that’s managed by SwiftData.
- [macro Attribute(Schema.Attribute.Option..., originalName: String?, hashModifier: String?)](attribute(_:originalname:hashmodifier:).md)
  Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.
- [macro Unique<T>([PartialKeyPath<T>]...)](unique(_:).md)
  Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances.
- [macro Index<T>([PartialKeyPath<T>]...)](index(_:)-74ia2.md)
  Specifies the key-paths that SwiftData uses to create one or more binary indices for the associated model.
- [Defining data relationships with enumerations and model classes](defining-data-relationships-with-enumerations-and-model-classes.md)
  Create relationships for static and dynamic data stored in your app.
- [macro Relationship(Schema.Relationship.Option..., deleteRule: Schema.Relationship.DeleteRule, minimumModelCount: Int?, maximumModelCount: Int?, originalName: String?, inverse: AnyKeyPath?, hashModifier: String?)](relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:).md)
  Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.
- [macro Transient()](transient().md)
  Tells SwiftData not to persist the annotated property when managing the owning class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/index(_:)-7d4z0)*