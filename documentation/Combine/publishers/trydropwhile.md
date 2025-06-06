# Publishers.TryDropWhile

**Framework**: Combine  
**Kind**: struct

A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.

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
struct TryDropWhile<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Try Drop While Publisher
- [init(upstream: Upstream, predicate: (Publishers.TryDropWhile<Upstream>.Output) throws -> Bool)](publishers/trydropwhile/init(upstream:predicate:).md)
  Creates a publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
### Declaring Publisher Topography
- [Publishers.TryDropWhile.Output](publishers/trydropwhile/output.md)
  The kind of values published by this publisher.
- [Publishers.TryDropWhile.Failure](publishers/trydropwhile/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/trydropwhile/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.TryDropWhile<Upstream>.Output) throws -> Bool](publishers/trydropwhile/predicate.md)
  The error-throwing closure that indicates whether to drop the element.
### Applying Operators
- [Publisher Operators](publishers-trydropwhile-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/trydropwhile/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.DropUntilOutput](publishers/dropuntiloutput.md)
  A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Publishers.Drop](publishers/drop.md)
  A publisher that omits a specified number of elements before republishing later elements.
- [Publishers.DropWhile](publishers/dropwhile.md)
  A publisher that omits elements from an upstream publisher until a given closure returns false.
- [Publishers.Concatenate](publishers/concatenate.md)
  A publisher that emits all of one publisher’s elements before those from another publisher.
- [Publishers.PrefixWhile](publishers/prefixwhile.md)
  A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [Publishers.TryPrefixWhile](publishers/tryprefixwhile.md)
  A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [Publishers.PrefixUntilOutput](publishers/prefixuntiloutput.md)
  A publisher that republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trydropwhile)*