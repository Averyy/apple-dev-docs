# Subscribers.Sink

**Framework**: Combine  
**Kind**: class

A simple subscriber that requests an unlimited number of values upon subscription.

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
final class Sink<Input, Failure> where Failure : Error
```

## Mentions

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)

## Topics

### Canceling Publication
- [func cancel()](subscribers/sink/cancel.md)
  Cancel the activity.
### Receiving Life Cycle Events
- [func receive(subscription: any Subscription)](subscribers/sink/receive(subscription:).md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.
### Supporting Debugging
- [var combineIdentifier: CombineIdentifier](subscribers/sink/combineidentifier.md)
  A unique identifier for identifying publisher streams.
- [var customMirror: Mirror](subscribers/sink/custommirror.md)
  The custom mirror for this instance.
- [var description: String](subscribers/sink/description.md)
  A textual representation of this instance.
- [var playgroundDescription: Any](subscribers/sink/playgrounddescription.md)
  A custom playground description for this instance.
### Initializers
- [init(receiveCompletion: (Subscribers.Completion<Failure>) -> Void, receiveValue: (Input) -> Void)](subscribers/sink/init(receivecompletion:receivevalue:).md)
  Initializes a sink with the provided closures.
### Instance Properties
- [var receiveCompletion: (Subscribers.Completion<Failure>) -> Void](subscribers/sink/receivecompletion.md)
  The closure to execute on completion.
- [var receiveValue: (Input) -> Void](subscribers/sink/receivevalue.md)
  The closure to execute on receipt of a value.
### Instance Methods
- [func receive(Input) -> Subscribers.Demand](subscribers/sink/receive(_:).md)
  Tells the subscriber that the publisher has produced an element.
- [func receive(completion: Subscribers.Completion<Failure>)](subscribers/sink/receive(completion:).md)
  Tells the subscriber that the publisher has completed publishing, either normally or with an error.
### Default Implementations
- [Cancellable Implementations](subscribers/sink/cancellable-implementations.md)
- [CustomCombineIdentifierConvertible Implementations](subscribers/sink/customcombineidentifierconvertible-implementations.md)
- [Subscriber Implementations](subscribers/sink/subscriber-implementations.md)

## Relationships

### Conforms To
- [Cancellable](cancellable.md)
- [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Subscriber](subscriber.md)

## See Also

- [Subscribers.Assign](subscribers/assign.md)
  A simple subscriber that assigns received elements to a property indicated by a key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/sink)*