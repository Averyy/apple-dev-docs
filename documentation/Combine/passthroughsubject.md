# PassthroughSubject

**Framework**: Combine  
**Kind**: class

A subject that broadcasts elements to downstream subscribers.

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
final class PassthroughSubject<Output, Failure> where Failure : Error
```

## Mentions

- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

#### Overview

As a concrete implementation of [`Subject`](subject.md), the [`PassthroughSubject`](passthroughsubject.md) provides a convenient way to adapt existing imperative code to the Combine model.

Unlike [`CurrentValueSubject`](currentvaluesubject.md), a [`PassthroughSubject`](passthroughsubject.md) doesn’t have an initial value or a buffer of the most recently-published element. A [`PassthroughSubject`](passthroughsubject.md) drops values if there are no subscribers, or its current demand is zero.

## Topics

### Creating a Passthrough Subject
- [init()](passthroughsubject/init.md)
### Delivering Elements to Subscribers
- [func send(Output)](passthroughsubject/send(_:).md)
  Sends a value to the subscriber.
- [func send()](passthroughsubject/send.md)
  Sends a void value to the subscriber.
### Delivering Life Cycle Events to Subscribers
- [func send(subscription: any Subscription)](passthroughsubject/send(subscription:).md)
  Sends a subscription to the subscriber.
- [func send(completion: Subscribers.Completion<Failure>)](passthroughsubject/send(completion:).md)
  Sends a completion signal to the subscriber.
### Applying Operators
- [Publisher Operators](passthroughsubject-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](passthroughsubject/publisher-implementations.md)
- [Subject Implementations](passthroughsubject/subject-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)
- [Subject](subject.md)

## See Also

- [protocol Subject](subject.md)
  A publisher that exposes a method for outside callers to publish elements.
- [class CurrentValueSubject](currentvaluesubject.md)
  A subject that wraps a single value and publishes a new element whenever the value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/passthroughsubject)*