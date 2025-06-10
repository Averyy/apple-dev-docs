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

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)

#### Discussion

Identifiers for which there is no matching entity are skipped, so the number of elements in the resulting array of entities can be smaller than the number of supplied identifiers.

## Parameters

- `identifiers`: Array of entity identifiers

## See Also

- [associatedtype Entity : AppEntity = Self.Result.Result.ValueType](entityquery/entity.md)
  The entity type that this query knows how to resolve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery/entities(for:))*