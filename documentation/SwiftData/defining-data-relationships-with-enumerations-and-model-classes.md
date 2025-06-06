# Defining data relationships with enumerations and model classes

**Framework**: SwiftData

Create relationships for static and dynamic data stored in your app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- Xcode 15.0+

#### Overview

There are two ways to define data relationships in your app: using enumerations and using the [`Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)`](relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:).md) macro in a model class. Which one to use depends on the unique circumstances of your app. This article explains how to apply both approaches to the sample [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) app that persist data using SwiftData.

##### Relate a Model Class to Static Data

Enumerations are a convenient way to form relationships between a model class and static data — data that the app defines and doesn’t change. To define the static data, create an enumeration and ensure it conforms to the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol. SwiftData requires this conformance to persist any data that is of the enumeration type. The following code, for example, declares a `Codable` conforming enumeration that specify the animal type based on their diets:

```swift
extension Animal {
    enum Diet: String, CaseIterable, Codable {
        case herbivorous = "Herbivore"
        case carnivorous = "Carnivore"
        case omnivorous = "Omnivore"
    }
}
```

The `Animal` model class declares the property `diet` as a type of `Diet`. Because this property is non-optional, its value must be set to one of the `Diet` cases: `herbivore`, `carnivore`, and `ominvore`.

```swift
@Model
final class Animal {
    var name: String
    var diet: Diet
    var category: AnimalCategory?
    
    init(name: String, diet: Diet) {
        self.name = name
        self.diet = diet
    }
}
```

A person using the sample app can set the diet of an animal by choosing one of the available `Diet` cases from a [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker); for example:

```swift
Picker("Diet", selection: $selectedDiet) {
    ForEach(Animal.Diet.allCases, id: \.self) { diet in
        Text(diet.rawValue).tag(diet)
    }
}
```

To learn more about how the sample app saves data changes, see [`Adding and editing persistent data in your app`](adding-and-editing-persistent-data-in-your-app.md).

##### Relate a Model Class to Dynamic Data

If the related data is dynamic and unknown to the app — data that comes from an external source such as someone using the app or a remote server — then form a relationship between two model classes instead of a class and enumeration. For instance, the dynamic data in the sample app includes animals and animal categories. An animal can belong to no more than one animal category, and a category can contain zero, one, or more animals.

To declare this relationship, the `AnimalCategory` class defines the property `animals`, which represents the animals contained in the category. The class also applies the [`Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)`](relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:).md) macro to the `animals` property. This macro defines the relationship between the `AnimalCategory` and `Animal` model classes.

```swift
@Model
final class AnimalCategory {
    @Attribute(.unique) var name: String
    // `.cascade` tells SwiftData to delete all animals contained in the 
    // category when deleting it.
    @Relationship(deleteRule: .cascade, inverse: \Animal.category)
    var animals = [Animal]()
    
    init(name: String) {
        self.name = name
    }
}
```

Set the parameter values of this macro to configure the relationship. For example, the `deleteRule` parameter specifies how SwiftData handles related data during delete operations. The `inverse` parameter is a key path to the store property, `category`, declared in the related model class, `Animal`. The inverse parameter forms the relationship between the two classes, `AnimalCategory` and `Animal`, and the `category` property declared in `Animal` provides a reference to an animal category.

##### Set a Relationships Delete Rule

The `deleteRule` parameter specifies how SwiftData handles delete operations with regards to the related data. The [`Schema.Relationship.DeleteRule.cascade`](schema/relationship/deleterule-swift.enum/cascade.md) delete rule tells SwiftData to delete all related data when deleting the primary object. For example, deleting an `AnimalCategory` in the sample app causes SwiftData to also delete all animals contained in that category.

```swift
@Relationship(deleteRule: .cascade, inverse: \Animal.category)
var animals = [Animal]()
```

If you don’t want to delete the animals within a category, you can use the [`Schema.Relationship.DeleteRule.nullify`](schema/relationship/deleterule-swift.enum/nullify.md) delete rule. This rule tells SwiftData to set the animal’s `category` property to `nil` for each animal contained in the animal category when deleting the category. Because the default value for the `deleteRule` parameter is `nullify`, you can create the relationship without explicitly specifying the delete rule, like so:

```swift
@Relationship(inverse: \Animal.category)
var animals = [Animal]()
```

For a complete list of delete rules, see [`Schema.Relationship.DeleteRule`](schema/relationship/deleterule-swift.enum.md).

##### Create a Model Container

Whether your data model includes relationships, you must always create a model container for your app when using SwiftData. The sample app creates a model container using the [`modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)`](https://developer.apple.com/documentation/SwiftUI/View/modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)-18hhy) modifier, passing in the model type `AnimalCategory.self`:

```swift
@main
struct SwiftDataAnimalsApp: App {
    var body: some Scene {
        WindowGroup() {
            ContentView()
        }
        .modelContainer(for: AnimalCategory.self)
    }
}
```

SwiftData uses the model type to construct the schema that determines the structure of the persistent storage area. The schema also includes all related types that form the object graph of the provided model type. For instance, `AnimalCategory` is a root model type of an object graph. `AnimalCategory` contains a relationship to the model type `Animal`, which means that the schema includes `Animal` along with `AnimalCategory`. If `Animal` had a relationship to another model type, the schema would also include that type.

If your app defines multiple root model types, use the
[`modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)`](https://developer.apple.com/documentation/SwiftUI/View/modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)-8oc48) modifier, passing in an array that contains each root model type used in your app.

## See Also

- [Adding and editing persistent data in your app](adding-and-editing-persistent-data-in-your-app.md)
  Create a data entry form for collecting and changing data managed by SwiftData.
- [Deleting persistent data from your app](deleting-persistent-data-from-your-app.md)
  Explore different ways to use SwiftData to delete persistent data.
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
- [protocol PersistentModel](persistentmodel.md)
  An interface that enables SwiftData to manage a Swift class as a stored model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defining-data-relationships-with-enumerations-and-model-classes)*