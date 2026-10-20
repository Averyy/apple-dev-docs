# Subscribers.Assign

**Framework**: Combine  
**Kind**: class  
**Role**: Class

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

- [Processing Published Elements with Subscribers](../processing-published-elements-with-subscribers.md)

## Topics

### Creating an assign subscriber
- [init(object: Root, keyPath: ReferenceWritableKeyPath<Root, Input>)](./assign/init%28object,keypath%29.md)
  Creates a subscriber to assign the value of a property indicated by a key path.
### Receiving elements
- [func receive(Input) -> Subscribers.Demand](./assign/receive%28_%29.md)
  Tells the subscriber that the publisher has produced an element.
### Receiving life cycle events
- [func receive(subscription: any Subscription)](./assign/receive%28subscription%29.md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [func receive(completion: Subscribers.Completion<Never>)](./assign/receive%28completion%29.md)
  Tells the subscriber that the publisher has completed publishing, either normally or with an error.
### Inspecting the assigned property
- [var object: Root?](./assign/object.md)
  The object that contains the property to assign.
- [let keyPath: ReferenceWritableKeyPath<Root, Input>](./assign/keypath.md)
  The key path that indicates the property to assign.
### Supporting Debugging
- [var customMirror: Mirror](./assign/custommirror.md)
  A mirror that reflects the subscriber.
- [var description: String](./assign/description.md)
  A textual representation of this subscriber.
- [var playgroundDescription: Any](./assign/playgrounddescription.md)
  A custom playground description for this subscriber.
### Instance Methods
- [func cancel()](./assign/cancel%28%29.md)
  Cancel the activity.

## Relationships

### Conforms To
- [Cancellable](../cancellable.md)
- [CustomCombineIdentifierConvertible](../customcombineidentifierconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomReflectable](../../Swift/customreflectable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Subscriber](../subscriber.md)

## See Also

### Using convenience subscribers
- [Subscribers.Sink](./sink.md)
  A simple subscriber that requests an unlimited number of values upon subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/assign)*