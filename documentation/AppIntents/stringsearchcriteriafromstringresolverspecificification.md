# StringSearchCriteriaFromStringResolverSpecificification

**Framework**: App Intents  
**Kind**: struct

An internal type that a resolver uses to convert data values.

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
struct StringSearchCriteriaFromStringResolverSpecificification
```

#### Overview

Don’t use a `StringSearchCriteriaFromStringResolverSpecificification` type directly in your code. The system uses this type internally to manage the resolution process.

## Topics

### Resolving the type
- [func resolve(from: String, context: IntentParameterContext<StringSearchCriteria>) async throws -> StringSearchCriteria?](stringsearchcriteriafromstringresolverspecificification/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (StringSearchCriteriaFromStringResolverSpecificification, StringSearchCriteriaFromStringResolverSpecificification) -> Bool](stringsearchcriteriafromstringresolverspecificification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](stringsearchcriteriafromstringresolverspecificification/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](stringsearchcriteriafromstringresolverspecificification/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [StringSearchCriteriaFromStringResolverSpecificification.Input](stringsearchcriteriafromstringresolverspecificification/input.md)
- [StringSearchCriteriaFromStringResolverSpecificification.Output](stringsearchcriteriafromstringresolverspecificification/output.md)
### Default Implementations
- [Equatable Implementations](stringsearchcriteriafromstringresolverspecificification/equatable-implementations.md)
- [Resolver Implementations](stringsearchcriteriafromstringresolverspecificification/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol ResolverSpecification](resolverspecification.md)
  An internal type that a resolver uses to convert data values.
- [struct EmptyResolverSpecification](emptyresolverspecification.md)
- [enum ResolverSpecificationBuilder](resolverspecificationbuilder.md)
  A result builder that declaratively specifies a set of resolvers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringsearchcriteriafromstringresolverspecificification)*