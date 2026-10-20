# receiveCompletion

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

A closure that executes when the upstream publisher finishes normally or terminates with an error.

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
var receiveCompletion: ((Subscribers.Completion<Publishers.HandleEvents<Upstream>.Failure>) -> Void)?
```

## See Also

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher from which this publisher receives elements.
- [var receiveSubscription: ((any Subscription) -> Void)?](./receivesubscription.md)
  A closure that executes when the publisher receives the subscription from the upstream publisher.
- [var receiveOutput: ((Publishers.HandleEvents<Upstream>.Output) -> Void)?](./receiveoutput.md)
  A closure that executes when the publisher receives a value from the upstream publisher.
- [var receiveCancel: (() -> Void)?](./receivecancel.md)
  A closure that executes when the downstream receiver cancels publishing.
- [var receiveRequest: ((Subscribers.Demand) -> Void)?](./receiverequest.md)
  A closure that executes when the publisher receives a request for more elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/handleevents/receivecompletion)*