# Publishers.DropWhile

**Framework**: Combine  
**Kind**: struct

A publisher that omits elements from an upstream publisher until a given closure returns false.

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
struct DropWhile<Upstream> where Upstream : Publisher
```

## Topics

### Creating a drop while publisher
- [init(upstream: Upstream, predicate: (Publishers.DropWhile<Upstream>.Output) -> Bool)](publishers/dropwhile/init(upstream:predicate:).md)
  Creates a publisher that omits elements from an upstream publisher until a given closure returns false.
### Declaring supporting types
- [Publishers.DropWhile.Output](publishers/dropwhile/output.md)
  The kind of values published by this publisher.
- [Publishers.DropWhile.Failure](publishers/dropwhile/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/dropwhile/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.DropWhile<Upstream>.Output) -> Bool](publishers/dropwhile/predicate.md)
  The closure that indicates whether to drop the element.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.DropUntilOutput](publishers/dropuntiloutput.md)
  A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Publishers.Drop](publishers/drop.md)
  A publisher that omits a specified number of elements before republishing later elements.
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

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/dropwhile)*