# CurrentValueSubject

**Framework**: Combine  
**Kind**: class

A subject that wraps a single value and publishes a new element whenever the value changes.

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
final class CurrentValueSubject<Output, Failure> where Failure : Error
```

## Mentions

- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

#### Overview

Unlike [`PassthroughSubject`](passthroughsubject.md), [`CurrentValueSubject`](currentvaluesubject.md) maintains a buffer of the most recently published element.

Calling [`send(_:)`](currentvaluesubject/send(_:).md) on a [`CurrentValueSubject`](currentvaluesubject.md) also updates the current value, making it equivalent to updating the [`value`](currentvaluesubject/value.md) directly.

## Topics

### Creating a Current Value Subject
- [init(Output)](currentvaluesubject/init(_:).md)
  Creates a current value subject with the given initial value.
### Accessing the Current Value
- [var value: Output](currentvaluesubject/value.md)
  The value wrapped by this subject, published as a new element whenever it changes.
### Delivering Elements to Subscribers
- [func send(Output)](currentvaluesubject/send(_:).md)
  Sends a value to the subscriber.
- [func send()](currentvaluesubject/send.md)
  Sends a void value to the subscriber.
### Delivering Life Cycle Events to Subscribers
- [func send(subscription: any Subscription)](currentvaluesubject/send(subscription:).md)
  Sends a subscription to the subscriber.
- [func send(completion: Subscribers.Completion<Failure>)](currentvaluesubject/send(completion:).md)
  Sends a completion signal to the subscriber.
### Applying Operators
- [Publisher Operators](currentvaluesubject-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](currentvaluesubject/publisher-implementations.md)
- [Subject Implementations](currentvaluesubject/subject-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)
- [Subject](subject.md)

## See Also

- [protocol Subject](subject.md)
  A publisher that exposes a method for outside callers to publish elements.
- [class PassthroughSubject](passthroughsubject.md)
  A subject that broadcasts elements to downstream subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/currentvaluesubject)*