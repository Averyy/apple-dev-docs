# intents

**Framework**: App Intents Testing  
**Kind**: property

The definitions for the target app’s app intents.

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
var intents: IntentDefinitions.DefinitionCollection<AppIntentDefinition> { get }
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Discussion

Access individual intent definitions using subscript syntax with the intent’s type name as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let orderIntent = definitions.intents[
    "OrderCoffeeIntent"
]
```

## See Also

- [struct AppIntentDefinition](appintentdefinition.md)
  A definition you use to dynamically create intent instances for testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentdefinitions/intents)*