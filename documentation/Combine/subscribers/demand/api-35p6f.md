# >(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean that indicates a given number of elements is greater than the maximum specified by the demand.

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
static func > (lhs: Int, rhs: Subscribers.Demand) -> Bool
```

#### Discussion

If `rhs` is `.unlimited`, then the result is always `false`. Otherwise, the operator compares the demand’s `max` value to `lhs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/_(_:_:)-35p6f)*