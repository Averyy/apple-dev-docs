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

### Operators
- [static func == (StringSearchCriteria, StringSearchCriteria) -> Bool](stringsearchcriteria/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(term: String)](stringsearchcriteria/init(term:).md)
### Instance Properties
- [var hashValue: Int](stringsearchcriteria/hashvalue.md)
  The hash value.
- [var term: String](stringsearchcriteria/term.md)
  The full search term given by the user.
### Instance Methods
- [func hash(into: inout Hasher)](stringsearchcriteria/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [StringSearchCriteria.SearchScopes](stringsearchcriteria/searchscopes.md)
- [StringSearchCriteria.Specification](stringsearchcriteria/specification.md)
- [StringSearchCriteria.UnwrappedType](stringsearchcriteria/unwrappedtype.md)
- [StringSearchCriteria.ValueType](stringsearchcriteria/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](stringsearchcriteria/defaultresolverspecification.md)
### Default Implementations
- [Equatable Implementations](stringsearchcriteria/equatable-implementations.md)

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