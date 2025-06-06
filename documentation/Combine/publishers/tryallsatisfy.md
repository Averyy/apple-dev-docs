# Publishers.TryAllSatisfy

**Framework**: Combine  
**Kind**: struct

A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

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
struct TryAllSatisfy<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Try All Satisfy Publisher
- [init(upstream: Upstream, predicate: (Upstream.Output) throws -> Bool)](publishers/tryallsatisfy/init(upstream:predicate:).md)
  Returns a publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
### Declaring Publisher Topography
- [Publishers.TryAllSatisfy.Output](publishers/tryallsatisfy/output.md)
  The kind of values published by this publisher.
- [Publishers.TryAllSatisfy.Failure](publishers/tryallsatisfy/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/tryallsatisfy/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Upstream.Output) throws -> Bool](publishers/tryallsatisfy/predicate.md)
  A closure that evaluates each received element.
### Applying Operators
- [Publisher Operators](publishers-tryallsatisfy-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/tryallsatisfy/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Contains](publishers/contains.md)
  A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [Publishers.ContainsWhere](publishers/containswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [Publishers.TryContainsWhere](publishers/trycontainswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [Publishers.AllSatisfy](publishers/allsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryallsatisfy)*