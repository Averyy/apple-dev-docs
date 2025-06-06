# Publishers.Concatenate

**Framework**: Combine  
**Kind**: struct

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

### Creating a Concatenate Publisher
- [init(prefix: Prefix, suffix: Suffix)](publishers/concatenate/init(prefix:suffix:).md)
  Creates a publisher that emits all of one publisher’s elements before those from another publisher.
### Declaring Publisher Topography
- [Publishers.Concatenate.Output](publishers/concatenate/output.md)
  The kind of values published by this publisher.
- [Publishers.Concatenate.Failure](publishers/concatenate/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let prefix: Prefix](publishers/concatenate/prefix.md)
  The publisher to republish, in its entirety, before republishing elements from `suffix`.
- [let suffix: Suffix](publishers/concatenate/suffix.md)
  The publisher to republish only after `prefix` finishes.
### Comparing Publishers
- [static func == (Publishers.Concatenate<Prefix, Suffix>, Publishers.Concatenate<Prefix, Suffix>) -> Bool](publishers/concatenate/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/concatenate/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-concatenate-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](publishers/concatenate/equatable-implementations.md)
- [Publisher Implementations](publishers/concatenate/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.DropUntilOutput](publishers/dropuntiloutput.md)
  A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Publishers.Drop](publishers/drop.md)
  A publisher that omits a specified number of elements before republishing later elements.
- [Publishers.DropWhile](publishers/dropwhile.md)
  A publisher that omits elements from an upstream publisher until a given closure returns false.
- [Publishers.TryDropWhile](publishers/trydropwhile.md)
  A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Publishers.PrefixWhile](publishers/prefixwhile.md)
  A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [Publishers.TryPrefixWhile](publishers/tryprefixwhile.md)
  A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [Publishers.PrefixUntilOutput](publishers/prefixuntiloutput.md)
  A publisher that republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/concatenate)*