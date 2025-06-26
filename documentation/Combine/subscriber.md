# Subscriber

**Framework**: Combine  
**Kind**: protocol

A protocol that declares a type that can receive input from a publisher.

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
protocol Subscriber<Input, Failure> : CustomCombineIdentifierConvertible
```

## Mentions

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)
- [Receiving and Handling Events with Combine](receiving-and-handling-events-with-combine.md)
- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md)
- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

#### Overview

A [`Subscriber`](subscriber.md) instance receives a stream of elements from a [`Publisher`](publisher.md), along with life cycle events describing changes to their relationship. A given subscriber’s [`Input`](subscriber/input.md) and [`Failure`](subscriber/failure.md) associated types must match the [`Output`](publisher/output.md) and [`Failure`](publisher/failure.md) of its corresponding publisher.

You connect a subscriber to a publisher by calling the publisher’s [`subscribe(_:)`](publisher/subscribe(_:)-4u8kn.md) method.  After making this call, the publisher invokes the subscriber’s [`receive(subscription:)`](subscriber/receive(subscription:).md) method. This gives the subscriber a [`Subscription`](subscription.md) instance, which it uses to demand elements from the publisher, and to optionally cancel the subscription. After the subscriber makes an initial demand, the publisher calls [`receive(_:)`](subscriber/receive(_:).md), possibly asynchronously, to deliver newly-published elements. If the publisher stops publishing, it calls [`receive(completion:)`](subscriber/receive(completion:).md), using a parameter of type [`Subscribers.Completion`](subscribers/completion.md) to indicate whether publishing completes normally or with an error.

Combine provides the following subscribers as operators on the [`Publisher`](publisher.md) type:

- [`sink(receiveCompletion:receiveValue:)`](publisher/sink(receivecompletion:receivevalue:).md) executes arbitrary closures when it receives a completion signal and each time it receives a new element.
- [`assign(to:on:)`](publisher/assign(to:on:).md) writes each newly-received value to a property identified by a key path on a given instance.

## Topics

### Declaring Subscriber Topography
- [associatedtype Input](subscriber/input.md)
  The kind of values this subscriber receives.
- [associatedtype Failure : Error](subscriber/failure.md)
  The kind of errors this subscriber might receive.
### Receiving Elements
- [func receive(Self.Input) -> Subscribers.Demand](subscriber/receive(_:).md)
  Tells the subscriber that the publisher has produced an element.
- [func receive() -> Subscribers.Demand](subscriber/receive.md)
  Tells the subscriber that a publisher of void elements is ready to receive further requests.
### Receiving Life Cycle Events
- [func receive(subscription: any Subscription)](subscriber/receive(subscription:).md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [func receive(completion: Subscribers.Completion<Self.Failure>)](subscriber/receive(completion:).md)
  Tells the subscriber that the publisher has completed publishing, either normally or with an error.
- [Subscribers.Completion](subscribers/completion.md)
  A signal that a publisher doesn’t produce additional elements, either due to normal completion or an error.

## Relationships

### Inherits From
- [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md)
### Conforming Types
- [AnySubscriber](anysubscriber.md)
- [Subscribers.Assign](subscribers/assign.md)
- [Subscribers.Sink](subscribers/sink.md)

## See Also

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)
  Apply back pressure to precisely control when publishers produce elements.
- [enum Subscribers](subscribers.md)
  A namespace for types that serve as subscribers.
- [struct AnySubscriber](anysubscriber.md)
  A type-erasing subscriber.
- [protocol Subscription](subscription.md)
  A protocol representing the connection of a subscriber to a publisher.
- [enum Subscriptions](subscriptions.md)
  A namespace for symbols related to subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscriber)*