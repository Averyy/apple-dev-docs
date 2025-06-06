# Publishers.TryMap

**Framework**: Combine  
**Kind**: struct

A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.

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
struct TryMap<Upstream, Output> where Upstream : Publisher
```

## Topics

### Creating a Try Map Publisher
- [init(upstream: Upstream, transform: (Upstream.Output) throws -> Output)](publishers/trymap/init(upstream:transform:).md)
  Creates a publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
### Declaring Publisher Topography
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.TryMap.Failure](publishers/trymap/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/trymap/upstream.md)
  The publisher from which this publisher receives elements.
- [let transform: (Upstream.Output) throws -> Output](publishers/trymap/transform.md)
  The error-throwing closure that transforms elements from the upstream publisher.
### Applying Operators
- [Publisher Operators](publishers-trymap-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/trymap/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Map](publishers/map.md)
  A publisher that transforms all elements from the upstream publisher with a provided closure.
- [Publishers.MapError](publishers/maperror.md)
  A publisher that converts any failure from the upstream publisher into a new error.
- [Publishers.Scan](publishers/scan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [Publishers.TryScan](publishers/tryscan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [Publishers.SetFailureType](publishers/setfailuretype.md)
  A publisher that appears to send a specified failure type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trymap)*