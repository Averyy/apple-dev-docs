# subscribe(on:options:)

**Framework**: Swift  
**Kind**: method

Specifies the scheduler on which to perform subscribe, cancel, and request operations.

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
func subscribe<S>(on scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.SubscribeOn<Self, S> where S : Scheduler
```

#### Return Value

A publisher which performs upstream operations on the specified scheduler.

#### Discussion

In contrast with [`receive(on:options:)`](optional/publisher-swift.struct/receive(on:options:).md), which affects downstream messages, [`subscribe(on:options:)`](optional/publisher-swift.struct/subscribe(on:options:).md) changes the execution context of upstream messages.

In the following example, the [`subscribe(on:options:)`](optional/publisher-swift.struct/subscribe(on:options:).md) operator causes `ioPerformingPublisher` to receive requests on `backgroundQueue`, while the [`receive(on:options:)`](optional/publisher-swift.struct/receive(on:options:).md) causes `uiUpdatingSubscriber` to receive elements and completion on `RunLoop.main`.

```swift
let ioPerformingPublisher == // Some publisher.
let uiUpdatingSubscriber == // Some subscriber that updates the UI.

ioPerformingPublisher
    .subscribe(on: backgroundQueue)
    .receive(on: RunLoop.main)
    .subscribe(uiUpdatingSubscriber)
```

Using [`subscribe(on:options:)`](optional/publisher-swift.struct/subscribe(on:options:).md) also causes the upstream publisher to perform `Cancellable/cancel()` using the specfied scheduler.

## Parameters

- `scheduler`: The scheduler used to send messages to upstream publishers.
- `options`: Options that customize the delivery of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/subscribe(on:options:))*