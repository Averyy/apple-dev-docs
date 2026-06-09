# transientEntities

**Framework**: App Intents Testing  
**Kind**: property

Retrieve a transient app entity definition using subscript syntax.

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
var transientEntities: IntentDefinitions.DefinitionCollection<TransientAppEntityDefinition> { get }
```

#### Discussion

Access individual transient entity definitions using subscript syntax with the entity’s type name as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let tempOrder = definitions.transientEntities[
    "TempOrderEntity"
]
```

## See Also

- [var entities: IntentDefinitions.DefinitionCollection<AppEntityDefinition>](intentdefinitions/entities.md)
  The definitions for the target app’s app entities.
- [struct AppEntityDefinition](appentitydefinition.md)
  A definition you use to dynamically create entity instances for testing.
- [var valueQueries: IntentDefinitions.DefinitionCollection<IntentValueQueryDefinition>](intentdefinitions/valuequeries.md)
  The definitions for the app’s intent value queries.
- [struct IntentValueQueryDefinition](intentvaluequerydefinition.md)
  A definition you use to create an intent value query for testing.
- [struct TransientAppEntityDefinition](transientappentitydefinition.md)
  A definition you use to dynamically create transient app entities for testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentdefinitions/transiententities)*