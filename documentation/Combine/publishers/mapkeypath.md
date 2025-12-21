# Publishers.MapKeyPath

**Framework**: Combine  
**Kind**: struct

A publisher that publishes the value of a key path.

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
struct MapKeyPath<Upstream, Output> where Upstream : Publisher
```

## Topics

### Declaring supporting types
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.MapKeyPath.Failure](publishers/mapkeypath/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/mapkeypath/upstream.md)
  The publisher from which this publisher receives elements.
- [let keyPath: KeyPath<Upstream.Output, Output>](publishers/mapkeypath/keypath.md)
  The key path of a property to publish.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.MapKeyPath2](publishers/mapkeypath2.md)
  A publisher that publishes the values of two key paths as a tuple.
- [Publishers.MapKeyPath3](publishers/mapkeypath3.md)
  A publisher that publishes the values of three key paths as a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/mapkeypath)*