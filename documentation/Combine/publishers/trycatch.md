# Publishers.TryCatch

**Framework**: Combine  
**Kind**: struct

A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.

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
struct TryCatch<Upstream, NewPublisher> where Upstream : Publisher, NewPublisher : Publisher, Upstream.Output == NewPublisher.Output
```

#### Overview

Because this publisher’s handler can throw an error, [`Publishers.TryCatch`](publishers/trycatch.md) defines its [`Failure`](publisher/failure.md) type as `Error`. This is different from [`Publishers.Catch`](publishers/catch.md), which gets its failure type from the replacement publisher.

## Topics

### Creating a Try-Catch Publisher
- [init(upstream: Upstream, handler: (Upstream.Failure) throws -> NewPublisher)](publishers/trycatch/init(upstream:handler:).md)
  Creates a publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or by throwing an error.
### Declaring Publisher Topography
- [Publishers.TryCatch.Output](publishers/trycatch/output.md)
  The kind of values published by this publisher.
- [Publishers.TryCatch.Failure](publishers/trycatch/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/trycatch/upstream.md)
  The publisher from which this publisher receives its elements.
- [let handler: (Upstream.Failure) throws -> NewPublisher](publishers/trycatch/handler.md)
  A closure that accepts the upstream failure as input and either returns a publisher to replace the upstream publisher or throws an error.
### Applying Operators
- [Publisher Operators](publishers-trycatch-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/trycatch/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.AssertNoFailure](publishers/assertnofailure.md)
  A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.
- [Publishers.Catch](publishers/catch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [Publishers.Retry](publishers/retry.md)
  A publisher that attempts to recreate its subscription to a failed upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycatch)*