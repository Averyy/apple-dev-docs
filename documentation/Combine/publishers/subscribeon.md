# Publishers.SubscribeOn

**Framework**: Combine  
**Kind**: struct

A publisher that receives elements from an upstream publisher on a specific scheduler.

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
struct SubscribeOn<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Topics

### Creating a Subscribe-On Publisher
- [init(upstream: Upstream, scheduler: Context, options: Context.SchedulerOptions?)](publishers/subscribeon/init(upstream:scheduler:options:).md)
  Creates a publisher that receives elements from an upstream publisher on a specific scheduler.
### Declaring Publisher Topography
- [Publishers.SubscribeOn.Output](publishers/subscribeon/output.md)
  The kind of values published by this publisher.
- [Publishers.SubscribeOn.Failure](publishers/subscribeon/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/subscribeon/upstream.md)
  The publisher from which this publisher receives elements.
- [let scheduler: Context](publishers/subscribeon/scheduler.md)
  The scheduler the publisher should use to receive elements.
- [let options: Context.SchedulerOptions?](publishers/subscribeon/options.md)
  Scheduler options that customize the delivery of elements.
### Applying Operators
- [Publisher Operators](publishers-subscribeon-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/subscribeon/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.ReceiveOn](publishers/receiveon.md)
  A publisher that delivers elements to its downstream subscriber on a specific scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/subscribeon)*