# EmptyResolverSpecification

**Framework**: App Intents  
**Kind**: struct

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
struct EmptyResolverSpecification<Value> where Value : _IntentValue
```

## Topics

### Creating the specification type
- [init()](emptyresolverspecification/init.md)
### Iterating over the values
- [func makeIterator() -> IndexingIterator<[any Resolver]>](emptyresolverspecification/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [EmptyResolverSpecification.Output](emptyresolverspecification/output.md)
### Operators
- [static func == (EmptyResolverSpecification<Value>, EmptyResolverSpecification<Value>) -> Bool](emptyresolverspecification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](emptyresolverspecification/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](emptyresolverspecification/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [EmptyResolverSpecification.Element](emptyresolverspecification/element.md)
  A type representing the sequence’s elements.
- [EmptyResolverSpecification.Iterator](emptyresolverspecification/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
### Default Implementations
- [Equatable Implementations](emptyresolverspecification/equatable-implementations.md)
- [Sequence Implementations](emptyresolverspecification/sequence-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ResolverSpecification](resolverspecification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [protocol ResolverSpecification](resolverspecification.md)
  An internal type that a resolver uses to convert data values.
- [struct StringSearchCriteriaFromStringResolverSpecificification](stringsearchcriteriafromstringresolverspecificification.md)
  An internal type that a resolver uses to convert data values.
- [enum ResolverSpecificationBuilder](resolverspecificationbuilder.md)
  A result builder that declaratively specifies a set of resolvers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/emptyresolverspecification)*