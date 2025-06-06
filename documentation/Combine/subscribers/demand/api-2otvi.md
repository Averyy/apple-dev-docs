# <=(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean that indicates whether the demand requests fewer or the same number of elements as the given integer.

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
static func <= (lhs: Subscribers.Demand, rhs: Int) -> Bool
```

#### Discussion

If `lhs` is `.unlimited`, then the result is always `false`. Otherwise, the operator compares the demand’s `max` value to `rhs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/_=(_:_:)-2otvi)*