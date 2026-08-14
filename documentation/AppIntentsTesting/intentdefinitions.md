# IntentDefinitions

**Framework**: App Intents Testing  
**Kind**: struct

A collection of definitions that catalog your app’s intents, enums, entities, and queries.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct IntentDefinitions
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Overview

Use the `IntentDefinitions` structure as the entry point for creating type-erased app intents for testing. Provide the bundle identifier of the app under test, then use subscript syntax to retrieve definitions for intents, entities, enums, or value queries as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)

let intent = definitions.intents["OrderCoffeeIntent"]
    .makeIntent(size: "large")
let entity = definitions.entities["CoffeeEntity"]
    .makeReference(identifier: "latte-123")
let enumCase = definitions.enums["CoffeeSizeEnum"]
    .makeCase("large")
```

## Topics

### Creating an intent definition
- [init(bundleIdentifier: String)](intentdefinitions/init(bundleidentifier:).md)
  Creates a new collection of definitions for intents that the specified app bundle contains.
- [let bundleIdentifier: String](intentdefinitions/bundleidentifier.md)
  The bundle identifier of the app target under test.
### Accessing app intents
- [var intents: IntentDefinitions.DefinitionCollection<AppIntentDefinition>](intentdefinitions/intents.md)
  The definitions for the target app’s app intents.
- [struct AppIntentDefinition](appintentdefinition.md)
  A definition you use to dynamically create intent instances for testing.
### Accessing app entities and queries
- [var entities: IntentDefinitions.DefinitionCollection<AppEntityDefinition>](intentdefinitions/entities.md)
  The definitions for the target app’s app entities.
- [struct AppEntityDefinition](appentitydefinition.md)
  A definition you use to dynamically create entity instances for testing.
- [var valueQueries: IntentDefinitions.DefinitionCollection<IntentValueQueryDefinition>](intentdefinitions/valuequeries.md)
  The definitions for the app’s intent value queries.
- [struct IntentValueQueryDefinition](intentvaluequerydefinition.md)
  A definition you use to create an intent value query for testing.
- [var transientEntities: IntentDefinitions.DefinitionCollection<TransientAppEntityDefinition>](intentdefinitions/transiententities.md)
  Retrieve a transient app entity definition using subscript syntax.
- [struct TransientAppEntityDefinition](transientappentitydefinition.md)
  A definition you use to dynamically create transient app entities for testing.
### Accessing app enums
- [var enums: IntentDefinitions.DefinitionCollection<AppEnumDefinition>](intentdefinitions/enums.md)
  The definitions for the target app’s app enums.
- [struct AppEnumDefinition](appenumdefinition.md)
  An app enumeration definition for testing and dynamic enumeration creation.
### Supporting types
- [IntentDefinitions.DefinitionCollection](intentdefinitions/definitioncollection.md)
  A collection of a specific type of definition.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentdefinitions)*