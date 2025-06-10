# ResolverSpecificationBuilder.Specification

**Framework**: App Intents  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Specification<Output, each R> where Output : _IntentValue, repeat each R : Resolver
```

## Topics

### Operators
- [static func == (ResolverSpecificationBuilder<Property>.Specification<Output, repeat each R>, ResolverSpecificationBuilder<Property>.Specification<Output, repeat each R>) -> Bool](resolverspecificationbuilder/specification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](resolverspecificationbuilder/specification/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](resolverspecificationbuilder/specification/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func makeIterator() -> Array<any Resolver>.Iterator](resolverspecificationbuilder/specification/makeiterator.md)
  Returns an iterator over the elements of this sequence.
### Type Aliases
- [ResolverSpecificationBuilder.Specification.Element](resolverspecificationbuilder/specification/element.md)
  A type representing the sequence’s elements.
- [ResolverSpecificationBuilder.Specification.Iterator](resolverspecificationbuilder/specification/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
### Default Implementations
- [Equatable Implementations](resolverspecificationbuilder/specification/equatable-implementations.md)
- [Sequence Implementations](resolverspecificationbuilder/specification/sequence-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ResolverSpecification](resolverspecification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolverspecificationbuilder/specification)*