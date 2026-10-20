# Publishers.HandleEvents

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that performs the specified closures when publisher events occur.

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
struct HandleEvents<Upstream> where Upstream : Publisher
```

## Topics

### Creating an event-handling publisher
- [init(upstream: Upstream, receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Publishers.HandleEvents<Upstream>.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Publishers.HandleEvents<Upstream>.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?)](./handleevents/init%28upstream,receivesubscription,receiveoutput,receivecompletion,receivecancel,receiverequest%29.md)
  Creates a publisher that performs the specified closures when publisher events occur.
### Declaring supporting types
- [Publishers.HandleEvents.Output](./handleevents/output.md)
  The kind of values published by this publisher.
- [Publishers.HandleEvents.Failure](./handleevents/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./handleevents/upstream.md)
  The publisher from which this publisher receives elements.
- [var receiveSubscription: ((any Subscription) -> Void)?](./handleevents/receivesubscription.md)
  A closure that executes when the publisher receives the subscription from the upstream publisher.
- [var receiveOutput: ((Publishers.HandleEvents<Upstream>.Output) -> Void)?](./handleevents/receiveoutput.md)
  A closure that executes when the publisher receives a value from the upstream publisher.
- [var receiveCompletion: ((Subscribers.Completion<Publishers.HandleEvents<Upstream>.Failure>) -> Void)?](./handleevents/receivecompletion.md)
  A closure that executes when the upstream publisher finishes normally or terminates with an error.
- [var receiveCancel: (() -> Void)?](./handleevents/receivecancel.md)
  A closure that executes when the downstream receiver cancels publishing.
- [var receiveRequest: ((Subscribers.Demand) -> Void)?](./handleevents/receiverequest.md)
  A closure that executes when the publisher receives a request for more elements.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Debugging
- [Publishers.Breakpoint](./breakpoint.md)
  A publisher that raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [Publishers.Print](./print.md)
  A publisher that prints log messages for all publishing events, optionally prefixed with a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/handleevents)*