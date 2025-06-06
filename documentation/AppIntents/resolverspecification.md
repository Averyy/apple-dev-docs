# ResolverSpecification

**Framework**: App Intents  
**Kind**: protocol

An internal type that a resolver uses to convert data values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol ResolverSpecification : Hashable, Sendable, Sequence where Self.Element == any Resolver
```

#### Overview

Don’t use a [`ResolverSpecification`](resolverspecification.md) type directly in your code. The system uses this type internally to manage the resolution process.

## Topics

### Getting the value type
- [associatedtype Output : _IntentValue](resolverspecification/output.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)
### Conforming Types
- [EmptyResolverSpecification](emptyresolverspecification.md)
- [ResolverSpecificationBuilder.Specification](resolverspecificationbuilder/specification.md)

## See Also

- [struct EmptyResolverSpecification](emptyresolverspecification.md)
- [struct StringSearchCriteriaFromStringResolverSpecificification](stringsearchcriteriafromstringresolverspecificification.md)
  An internal type that a resolver uses to convert data values.
- [enum ResolverSpecificationBuilder](resolverspecificationbuilder.md)
  A result builder that declaratively specifies a set of resolvers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolverspecification)*