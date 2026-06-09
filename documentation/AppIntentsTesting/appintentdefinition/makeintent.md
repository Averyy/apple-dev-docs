# makeIntent

**Framework**: App Intents Testing  
**Kind**: property

Creates a populated instance of this intent.

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
var makeIntent: IntentValuePropertiesCallable<AnyAppIntent> { get }
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Discussion

The following example shows how you can create an intent instance:

```swift
let definitions = IntentDefinitions(bundleIdentifier: "com.example.exampleapp")
let exampleIntentDefinition = definitions.intents["MyExampleIntent"]

let intent = exampleIntentDefinition.makeIntent(
    paramA: "Hello World",
    paramB: 1234
)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintentdefinition/makeintent)*