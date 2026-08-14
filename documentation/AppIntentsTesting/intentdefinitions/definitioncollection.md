# IntentDefinitions.DefinitionCollection

**Framework**: App Intents Testing  
**Kind**: struct

A collection of a specific type of definition.

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
struct DefinitionCollection<Definition>
```

#### Overview

Retrieve individual definitions using their type identifier string as shown in the following example:

```swift
let orderIntent = definitions.intents[
    "OrderCoffeeIntent"
]
```

## Topics

### Subscripts
- [subscript(String) -> Definition](intentdefinitions/definitioncollection/subscript(_:).md)
  Retrieves a type definition using its identifier.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentdefinitions/definitioncollection)*