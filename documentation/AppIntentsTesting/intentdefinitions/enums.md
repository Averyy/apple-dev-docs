# enums

**Framework**: App Intents Testing  
**Kind**: property

The definitions for the target app’s app enums.

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