# Publishers.Contains

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.

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
struct Contains<Upstream> where Upstream : Publisher, Upstream.Output : Equatable
```

## Topics

### Creating a contains Publisher
- [init(upstream: Upstream, output: Upstream.Output)](./contains/init%28upstream,output%29.md)
  Creates a publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
### Declaring supporting types
- [Publishers.Contains.Output](./contains/output-swift.typealias.md)
  The kind of values published by this publisher.
- [Publishers.Contains.Failure](./contains/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./contains/upstream.md)
  The publisher from which this publisher receives elements.
- [let output: Upstream.Output](./contains/output-swift.property.md)
  The element to match in the upstream publisher.
### Comparing publishers
- [static func == (Publishers.Contains<Upstream>, Publishers.Contains<Upstream>) -> Bool](./contains/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./contains/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Applying matching criteria to elements
- [Publishers.ContainsWhere](./containswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [Publishers.TryContainsWhere](./trycontainswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [Publishers.AllSatisfy](./allsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [Publishers.TryAllSatisfy](./tryallsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/contains)*