# maxPublishers

**Framework**: Combine  
**Kind**: property

The maximum number of concurrent publisher subscriptions

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
let maxPublishers: Subscribers.Demand
```

## See Also

- [let upstream: Upstream](publishers/flatmap/upstream.md)
  The publisher from which this publisher receives elements.
- [let transform: (Upstream.Output) -> NewPublisher](publishers/flatmap/transform.md)
  A closure that takes an element as a parameter and returns a publisher that produces elements of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/flatmap/maxpublishers)*