# receive(on:options:)

**Framework**: Combine  
**Kind**: method

Specifies the scheduler on which to receive elements from the publisher.

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
func receive<S>(on scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.ReceiveOn<Self, S> where S : Scheduler
```

#### Return Value

A publisher that delivers elements using the specified scheduler.

#### Discussion

You use the [`receive(on:options:)`](publisher/receive(on:options:).md) operator to receive results and completion on a specific scheduler, such as performing UI work on the main run loop. In contrast with [`subscribe(on:options:)`](publisher/subscribe(on:options:).md), which affects upstream messages, [`receive(on:options:)`](publisher/receive(on:options:).md) changes the execution context of downstream messages.

In the following example, the [`subscribe(on:options:)`](publisher/subscribe(on:options:).md) operator causes `jsonPublisher` to receive requests on `backgroundQueue`, while the [`receive(on:options:)`](publisher/receive(on:options:).md) causes `labelUpdater` to receive elements and completion on `RunLoop.main`.

```swift
let jsonPublisher = MyJSONLoaderPublisher() // Some publisher.
let labelUpdater = MyLabelUpdateSubscriber() // Some subscriber that updates the UI.

jsonPublisher
    .subscribe(on: backgroundQueue)
    .receive(on: RunLoop.main)
    .subscribe(labelUpdater)
```

Prefer [`receive(on:options:)`](publisher/receive(on:options:).md) over explicit use of dispatch queues when performing work in subscribers. For example, instead of the following pattern:

```swift
pub.sink {
    DispatchQueue.main.async {
        // Do something.
    }
}
```

Use this pattern instead:

```swift
pub.receive(on: DispatchQueue.main).sink {
    // Do something.
}
```

> **Note**: [`receive(on:options:)`](publisher/receive(on:options:).md) doesn’t affect the scheduler used to call the subscriber’s [`receive(subscription:)`](subscriber/receive(subscription:).md) method.

## Parameters

- `scheduler`: The scheduler the publisher uses for element delivery.
- `options`: Scheduler options used to customize element delivery.

## See Also

- [func subscribe<S>(on: S, options: S.SchedulerOptions?) -> Publishers.SubscribeOn<Self, S>](publishers/zip4/subscribe(on:options:).md)
  Specifies the scheduler on which to perform subscribe, cancel, and request operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip4/receive(on:options:))*