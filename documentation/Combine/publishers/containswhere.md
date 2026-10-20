# Publishers.ContainsWhere

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.

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
struct ContainsWhere<Upstream> where Upstream : Publisher
```

## Topics

### Creating a contains where publisher
- [init(upstream: Upstream, predicate: (Upstream.Output) -> Bool)](./containswhere/init%28upstream,predicate%29.md)
  Creates a publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
### Declaring supporting types
- [Publishers.ContainsWhere.Output](./containswhere/output.md)
  The kind of values published by this publisher.
- [Publishers.ContainsWhere.Failure](./containswhere/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./containswhere/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Upstream.Output) -> Bool](./containswhere/predicate.md)
  The closure that determines whether the publisher should consider an element as a match.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Applying matching criteria to elements
- [Publishers.Contains](./contains.md)
  A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [Publishers.TryContainsWhere](./trycontainswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [Publishers.AllSatisfy](./allsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [Publishers.TryAllSatisfy](./tryallsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/containswhere)*