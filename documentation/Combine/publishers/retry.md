# Publishers.Retry

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that attempts to recreate its subscription to a failed upstream publisher.

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
struct Retry<Upstream> where Upstream : Publisher
```

## Topics

### Creating a retry publisher
- [init(upstream: Upstream, retries: Int?)](./retry/init%28upstream,retries%29.md)
  Creates a publisher that attempts to recreate its subscription to a failed upstream publisher.
### Declaring supporting types
- [Publishers.Retry.Output](./retry/output.md)
  The kind of values published by this publisher.
- [Publishers.Retry.Failure](./retry/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./retry/upstream.md)
  The publisher from which this publisher receives elements.
- [let retries: Int?](./retry/retries.md)
  The maximum number of retry attempts to perform.
### Comparing publishers
- [static func == (Publishers.Retry<Upstream>, Publishers.Retry<Upstream>) -> Bool](./retry/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./retry/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Handling errors
- [Publishers.AssertNoFailure](./assertnofailure.md)
  A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.
- [Publishers.Catch](./catch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [Publishers.TryCatch](./trycatch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/retry)*