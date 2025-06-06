# none

**Framework**: Combine  
**Kind**: property

A request for no elements from the publisher.

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
static let none: Subscribers.Demand
```

#### Discussion

This is equivalent to `Demand.max(0)`.

## See Also

- [static let unlimited: Subscribers.Demand](subscribers/demand/unlimited.md)
  A request for as many values as the publisher can produce.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/none)*