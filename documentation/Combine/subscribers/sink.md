# Subscribers.Sink

**Framework**: Combine  
**Kind**: class  
**Role**: Class

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

- [Processing Published Elements with Subscribers](../processing-published-elements-with-subscribers.md)

## Topics

### Creating a sink subscriber
- [init(receiveCompletion: (Subscribers.Completion<Failure>) -> Void, receiveValue: (Input) -> Void)](./sink/init%28receivecompletion,receivevalue%29.md)
  Initializes a sink with the provided closures.
### Inspecting subscriber properties
- [var receiveValue: (Input) -> Void](./sink/receivevalue.md)
  The closure to execute on receipt of a value.
- [var receiveCompletion: (Subscribers.Completion<Failure>) -> Void](./sink/receivecompletion.md)
  The closure to execute on completion.

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
- [Subscribers.Assign](./assign.md)
  A simple subscriber that assigns received elements to a property indicated by a key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/sink)*