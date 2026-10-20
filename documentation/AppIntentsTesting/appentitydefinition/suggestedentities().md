# suggestedEntities()

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Fetches all suggested entities of this type.

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
func suggestedEntities() async throws -> [AnyAppEntity]
```

#### Return Value

An array of suggested app entities.

#### Discussion

The system uses suggested entities for disambiguation and recommendations in Shortcuts and Siri.

> **Throws**: Any errors encountered during the query execution.

## See Also

### Accessing suggested entities
- [func suggestedEntitiesQuery() -> AnyEntityQuery](./suggestedentitiesquery%28%29.md)
  Creates an entity query that retrieves suggested entities of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/suggestedentities())*