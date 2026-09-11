# IntentDefinitions.DefinitionCollection

**Framework**: App Intents Testing  
**Kind**: struct

A collection of a specific type of definition.

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