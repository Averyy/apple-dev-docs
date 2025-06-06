# Subscribers.Assign

**Framework**: Combine  
**Kind**: class

A simple subscriber that assigns received elements to a property indicated by a key path.

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
final class Assign<Root, Input>
```

## Mentions

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)

## Topics

### Declaring Subscriber Topography
- [Subscribers.Assign.Failure](subscribers/assign/failure.md)
  The kind of errors this subscriber might receive.
### Creating an Assign Subscriber
- [init(object: Root, keyPath: ReferenceWritableKeyPath<Root, Input>)](subscribers/assign/init(object:keypath:).md)
  Creates a subscriber to assign the value of a property indicated by a key path.
### Declaring Publisher Topography
- [Subscribers.Assign.Failure](subscribers/assign/failure.md)
  The kind of errors this subscriber might receive.
### Inspecting the Assigned Property
- [var object: Root?](subscribers/assign/object.md)
  The object that contains the property to assign.
- [let keyPath: ReferenceWritableKeyPath<Root, Input>](subscribers/assign/keypath.md)
  The key path that indicates the property to assign.
### Instance Properties
- [var customMirror: Mirror](subscribers/assign/custommirror.md)
  A mirror that reflects the subscriber.
- [var description: String](subscribers/assign/description.md)
  A textual representation of this subscriber.
- [var playgroundDescription: Any](subscribers/assign/playgrounddescription.md)
  A custom playground description for this subscriber.
### Instance Methods
- [func cancel()](subscribers/assign/cancel.md)
  Cancel the activity.
- [func receive(Input) -> Subscribers.Demand](subscribers/assign/receive(_:).md)
  Tells the subscriber that the publisher has produced an element.
- [func receive(completion: Subscribers.Completion<Never>)](subscribers/assign/receive(completion:).md)
  Tells the subscriber that the publisher has completed publishing, either normally or with an error.
- [func receive(subscription: any Subscription)](subscribers/assign/receive(subscription:).md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.
### Default Implementations
- [Cancellable Implementations](subscribers/assign/cancellable-implementations.md)
- [CustomCombineIdentifierConvertible Implementations](subscribers/assign/customcombineidentifierconvertible-implementations.md)
- [Subscriber Implementations](subscribers/assign/subscriber-implementations.md)

## Relationships

### Conforms To
- [Cancellable](cancellable.md)
- [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Subscriber](subscriber.md)

## See Also

- [Subscribers.Sink](subscribers/sink.md)
  A simple subscriber that requests an unlimited number of values upon subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/assign)*