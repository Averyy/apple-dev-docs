# Entity

**Framework**: App Intents  
**Kind**: associatedtype  
**Required**: Yes

The entity type that this query knows how to resolve.

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
associatedtype Entity : AppEntity = Self.Result.Result.ValueType where Self.Entity == Self.Result.Result
```

## See Also

- [func entities(for: [Self.Entity.ID]) async throws -> [Self.Entity]](entityquery/entities(for:).md)
  Retrieves instances by identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery/entity)*