# Publishers.Concatenate

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that emits all of one publisher’s elements before those from another publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Concatenate<Prefix, Suffix> where Prefix : Publisher, Suffix : Publisher, Prefix.Failure == Suffix.Failure, Prefix.Output == Suffix.Output
```

## Topics

### Creating a concatenate publisher
- [init(prefix: Prefix, suffix: Suffix)](./concatenate/init%28prefix,suffix%29.md)
  Creates a publisher that emits all of one publisher’s elements before those from another publisher.
### Declaring supporting types
- [Publishers.Concatenate.Output](./concatenate/output.md)
  The kind of values published by this publisher.
- [Publishers.Concatenate.Failure](./concatenate/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let prefix: Prefix](./concatenate/prefix.md)
  The publisher to republish, in its entirety, before republishing elements from `suffix`.
- [let suffix: Suffix](./concatenate/suffix.md)
  The publisher to republish only after `prefix` finishes.
### Comparing publishers
- [static func == (Publishers.Concatenate<Prefix, Suffix>, Publishers.Concatenate<Prefix, Suffix>) -> Bool](./concatenate/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./concatenate/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Applying sequence operations to elements
- [Publishers.DropUntilOutput](./dropuntiloutput.md)
  A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Publishers.Drop](./drop.md)
  A publisher that omits a specified number of elements before republishing later elements.
- [Publishers.DropWhile](./dropwhile.md)
  A publisher that omits elements from an upstream publisher until a given closure returns false.
- [Publishers.TryDropWhile](./trydropwhile.md)
  A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Publishers.PrefixWhile](./prefixwhile.md)
  A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [Publishers.TryPrefixWhile](./tryprefixwhile.md)
  A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [Publishers.PrefixUntilOutput](./prefixuntiloutput.md)
  A publisher that republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/concatenate)*