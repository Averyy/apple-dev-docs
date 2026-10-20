# upstream

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The publisher from which this publisher receives elements.

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
let upstream: Upstream
```

## See Also

### Inspecting publisher properties
- [let maxPublishers: Subscribers.Demand](./maxpublishers.md)
  The maximum number of concurrent publisher subscriptions
- [let transform: (Upstream.Output) -> NewPublisher](./transform.md)
  A closure that takes an element as a parameter and returns a publisher that produces elements of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/flatmap/upstream)*