# Publishers.MapKeyPath2

**Framework**: Combine  
**Kind**: struct

A publisher that publishes the values of two key paths as a tuple.

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
struct MapKeyPath2<Upstream, Output0, Output1> where Upstream : Publisher
```

## Topics

### Declaring supporting types
- [Publishers.MapKeyPath2.Output](publishers/mapkeypath2/output.md)
  The kind of values published by this publisher.
- [Publishers.MapKeyPath2.Failure](publishers/mapkeypath2/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/mapkeypath2/upstream.md)
  The publisher from which this publisher receives elements.
- [let keyPath0: KeyPath<Upstream.Output, Output0>](publishers/mapkeypath2/keypath0.md)
  The key path of a property to publish.
- [let keyPath1: KeyPath<Upstream.Output, Output1>](publishers/mapkeypath2/keypath1.md)
  The key path of a second property to publish.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.MapKeyPath](publishers/mapkeypath.md)
  A publisher that publishes the value of a key path.
- [Publishers.MapKeyPath3](publishers/mapkeypath3.md)
  A publisher that publishes the values of three key paths as a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/mapkeypath2)*