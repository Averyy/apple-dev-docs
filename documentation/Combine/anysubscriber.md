# AnySubscriber

**Framework**: Combine  
**Kind**: struct

A type-erasing subscriber.

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
@frozen
struct AnySubscriber<Input, Failure> where Failure : Error
```

#### Overview

Use an [`AnySubscriber`](anysubscriber.md) to wrap an existing subscriber whose details you don’t want to expose. You can also use [`AnySubscriber`](anysubscriber.md) to create a custom subscriber by providing closures for the methods defined in [`Subscriber`](subscriber.md), rather than implementing [`Subscriber`](subscriber.md) directly.

## Topics

### Creating a Type-Erased Subscriber
- [init<S>(S)](anysubscriber/init(_:)-2dbfs.md)
  Creates a type-erasing subscriber to wrap an existing subscriber.
- [init(receiveSubscription: ((any Subscription) -> Void)?, receiveValue: ((Input) -> Subscribers.Demand)?, receiveCompletion: ((Subscribers.Completion<Failure>) -> Void)?)](anysubscriber/init(receivesubscription:receivevalue:receivecompletion:).md)
  Creates a type-erasing subscriber that executes the provided closures.
### Receiving Elements
- [func receive(Input) -> Subscribers.Demand](anysubscriber/receive(_:).md)
  Tells the subscriber that the publisher has produced an element.
- [func receive() -> Subscribers.Demand](anysubscriber/receive.md)
  Tells the subscriber that a publisher of void elements is ready to receive further requests.
### Receiving Life Cycle Events
- [func receive(subscription: any Subscription)](anysubscriber/receive(subscription:).md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [func receive(completion: Subscribers.Completion<Failure>)](anysubscriber/receive(completion:).md)
  Tells the subscriber that the publisher has completed publishing, either normally or with an error.
### Inspecting Subscriber Properties
- [let combineIdentifier: CombineIdentifier](anysubscriber/combineidentifier.md)
  A unique identifier for identifying publisher streams.
- [var customMirror: Mirror](anysubscriber/custommirror.md)
  The custom mirror for this instance.
- [var description: String](anysubscriber/description.md)
  A textual representation of this instance.
- [var playgroundDescription: Any](anysubscriber/playgrounddescription.md)
  A custom playground description for this instance.
### Initializers
- [init<S>(S)](anysubscriber/init(_:)-3t3eh.md)
  Creates a type-erasing subscriber to wrap an existing subscriber.
### Default Implementations
- [Subscriber Implementations](anysubscriber/subscriber-implementations.md)

## Relationships

### Conforms To
- [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Subscriber](subscriber.md)

## See Also

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)
  Apply back pressure to precisely control when publishers produce elements.
- [protocol Subscriber](subscriber.md)
  A protocol that declares a type that can receive input from a publisher.
- [enum Subscribers](subscribers.md)
  A namespace for types that serve as subscribers.
- [protocol Subscription](subscription.md)
  A protocol representing the connection of a subscriber to a publisher.
- [enum Subscriptions](subscriptions.md)
  A namespace for symbols related to subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anysubscriber)*