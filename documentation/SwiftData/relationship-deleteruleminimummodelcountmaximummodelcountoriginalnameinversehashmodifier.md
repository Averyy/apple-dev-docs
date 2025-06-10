# Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)

**Framework**: SwiftData  
**Kind**: macro

Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.

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
(peer) macro Relationship(_ options: Schema.Relationship.Option..., deleteRule: Schema.Relationship.DeleteRule = .nullify, minimumModelCount: Int? = 0, maximumModelCount: Int? = 0, originalName: String? = nil, inverse: AnyKeyPath? = nil, hashModifier: String? = nil)
```

## Mentions

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

#### Overview

If one or more of a model’s properties represent relationships between their containing model and another model, annotate those properties with the `@Relationship` macro. This enables SwiftData to enforce those relationships at runtime — including what happens if you delete related data – as well as write any associated metadata to the persistent storage so the relationships exist across app launches.

In the following example, a remote image may belong to a category, and a category can contain zero, one, or more images.

```swift
@Model
class RemoteImage {
    @Attribute(.unique) var sourceURL: URL
    @Relationship(inverse: \Category.images) var category: Category?
    var data: Data

    init(sourceURL: URL, data: Data = Data()) {
        self.sourceURL = sourceURL
        self.data = data
    }
}

@Model
class Category {
    @Attribute(.unique) var name: String
    @Relationship var images = [RemoteImage]()

    init(name: String) {
        self.name = name
    }
}
```

> **Note**: If you declare a relationship attribute as optional when defining your persistent models, SwiftData only enforces `minimumModelCount` and `maximumModelCount` when that attribute isn’t nil.

For more information about defining relationships between models, see [`Defining data relationships with enumerations and model classes`](defining-data-relationships-with-enumerations-and-model-classes.md).

## Parameters

- `options`: A list of options to apply to the annotated property to customize its behavior. For possible values, see  .
- `deleteRule`: The rule to apply when you delete the relationship’s owning persistent model. For possible values, see  . The default value is  .
- `minimumModelCount`: The minimum number of models the relationship can reference. The default value is  .
- `maximumModelCount`: The maximum number of models the relationship can reference. The default value is  .
- `originalName`: The previous name of the attribute, if it’s different to the one in the current schema version. The default value is  .
- `inverse`: The key path of the relationship that represents the inverse of this relationship. The default value is  .
- `hashModifier`: A unique hash value that represents the most recent version of the annotated property. The default value is  .

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
- [protocol PersistentModel](persistentmodel.md)
  An interface that enables SwiftData to manage a Swift class as a stored model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:))*