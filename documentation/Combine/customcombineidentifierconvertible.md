# CustomCombineIdentifierConvertible

**Framework**: Combine  
**Kind**: protocol

A protocol for uniquely identifying publisher streams.

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
protocol CustomCombineIdentifierConvertible
```

#### Overview

If you create a custom [`Subscription`](subscription.md) or [`Subscriber`](subscriber.md) type, implement this protocol so that development tools can uniquely identify publisher chains in your app. If your type is a class, Combine provides an implementation of [`combineIdentifier`](customcombineidentifierconvertible/combineidentifier.md) for you. If your type is a structure, set up the identifier as follows:

```swift
let combineIdentifier = CombineIdentifier()
```

## Topics

### Identifying publisher streams
- [var combineIdentifier: CombineIdentifier](customcombineidentifierconvertible/combineidentifier.md)
  A unique identifier for identifying publisher streams.

## Relationships

### Inherited By
- [Subscriber](subscriber.md)
- [Subscription](subscription.md)
### Conforming Types
- [AnySubscriber](anysubscriber.md)
- [Subscribers.Assign](subscribers/assign.md)
- [Subscribers.Sink](subscribers/sink.md)

## See Also

- [struct CombineIdentifier](combineidentifier.md)
  A unique identifier for identifying publisher streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/customcombineidentifierconvertible)*