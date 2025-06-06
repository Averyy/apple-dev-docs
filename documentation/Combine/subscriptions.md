# Subscriptions

**Framework**: Combine  
**Kind**: enum

A namespace for symbols related to subscriptions.

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
enum Subscriptions
```

## Topics

### Using Convenience Subscriptions
- [static var empty: any Subscription](subscriptions/empty.md)
  Returns the “empty” subscription.

## See Also

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)
  Apply back pressure to precisely control when publishers produce elements.
- [protocol Subscriber](subscriber.md)
  A protocol that declares a type that can receive input from a publisher.
- [enum Subscribers](subscribers.md)
  A namespace for types that serve as subscribers.
- [struct AnySubscriber](anysubscriber.md)
  A type-erasing subscriber.
- [protocol Subscription](subscription.md)
  A protocol representing the connection of a subscriber to a publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscriptions)*