# init(upstream:receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that performs the specified closures when publisher events occur.

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
init(upstream: Upstream, receiveSubscription: ((any Subscription) -> Void)? = nil, receiveOutput: ((Publishers.HandleEvents<Upstream>.Output) -> Void)? = nil, receiveCompletion: ((Subscribers.Completion<Publishers.HandleEvents<Upstream>.Failure>) -> Void)? = nil, receiveCancel: (() -> Void)? = nil, receiveRequest: ((Subscribers.Demand) -> Void)?)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `receiveSubscription`: A closure that executes when the publisher receives the subscription from the upstream publisher.
- `receiveOutput`: A closure that executes when the publisher receives a value from the upstream publisher.
- `receiveCompletion`: A closure that executes when the publisher receives the completion from the upstream publisher.
- `receiveCancel`: A closure that executes when the downstream receiver cancels publishing.
- `receiveRequest`: A closure that executes when the publisher receives a request for more elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/handleevents/init(upstream:receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:))*