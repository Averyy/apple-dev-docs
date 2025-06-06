# Publishers.MapError

**Framework**: Combine  
**Kind**: struct

A publisher that converts any failure from the upstream publisher into a new error.

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
struct MapError<Upstream, Failure> where Upstream : Publisher, Failure : Error
```

## Topics

### Creating a Map Error Publisher
- [init(upstream: Upstream, (Upstream.Failure) -> Failure)](publishers/maperror/init(upstream:_:).md)
- [init(upstream: Upstream, transform: (Upstream.Failure) -> Failure)](publishers/maperror/init(upstream:transform:).md)
  Creates a publisher that converts any failure from the upstream publisher into a new error.
### Declaring Publisher Topography
- [Publishers.MapError.Output](publishers/maperror/output.md)
  The kind of values published by this publisher.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/maperror/upstream.md)
  The publisher from which this publisher receives elements.
- [let transform: (Upstream.Failure) -> Failure](publishers/maperror/transform.md)
  The closure that converts the upstream failure into a new error.
### Applying Operators
- [Publisher Operators](publishers-maperror-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/maperror/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Map](publishers/map.md)
  A publisher that transforms all elements from the upstream publisher with a provided closure.
- [Publishers.TryMap](publishers/trymap.md)
  A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [Publishers.Scan](publishers/scan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [Publishers.TryScan](publishers/tryscan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [Publishers.SetFailureType](publishers/setfailuretype.md)
  A publisher that appears to send a specified failure type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/maperror)*