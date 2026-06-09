# makeReference(identifier:)

**Framework**: App Intents Testing  
**Kind**: method

Creates an app entity instance of the given entity type.

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