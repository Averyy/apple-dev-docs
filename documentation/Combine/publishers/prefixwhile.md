# Publishers.PrefixWhile

**Framework**: Combine  
**Kind**: struct

A publisher that republishes elements while a predicate closure indicates publishing should continue.

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
struct PrefixWhile<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Prefix While Publisher
- [init(upstream: Upstream, predicate: (Publishers.PrefixWhile<Upstream>.Output) -> Bool)](publishers/prefixwhile/init(upstream:predicate:).md)
  Creates a publisher that republishes elements while a predicate closure indicates publishing should continue.
### Declaring Publisher Topography
- [Publishers.PrefixWhile.Output](publishers/prefixwhile/output.md)
  The kind of values published by this publisher.
- [Publishers.PrefixWhile.Failure](publishers/prefixwhile/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/prefixwhile/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.PrefixWhile<Upstream>.Output) -> Bool](publishers/prefixwhile/predicate.md)
  The closure that determines whether publishing should continue.
### Applying Operators
- [Publisher Operators](publishers-prefixwhile-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/prefixwhile/publisher-implementations.md)

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
- [Publishers.TryDropWhile](publishers/trydropwhile.md)
  A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Publishers.Concatenate](publishers/concatenate.md)
  A publisher that emits all of one publisher’s elements before those from another publisher.
- [Publishers.TryPrefixWhile](publishers/tryprefixwhile.md)
  A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [Publishers.PrefixUntilOutput](publishers/prefixuntiloutput.md)
  A publisher that republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/prefixwhile)*