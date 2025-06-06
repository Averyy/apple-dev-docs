# init(upstream:interval:scheduler:latest:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.

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
init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, scheduler: Context, latest: Bool)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `interval`: The interval in which to find and emit the most recent element.
- `scheduler`: The scheduler on which to publish elements.
- `latest`: A Boolean value indicating whether to publish the most recent element. If  , the publisher emits the first element received during the interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/throttle/init(upstream:interval:scheduler:latest:))*