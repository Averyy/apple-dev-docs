# >(_:_:)

**Framework**: Combine  
**Kind**: op  
**Role**: Operator

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

## See Also

### Comparing demands
- [static func == (Int, Subscribers.Demand) -> Bool](./eqeq%28_,_%29-4oy8i.md)
  Returns a Boolean value that indicates whether a given number of elements matches the request of a given demand.
- [static func == (Subscribers.Demand, Int) -> Bool](./eqeq%28_,_%29-7246z.md)
  Returns a Boolean value that indicates whether a demand requests the given number of elements.
- [static func != (Int, Subscribers.Demand) -> Bool](./noteq%28_,_%29-3j2h8.md)
  Returns a Boolean value that indicates whether an integer is unequal to a demand.
- [static func != (Subscribers.Demand, Int) -> Bool](./noteq%28_,_%29-2dj1p.md)
  Returns a Boolean value that indicates whether a demand isn’t equal to an integer.
- [static func < (Int, Subscribers.Demand) -> Bool](./op%28_,_%29-1wuod.md)
  Returns a Boolean that indicates a given number of elements is less than the maximum specified by the demand.
- [static func < (Subscribers.Demand, Int) -> Bool](./op%28_,_%29-ciby.md)
  Returns a Boolean that indicates whether the demand requests fewer than the given number of elements.
- [static func < (Subscribers.Demand, Subscribers.Demand) -> Bool](./op%28_,_%29-8nf1g.md)
  Returns a Boolean that indicates whether the first demand requests fewer elements than the second.
- [static func <= (Int, Subscribers.Demand) -> Bool](./opeq%28_,_%29-5f62z.md)
  Returns a Boolean value that indicates a given number of elements is less than or equal the maximum specified by the demand.
- [static func <= (Subscribers.Demand, Int) -> Bool](./opeq%28_,_%29-2otvi.md)
  Returns a Boolean that indicates whether the demand requests fewer or the same number of elements as the given integer.
- [static func <= (Subscribers.Demand, Subscribers.Demand) -> Bool](./opeq%28_,_%29-9cywv.md)
  Returns a Boolean value that indicates whether the first demand requests fewer or the same number of elements as the second.
- [static func > (Int, Subscribers.Demand) -> Bool](./op%28_,_%29-35p6f.md)
  Returns a Boolean that indicates a given number of elements is greater than the maximum specified by the demand.
- [static func > (Subscribers.Demand, Subscribers.Demand) -> Bool](./op%28_,_%29-74yle.md)
  Returns a Boolean that indicates whether the first demand requests more elements than the second.
- [static func >= (Int, Subscribers.Demand) -> Bool](./opeq%28_,_%29-6lv9s.md)
  Returns a Boolean that indicates a given number of elements is greater than or equal to the maximum specified by the demand.
- [static func >= (Subscribers.Demand, Int) -> Bool](./opeq%28_,_%29-28c1e.md)
  Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
- [static func >= (Subscribers.Demand, Subscribers.Demand) -> Bool](./opeq%28_,_%29-5xnt.md)
  Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/_(_:_:)-4k1xp)*