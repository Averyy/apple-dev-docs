# SearchCriteria

**Framework**: App Intents  
**Kind**: protocol

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
protocol SearchCriteria : _IntentValue, Hashable, Sendable
```

## Topics

### Associated Types
- [associatedtype SearchScopes = Void](searchcriteria/searchscopes.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [StringSearchCriteria](stringsearchcriteria.md)

## See Also

- [var criteria: Self.Criteria](showinappsearchresultsintent/criteria-swift.property.md)
- [struct StringSearchCriteria](stringsearchcriteria.md)
  A structure that represents a string-based search request.
- [associatedtype Criteria : SearchCriteria](showinappsearchresultsintent/criteria-swift.associatedtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/searchcriteria)*