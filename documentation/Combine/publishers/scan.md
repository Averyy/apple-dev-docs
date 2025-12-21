# Publishers.Scan

**Framework**: Combine  
**Kind**: struct

A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.

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
struct Scan<Upstream, Output> where Upstream : Publisher
```

## Topics

### Creating a scan publisher
- [init(upstream: Upstream, initialResult: Output, nextPartialResult: (Output, Upstream.Output) -> Output)](publishers/scan/init(upstream:initialresult:nextpartialresult:).md)
  Creates a publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
### Declaring supporting types
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.Scan.Failure](publishers/scan/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/scan/upstream.md)
  The publisher that this publisher receives elements from.
- [let initialResult: Output](publishers/scan/initialresult.md)
  The previous result returned by the `nextPartialResult` closure.
- [let nextPartialResult: (Output, Upstream.Output) -> Output](publishers/scan/nextpartialresult.md)
  An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Map](publishers/map.md)
  A publisher that transforms all elements from the upstream publisher with a provided closure.
- [Publishers.TryMap](publishers/trymap.md)
  A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [Publishers.MapError](publishers/maperror.md)
  A publisher that converts any failure from the upstream publisher into a new error.
- [Publishers.TryScan](publishers/tryscan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [Publishers.SetFailureType](publishers/setfailuretype.md)
  A publisher that appears to send a specified failure type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/scan)*