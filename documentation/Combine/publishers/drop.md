# Publishers.Drop

**Framework**: Combine  
**Kind**: struct

A publisher that omits a specified number of elements before republishing later elements.

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
struct Drop<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Drop Publisher
- [init(upstream: Upstream, count: Int)](publishers/drop/init(upstream:count:).md)
  Creates a publisher that omits a specified number of elements before republishing later elements.
### Declaring Publisher Topography
- [Publishers.Drop.Output](publishers/drop/output.md)
  The kind of values published by this publisher.
- [Publishers.Drop.Failure](publishers/drop/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/drop/upstream.md)
  The publisher from which this publisher receives elements.
- [let count: Int](publishers/drop/count.md)
  The number of elements to drop.
### Comparing Publishers
- [static func == (Publishers.Drop<Upstream>, Publishers.Drop<Upstream>) -> Bool](publishers/drop/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/drop/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-drop-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](publishers/drop/equatable-implementations.md)
- [Publisher Implementations](publishers/drop/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.DropUntilOutput](publishers/dropuntiloutput.md)
  A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Publishers.DropWhile](publishers/dropwhile.md)
  A publisher that omits elements from an upstream publisher until a given closure returns false.
- [Publishers.TryDropWhile](publishers/trydropwhile.md)
  A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Publishers.Concatenate](publishers/concatenate.md)
  A publisher that emits all of one publisher’s elements before those from another publisher.
- [Publishers.PrefixWhile](publishers/prefixwhile.md)
  A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [Publishers.TryPrefixWhile](publishers/tryprefixwhile.md)
  A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [Publishers.PrefixUntilOutput](publishers/prefixuntiloutput.md)
  A publisher that republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/drop)*