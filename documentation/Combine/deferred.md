# Deferred

**Framework**: Combine  
**Kind**: struct

A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.

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
struct Deferred<DeferredPublisher> where DeferredPublisher : Publisher
```

## Topics

### Creating a Deferred Publisher
- [init(createPublisher: () -> DeferredPublisher)](deferred/init(createpublisher:).md)
  Creates a deferred publisher.
### Declaring Publisher Topography
- [typealias Output](deferred/output.md)
  The kind of values published by this publisher.
- [typealias Failure](deferred/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let createPublisher: () -> DeferredPublisher](deferred/createpublisher.md)
  The closure to execute when this deferred publisher receives a subscription.
### Applying Operators
- [Publisher Operators](deferred-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](deferred/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [class Future](future.md)
  A publisher that eventually produces a single value and then finishes or fails.
- [struct Just](just.md)
  A publisher that emits an output to each subscriber just once, and then finishes.
- [struct Empty](empty.md)
  A publisher that never publishes any values, and optionally finishes immediately.
- [struct Fail](fail.md)
  A publisher that immediately terminates with the specified error.
- [struct Record](record.md)
  A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/deferred)*