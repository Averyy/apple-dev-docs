# +=(_:_:)

**Framework**: Combine  
**Kind**: op

Adds two demands, and assigns the result to the first demand.

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
static func += (lhs: inout Subscribers.Demand, rhs: Subscribers.Demand)
```

#### Discussion

When adding any value to `.unlimited`, the result is `.unlimited`.

## See Also

- [static func * (Subscribers.Demand, Int) -> Subscribers.Demand](subscribers/demand/*(_:_:).md)
  Returns the result of multiplying a demand by an integer.
- [static func *= (inout Subscribers.Demand, Int)](subscribers/demand/*=(_:_:).md)
  Multiplies a demand by an integer, and assigns the result to the demand.
- [static func + (Subscribers.Demand, Subscribers.Demand) -> Subscribers.Demand](subscribers/demand/+(_:_:)-2hdad.md)
  Returns the result of adding two demands. When adding any value to `.unlimited`, the result is `.unlimited`.
- [static func + (Subscribers.Demand, Int) -> Subscribers.Demand](subscribers/demand/+(_:_:)-902we.md)
  Returns the result of adding an integer to a demand.
- [static func += (inout Subscribers.Demand, Int)](subscribers/demand/+=(_:_:)-3k1hv.md)
  Adds an integer to a demand, and assigns the result to the demand.
- [static func - (Subscribers.Demand, Subscribers.Demand) -> Subscribers.Demand](subscribers/demand/-(_:_:)-1r0gm.md)
  Returns the result of subtracting one demand from another.
- [static func - (Subscribers.Demand, Int) -> Subscribers.Demand](subscribers/demand/-(_:_:)-6mw4s.md)
  Returns the result of subtracting an integer from a demand.
- [static func -= (inout Subscribers.Demand, Subscribers.Demand)](subscribers/demand/-=(_:_:)-1d0m9.md)
  Subtracts one demand from another, and assigns the result to the first demand.
- [static func -= (inout Subscribers.Demand, Int)](subscribers/demand/-=(_:_:)-9pwnc.md)
  Subtracts an integer from a demand, and assigns the result to the demand.
- [static func ... (Self) -> PartialRangeFrom<Self>](subscribers/demand/'...(_:)-3qgos.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](subscribers/demand/'...(_:)-kb35.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](subscribers/demand/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/+=(_:_:)-20lis)*