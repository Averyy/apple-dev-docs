# entities

**Framework**: App Intents Testing  
**Kind**: property

The definitions for the target app’s app entities.

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
var entities: IntentDefinitions.DefinitionCollection<AppEntityDefinition> { get }
```

#### Discussion

Access individual entity definitions using subscript syntax with the entity’s type name as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let coffeeEntity = definitions.entities[
    "CoffeeEntity"
]
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentdefinitions/entities)*