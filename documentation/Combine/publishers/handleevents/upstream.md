# upstream

**Framework**: Combine  
**Kind**: property

The publisher from which this publisher receives elements.

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
let upstream: Upstream
```

## See Also

- [var receiveSubscription: ((any Subscription) -> Void)?](publishers/handleevents/receivesubscription.md)
  A closure that executes when the publisher receives the subscription from the upstream publisher.
- [var receiveOutput: ((Publishers.HandleEvents<Upstream>.Output) -> Void)?](publishers/handleevents/receiveoutput.md)
  A closure that executes when the publisher receives a value from the upstream publisher.
- [var receiveCompletion: ((Subscribers.Completion<Publishers.HandleEvents<Upstream>.Failure>) -> Void)?](publishers/handleevents/receivecompletion.md)
  A closure that executes when the upstream publisher finishes normally or terminates with an error.
- [var receiveCancel: (() -> Void)?](publishers/handleevents/receivecancel.md)
  A closure that executes when the downstream receiver cancels publishing.
- [var receiveRequest: ((Subscribers.Demand) -> Void)?](publishers/handleevents/receiverequest.md)
  A closure that executes when the publisher receives a request for more elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/handleevents/upstream)*