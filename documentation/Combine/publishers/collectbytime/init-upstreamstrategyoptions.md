# init(upstream:strategy:options:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that buffers and periodically publishes its items.

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
init(upstream: Upstream, strategy: Publishers.TimeGroupingStrategy<Context>, options: Context.SchedulerOptions?)
```

## Parameters

- `upstream`: The publisher that this publisher receives elements from.
- `strategy`: The strategy with which to collect and publish elements.
- `options`:   options to use for the strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/collectbytime/init(upstream:strategy:options:))*