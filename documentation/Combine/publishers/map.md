# Publishers.Map

**Framework**: Combine  
**Kind**: struct

A publisher that transforms all elements from the upstream publisher with a provided closure.

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
struct Map<Upstream, Output> where Upstream : Publisher
```

## Topics

### Creating a map publisher
- [init(upstream: Upstream, transform: (Upstream.Output) -> Output)](publishers/map/init(upstream:transform:).md)
  Creates a publisher that transforms all elements from the upstream publisher with a provided closure.
### Mapping elements
- [func map<T>((Output) -> T) -> Publishers.Map<Upstream, T>](publishers/map/map(_:).md)
- [func tryMap<T>((Output) throws -> T) -> Publishers.TryMap<Upstream, T>](publishers/map/trymap(_:).md)
### Declaring supporting types
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.Map.Failure](publishers/map/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/map/upstream.md)
  The publisher from which this publisher receives elements.
- [let transform: (Upstream.Output) -> Output](publishers/map/transform.md)
  The closure that transforms elements from the upstream publisher.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.TryMap](publishers/trymap.md)
  A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [Publishers.MapError](publishers/maperror.md)
  A publisher that converts any failure from the upstream publisher into a new error.
- [Publishers.Scan](publishers/scan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [Publishers.TryScan](publishers/tryscan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [Publishers.SetFailureType](publishers/setfailuretype.md)
  A publisher that appears to send a specified failure type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/map)*