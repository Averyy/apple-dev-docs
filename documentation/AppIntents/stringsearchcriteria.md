# StringSearchCriteria

**Framework**: App Intents  
**Kind**: struct

A structure that represents a string-based search request.

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
struct StringSearchCriteria
```

## Topics

### Initializers
- [init(term: String)](stringsearchcriteria/init(term:).md)
### Instance Properties
- [var term: String](stringsearchcriteria/term.md)
  The full search term given by the user.
### Type Aliases
- [StringSearchCriteria.Specification](stringsearchcriteria/specification.md)
- [StringSearchCriteria.UnwrappedType](stringsearchcriteria/unwrappedtype.md)
- [StringSearchCriteria.ValueType](stringsearchcriteria/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](stringsearchcriteria/defaultresolverspecification.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [SearchCriteria](searchcriteria.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var criteria: Self.Criteria](showinappsearchresultsintent/criteria-swift.property.md)
- [protocol SearchCriteria](searchcriteria.md)
- [associatedtype Criteria : SearchCriteria](showinappsearchresultsintent/criteria-swift.associatedtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringsearchcriteria)*