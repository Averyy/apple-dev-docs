# transform

**Framework**: Combine  
**Kind**: property

A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

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
let transform: (Upstream.Output) -> NewPublisher
```

## See Also

- [let upstream: Upstream](publishers/flatmap/upstream.md)
  The publisher from which this publisher receives elements.
- [let maxPublishers: Subscribers.Demand](publishers/flatmap/maxpublishers.md)
  The maximum number of concurrent publisher subscriptions


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/flatmap/transform)*