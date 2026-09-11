# makeReference(identifier:)

**Framework**: App Intents Testing  
**Kind**: method

Creates an app entity instance of the given entity type.

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
func makeReference(identifier: String) -> AnyAppEntity
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Discussion

```swift
let entityDefinition: AppEntityDefinition!

let entityRef = entityDefinition.reference(identifier: "unique-id-123")
``

- Parameter identifier: The entity instance's unique identifier.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/makereference(identifier:))*