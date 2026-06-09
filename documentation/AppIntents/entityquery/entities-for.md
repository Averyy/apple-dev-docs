# entities(for:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Retrieves instances by identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func entities(for identifiers: [Self.Entity.ID]) async throws -> [Self.Entity]
```

## Mentions

- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

#### Discussion

The system skips identifiers that have no matching entity, so the returned array can have fewer entries than the supplied identifiers.

## Parameters

- `identifiers`: An array of entity identifiers.

## See Also

- [associatedtype Entity : AppEntity = Self.Result.Result.ValueType](entityquery/entity.md)
  The entity type that this query knows how to resolve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery/entities(for:))*