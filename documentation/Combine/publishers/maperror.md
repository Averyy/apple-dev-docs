# Publishers.MapError

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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

### Creating an error-mapping publisher
- [init(upstream: Upstream, (Upstream.Failure) -> Failure)](./maperror/init%28upstream,_%29.md)
- [init(upstream: Upstream, transform: (Upstream.Failure) -> Failure)](./maperror/init%28upstream,transform%29.md)
  Creates a publisher that converts any failure from the upstream publisher into a new error.
### Declaring supporting types
- [Publishers.MapError.Output](./maperror/output.md)
  The kind of values published by this publisher.
### Inspecting publisher properties
- [let upstream: Upstream](./maperror/upstream.md)
  The publisher from which this publisher receives elements.
- [let transform: (Upstream.Failure) -> Failure](./maperror/transform.md)
  The closure that converts the upstream failure into a new error.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Mapping elements
- [Publishers.Map](./map.md)
  A publisher that transforms all elements from the upstream publisher with a provided closure.
- [Publishers.TryMap](./trymap.md)
  A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [Publishers.Scan](./scan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [Publishers.TryScan](./tryscan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [Publishers.SetFailureType](./setfailuretype.md)
  A publisher that appears to send a specified failure type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/maperror)*