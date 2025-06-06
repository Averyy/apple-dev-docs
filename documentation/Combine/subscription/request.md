# request(_:)

**Framework**: Combine  
**Kind**: method  
**Required**: Yes

Tells a publisher that it may send more values to the subscriber.

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
func request(_ demand: Subscribers.Demand)
```

## Mentions

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)

## See Also

- [Subscribers.Demand](subscribers/demand.md)
  A requested number of items, sent to a publisher from a subscriber through the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscription/request(_:))*