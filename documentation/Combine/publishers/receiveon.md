# Publishers.ReceiveOn

**Framework**: Combine  
**Kind**: struct

A publisher that delivers elements to its downstream subscriber on a specific scheduler.

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
struct ReceiveOn<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Topics

### Creating a receive-on Publisher
- [init(upstream: Upstream, scheduler: Context, options: Context.SchedulerOptions?)](publishers/receiveon/init(upstream:scheduler:options:).md)
  Creates a publisher that delivers elements to its downstream subscriber on a specific scheduler.
### Declaring supporting types
- [Publishers.ReceiveOn.Output](publishers/receiveon/output.md)
  The kind of values published by this publisher.
- [Publishers.ReceiveOn.Failure](publishers/receiveon/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/receiveon/upstream.md)
  The publisher from which this publisher receives elements.
- [let scheduler: Context](publishers/receiveon/scheduler.md)
  The scheduler the publisher uses to deliver elements.
- [let options: Context.SchedulerOptions?](publishers/receiveon/options.md)
  Scheduler options used to customize element delivery.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.SubscribeOn](publishers/subscribeon.md)
  A publisher that receives elements from an upstream publisher on a specific scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/receiveon)*