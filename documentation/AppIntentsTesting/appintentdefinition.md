# AppIntentDefinition

**Framework**: App Intents Testing  
**Kind**: struct

A definition you use to dynamically create intent instances for testing.

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
struct AppIntentDefinition
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Overview

To create an app intent instance for testing, instantiate its corresponding intent definition for your app intent using [`IntentDefinitions`](intentdefinitions.md), then create an intent instance using [`makeIntent`](appintentdefinition/makeintent.md) as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let orderIntent = definitions.intents[
    "OrderCoffeeIntent"
]
let intent = orderIntent.makeIntent(
    size: "large",
    type: "latte"
)
```

## Topics

### Creating an app intent instance
- [var makeIntent: IntentValuePropertiesCallable<AnyAppIntent>](appintentdefinition/makeintent.md)
  Creates a populated instance of this intent.
### Identifying the intent
- [let identifier: String](appintentdefinition/identifier.md)
  The intent’s identifier.
- [let bundleIdentifier: String](appintentdefinition/bundleidentifier.md)
  The bundle identifier of the app that includes this intent.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var intents: IntentDefinitions.DefinitionCollection<AppIntentDefinition>](intentdefinitions/intents.md)
  The definitions for the target app’s app intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintentdefinition)*