# Publishers.TryContainsWhere

**Framework**: Combine  
**Kind**: struct

A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.

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
struct TryContainsWhere<Upstream> where Upstream : Publisher
```

## Topics

### Creating a try-contains-where publisher
- [init(upstream: Upstream, predicate: (Upstream.Output) throws -> Bool)](publishers/trycontainswhere/init(upstream:predicate:).md)
  Creates a publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
### Declaring supporting types
- [Publishers.TryContainsWhere.Output](publishers/trycontainswhere/output.md)
  The kind of values published by this publisher.
- [Publishers.TryContainsWhere.Failure](publishers/trycontainswhere/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/trycontainswhere/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Upstream.Output) throws -> Bool](publishers/trycontainswhere/predicate.md)
  The error-throwing closure that determines whether this publisher should emit a Boolean true element.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Contains](publishers/contains.md)
  A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [Publishers.ContainsWhere](publishers/containswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [Publishers.AllSatisfy](publishers/allsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [Publishers.TryAllSatisfy](publishers/tryallsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycontainswhere)*