# -(_:_:)

**Framework**: Combine  
**Kind**: op  
**Role**: Operator

Returns the result of subtracting an integer from a demand.

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
static func - (lhs: Subscribers.Demand, rhs: Int) -> Subscribers.Demand
```

## Discussion

When subtracting any value from `.unlimited`, the result is still `.unlimited`. A negative demand is possible, but be aware that it isn’t usable when requesting values in a subscription.

## See Also

### Performing mathematical operations
- [static func * (Subscribers.Demand, Int) -> Subscribers.Demand](./star%28_,_%29.md)
  Returns the result of multiplying a demand by an integer.
- [static func *= (inout Subscribers.Demand, Int)](./stareq%28_,_%29.md)
  Multiplies a demand by an integer, and assigns the result to the demand.
- [static func + (Subscribers.Demand, Subscribers.Demand) -> Subscribers.Demand](./plus%28_,_%29-2hdad.md)
  Returns the result of adding two demands. When adding any value to `.unlimited`, the result is `.unlimited`.
- [static func + (Subscribers.Demand, Int) -> Subscribers.Demand](./plus%28_,_%29-902we.md)
  Returns the result of adding an integer to a demand.
- [static func += (inout Subscribers.Demand, Subscribers.Demand)](./pluseq%28_,_%29-20lis.md)
  Adds two demands, and assigns the result to the first demand.
- [static func += (inout Subscribers.Demand, Int)](./pluseq%28_,_%29-3k1hv.md)
  Adds an integer to a demand, and assigns the result to the demand.
- [static func - (Subscribers.Demand, Subscribers.Demand) -> Subscribers.Demand](./minus%28_,_%29-1r0gm.md)
  Returns the result of subtracting one demand from another.
- [static func -= (inout Subscribers.Demand, Subscribers.Demand)](./minuseq%28_,_%29-1d0m9.md)
  Subtracts one demand from another, and assigns the result to the first demand.
- [static func -= (inout Subscribers.Demand, Int)](./minuseq%28_,_%29-9pwnc.md)
  Subtracts an integer from a demand, and assigns the result to the demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/-(_:_:)-6mw4s)*