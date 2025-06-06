# Publishers.ContainsWhere

**Framework**: Combine  
**Kind**: struct

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

### Creating a Contains Where Publisher
- [init(upstream: Upstream, predicate: (Upstream.Output) -> Bool)](publishers/containswhere/init(upstream:predicate:).md)
  Creates a publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
### Declaring Publisher Topography
- [Publishers.ContainsWhere.Output](publishers/containswhere/output.md)
  The kind of values published by this publisher.
- [Publishers.ContainsWhere.Failure](publishers/containswhere/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/containswhere/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Upstream.Output) -> Bool](publishers/containswhere/predicate.md)
  The closure that determines whether the publisher should consider an element as a match.
### Applying Operators
- [Publisher Operators](publishers-containswhere-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/containswhere/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Contains](publishers/contains.md)
  A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [Publishers.TryContainsWhere](publishers/trycontainswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [Publishers.AllSatisfy](publishers/allsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [Publishers.TryAllSatisfy](publishers/tryallsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/containswhere)*