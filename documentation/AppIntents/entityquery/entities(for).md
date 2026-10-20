# entities(for:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Retrieves instances by identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func entities(for identifiers: [Self.Entity.ID]) async throws -> [Self.Entity]
```

## Mentions

- [Defining app entities for your custom data types](../defining-app-entities-for-your-custom-data-types.md)

#### Discussion

The system skips identifiers that have no matching entity, so the returned array can have fewer entries than the supplied identifiers.

## Parameters

- `identifiers`: An array of entity identifiers.

## Default Implementations

### EntityQuery Implementations
- [func entities(for: [Self.Unique.ID]) async throws -> [Self.Unique]](./entities%28for%29-luma.md)

## See Also

### Searching for entities
- [associatedtype Entity : AppEntity = Self.Result.Result.ValueType](./entity.md)
  The entity type that this query knows how to resolve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery/entities(for:))*