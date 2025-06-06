# receive()

**Framework**: Combine  
**Kind**: method

Tells the subscriber that a publisher of void elements is ready to receive further requests.

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
func receive() -> Subscribers.Demand
```

#### Return Value

A [`Subscribers.Demand`](subscribers/demand.md) instance indicating how many more elements the subscriber expects to receive.

#### Discussion

Use `Void` inputs and outputs when you want to signal that an event has occurred, but don’t need to send the event itself.

## See Also

- [func receive(Input) -> Subscribers.Demand](anysubscriber/receive(_:).md)
  Tells the subscriber that the publisher has produced an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anysubscriber/receive())*