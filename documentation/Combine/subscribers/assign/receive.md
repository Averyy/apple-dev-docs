# receive(_:)

**Framework**: Combine  
**Kind**: method

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
final func receive(_ value: Input) -> Subscribers.Demand
```

#### Discussion

A [`Subscribers.Demand`](subscribers/demand.md) instance indicating how many more elements the subscriber expects to receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/assign/receive(_:))*