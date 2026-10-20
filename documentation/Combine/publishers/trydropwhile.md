# Publishers.TryDropWhile

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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

### Creating a try-drop-while publisher
- [init(upstream: Upstream, predicate: (Publishers.TryDropWhile<Upstream>.Output) throws -> Bool)](./trydropwhile/init%28upstream,predicate%29.md)
  Creates a publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
### Declaring supporting types
- [Publishers.TryDropWhile.Output](./trydropwhile/output.md)
  The kind of values published by this publisher.
- [Publishers.TryDropWhile.Failure](./trydropwhile/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./trydropwhile/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.TryDropWhile<Upstream>.Output) throws -> Bool](./trydropwhile/predicate.md)
  The error-throwing closure that indicates whether to drop the element.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Applying sequence operations to elements
- [Publishers.DropUntilOutput](./dropuntiloutput.md)
  A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Publishers.Drop](./drop.md)
  A publisher that omits a specified number of elements before republishing later elements.
- [Publishers.DropWhile](./dropwhile.md)
  A publisher that omits elements from an upstream publisher until a given closure returns false.
- [Publishers.Concatenate](./concatenate.md)
  A publisher that emits all of one publisher’s elements before those from another publisher.
- [Publishers.PrefixWhile](./prefixwhile.md)
  A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [Publishers.TryPrefixWhile](./tryprefixwhile.md)
  A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [Publishers.PrefixUntilOutput](./prefixuntiloutput.md)
  A publisher that republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trydropwhile)*