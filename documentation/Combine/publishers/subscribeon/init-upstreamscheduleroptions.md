# init(upstream:scheduler:options:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that receives elements from an upstream publisher on a specific scheduler.

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
init(upstream: Upstream, scheduler: Context, options: Context.SchedulerOptions?)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `scheduler`: The scheduler the publisher should use to receive elements.
- `options`: Scheduler options that customize the delivery of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/subscribeon/init(upstream:scheduler:options:))*