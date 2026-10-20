# Publishers.Catch

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.

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
struct Catch<Upstream, NewPublisher> where Upstream : Publisher, NewPublisher : Publisher, Upstream.Output == NewPublisher.Output
```

## Topics

### Creating a catch publisher
- [init(upstream: Upstream, handler: (Upstream.Failure) -> NewPublisher)](./catch/init%28upstream,handler%29.md)
  Creates a publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
### Declaring supporting types
- [Publishers.Catch.Output](./catch/output.md)
  The kind of values published by this publisher.
- [Publishers.Catch.Failure](./catch/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./catch/upstream.md)
  The publisher from which this publisher receives its elements.
- [let handler: (Upstream.Failure) -> NewPublisher](./catch/handler.md)
  A closure that accepts the upstream failure as input and returns a publisher to replace the upstream publisher.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Convenience publishers
- [Publishers.Sequence](./sequence.md)
  A publisher that publishes a given sequence of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/catch)*