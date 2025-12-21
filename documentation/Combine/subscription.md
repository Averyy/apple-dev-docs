# Subscription

**Framework**: Combine  
**Kind**: protocol

A protocol representing the connection of a subscriber to a publisher.

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
protocol Subscription : Cancellable, CustomCombineIdentifierConvertible
```

## Mentions

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)
- [Receiving and Handling Events with Combine](receiving-and-handling-events-with-combine.md)

#### Overview

Subscriptions are class constrained because a [`Subscription`](subscription.md) has identity, defined by the moment in time a particular subscriber attached to a publisher. Canceling a [`Subscription`](subscription.md) must be thread-safe.

You can only cancel a [`Subscription`](subscription.md) once.

Canceling a subscription frees up any resources previously allocated by attaching the [`Subscriber`](subscriber.md).

## Topics

### Requesting elements
- [func request(Subscribers.Demand)](subscription/request(_:).md)
  Tells a publisher that it may send more values to the subscriber.
- [Subscribers.Demand](subscribers/demand.md)
  A requested number of items, sent to a publisher from a subscriber through the subscription.

## Relationships

### Inherits From
- [Cancellable](cancellable.md)
- [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md)

## See Also

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)
  Apply back pressure to precisely control when publishers produce elements.
- [protocol Subscriber](subscriber.md)
  A protocol that declares a type that can receive input from a publisher.
- [enum Subscribers](subscribers.md)
  A namespace for types that serve as subscribers.
- [struct AnySubscriber](anysubscriber.md)
  A type-erasing subscriber.
- [enum Subscriptions](subscriptions.md)
  A namespace for symbols related to subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscription)*