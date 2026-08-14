# AppEnumDefinition

**Framework**: App Intents Testing  
**Kind**: struct

An app enumeration definition for testing and dynamic enumeration creation.

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
struct AppEnumDefinition
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Overview

To create an app enum for testing, load the enum definition using [`IntentDefinitions`](intentdefinitions.md) and its [`enums`](intentdefinitions/enums.md) property. Then, set its value as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let colorEnum = definitions.enums["Color"]
let redCase = colorEnum.makeCase("red") // Matches `Color.red`.
```

## Topics

### Creating an enumeration case
- [func makeCase(String) -> AnyAppEnum](appenumdefinition/makecase(_:).md)
  Creates an enumeration case with the specified raw value.
### Identifying the enum
- [let typeIdentifier: String](appenumdefinition/typeidentifier.md)
  The enum type’s unique identifier.
### Default Implementations
- [AppIntentTypeDefinition Implementations](appenumdefinition/appintenttypedefinition-implementations.md)

## Relationships

### Conforms To
- [AppIntentTypeDefinition](appintenttypedefinition.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)

## See Also

- [var enums: IntentDefinitions.DefinitionCollection<AppEnumDefinition>](intentdefinitions/enums.md)
  The definitions for the target app’s app enums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appenumdefinition)*