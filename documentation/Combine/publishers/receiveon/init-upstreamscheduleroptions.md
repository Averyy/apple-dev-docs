# init(upstream:scheduler:options:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that delivers elements to its downstream subscriber on a specific scheduler.

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
- `scheduler`: The scheduler the publisher uses to deliver elements.
- `options`: Scheduler options used to customize element delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/receiveon/init(upstream:scheduler:options:))*