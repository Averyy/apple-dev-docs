# receive()

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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

Available when `Input` is `()`.

## Return Value

A [`Subscribers.Demand`](../subscribers/demand.md) instance indicating how many more elements the subscriber expects to receive.

## Discussion

Use `Void` inputs and outputs when you want to signal that an event has occurred, but don’t need to send the event itself.

## See Also

### Receiving elements
- [func receive(Self.Input) -> Subscribers.Demand](./receive%28_%29.md)
  Tells the subscriber that the publisher has produced an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscriber/receive())*