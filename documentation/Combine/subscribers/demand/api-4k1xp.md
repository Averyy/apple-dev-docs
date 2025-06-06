# >(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean that indicates whether the demand requests more than the given number of elements.

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
static func > (lhs: Subscribers.Demand, rhs: Int) -> Bool
```

#### Discussion

If `lhs` is `.unlimited`, then the result is always `true`. Otherwise, the operator compares the demand’s `max` value to `rhs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/_(_:_:)-4k1xp)*