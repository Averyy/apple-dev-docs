# Subject

**Framework**: Combine  
**Kind**: protocol

A publisher that exposes a method for outside callers to publish elements.

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
protocol Subject<Output, Failure> : AnyObject, Publisher
```

## Mentions

- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

#### Overview

A subject is a publisher that you can use to ”inject” values into a stream, by calling its [`send(_:)`](subject/send(_:).md) method. This can be useful for adapting existing imperative code to the Combine model.

## Topics

### Delivering elements to subscribers
- [func send(Self.Output)](subject/send(_:).md)
  Sends a value to the subscriber.
- [func send()](subject/send.md)
  Sends a void value to the subscriber.
### Delivering life cycle events to subscribers
- [func send(subscription: any Subscription)](subject/send(subscription:).md)
  Sends a subscription to the subscriber.
- [func send(completion: Subscribers.Completion<Self.Failure>)](subject/send(completion:).md)
  Sends a completion signal to the subscriber.

## Relationships

### Inherits From
- [Publisher](publisher.md)
### Conforming Types
- [CurrentValueSubject](currentvaluesubject.md)
- [PassthroughSubject](passthroughsubject.md)

## See Also

- [class CurrentValueSubject](currentvaluesubject.md)
  A subject that wraps a single value and publishes a new element whenever the value changes.
- [class PassthroughSubject](passthroughsubject.md)
  A subject that broadcasts elements to downstream subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subject)*