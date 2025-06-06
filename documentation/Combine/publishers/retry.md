# Publishers.Retry

**Framework**: Combine  
**Kind**: struct

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

### Creating a Retry Publisher
- [init(upstream: Upstream, retries: Int?)](publishers/retry/init(upstream:retries:).md)
  Creates a publisher that attempts to recreate its subscription to a failed upstream publisher.
### Declaring Publisher Topography
- [Publishers.Retry.Output](publishers/retry/output.md)
  The kind of values published by this publisher.
- [Publishers.Retry.Failure](publishers/retry/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/retry/upstream.md)
  The publisher from which this publisher receives elements.
- [let retries: Int?](publishers/retry/retries.md)
  The maximum number of retry attempts to perform.
### Comparing Publishers
- [static func == (Publishers.Retry<Upstream>, Publishers.Retry<Upstream>) -> Bool](publishers/retry/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/retry/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-retry-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](publishers/retry/equatable-implementations.md)
- [Publisher Implementations](publishers/retry/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.AssertNoFailure](publishers/assertnofailure.md)
  A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.
- [Publishers.Catch](publishers/catch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [Publishers.TryCatch](publishers/trycatch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/retry)*