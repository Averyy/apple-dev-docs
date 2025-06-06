# subscribe(on:options:)

**Framework**: RealityKit  
**Kind**: method

Specifies the scheduler on which to perform subscribe, cancel, and request operations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func subscribe<S>(on scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.SubscribeOn<Self, S> where S : Scheduler
```

#### Return Value

A publisher which performs upstream operations on the specified scheduler.

#### Discussion

In contrast with `Publisher/receive(on:options:)`, which affects downstream messages, `Publisher/subscribe(on:options:)` changes the execution context of upstream messages.

In the following example, the `Publisher/subscribe(on:options:)` operator causes `ioPerformingPublisher` to receive requests on `backgroundQueue`, while the `Publisher/receive(on:options:)` causes `uiUpdatingSubscriber` to receive elements and completion on `RunLoop.main`.

```None
let ioPerformingPublisher == // Some publisher.
let uiUpdatingSubscriber == // Some subscriber that updates the UI.

ioPerformingPublisher
    .subscribe(on: backgroundQueue)
    .receive(on: RunLoop.main)
    .subscribe(uiUpdatingSubscriber)
```

Using `Publisher/subscribe(on:options:)` also causes the upstream publisher to perform `Cancellable/cancel()` using the specfied scheduler.

## Parameters

- `scheduler`: The scheduler used to send messages to upstream publishers.
- `options`: Options that customize the delivery of elements.

## See Also

- [func receive<S>(on: S, options: S.SchedulerOptions?) -> Publishers.ReceiveOn<Self, S>](loadrequest/receive(on:options:).md)
  Specifies the scheduler on which to receive elements from the publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/subscribe(on:options:))*