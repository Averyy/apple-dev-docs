# Publishers.TryContainsWhere

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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
- [init(upstream: Upstream, predicate: (Upstream.Output) throws -> Bool)](./trycontainswhere/init%28upstream,predicate%29.md)
  Creates a publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
### Declaring supporting types
- [Publishers.TryContainsWhere.Output](./trycontainswhere/output.md)
  The kind of values published by this publisher.
- [Publishers.TryContainsWhere.Failure](./trycontainswhere/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./trycontainswhere/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Upstream.Output) throws -> Bool](./trycontainswhere/predicate.md)
  The error-throwing closure that determines whether this publisher should emit a Boolean true element.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Applying matching criteria to elements
- [Publishers.Contains](./contains.md)
  A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [Publishers.ContainsWhere](./containswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [Publishers.AllSatisfy](./allsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [Publishers.TryAllSatisfy](./tryallsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycontainswhere)*