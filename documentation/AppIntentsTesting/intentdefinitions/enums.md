# enums

**Framework**: App Intents Testing  
**Kind**: property

The definitions for the target app’s app enums.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var enums: IntentDefinitions.DefinitionCollection<AppEnumDefinition> { get }
```

#### Discussion

Access individual enum definitions using subscript syntax with the enum’s type name as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let coffeeSizeEnum = definitions.enums[
    "CoffeeSizeEnum"
]
```

## See Also

- [struct AppEnumDefinition](appenumdefinition.md)
  An app enumeration definition for testing and dynamic enumeration creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentdefinitions/enums)*