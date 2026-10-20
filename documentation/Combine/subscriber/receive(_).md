# receive(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the subscriber that the publisher has produced an element.

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
func receive(_ input: Self.Input) -> Subscribers.Demand
```

## Mentions

- [Processing Published Elements with Subscribers](../processing-published-elements-with-subscribers.md)

#### Return Value

A `Subscribers.Demand` instance indicating how many more elements the subscriber expects to receive.

## Parameters

- `input`: The published element.

## See Also

### Receiving elements
- [func receive() -> Subscribers.Demand](./receive%28%29.md)
  Tells the subscriber that a publisher of void elements is ready to receive further requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscriber/receive(_:))*