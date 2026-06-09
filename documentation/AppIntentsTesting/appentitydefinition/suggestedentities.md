# suggestedEntities()

**Framework**: App Intents Testing  
**Kind**: method

Fetches all suggested entities of this type.

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
func suggestedEntities() async throws -> [AnyAppEntity]
```

#### Return Value

An array of suggested app entities.

#### Discussion

The system uses suggested entities for disambiguation and recommendations in Shortcuts and Siri.

> **Note**: Any errors encountered during the query execution.

## See Also

- [func suggestedEntitiesQuery() -> AnyEntityQuery](appentitydefinition/suggestedentitiesquery.md)
  Creates an entity query that retrieves suggested entities of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/suggestedentities())*