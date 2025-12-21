# !=(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean value that indicates whether an integer is unequal to a demand.

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
static func != (lhs: Int, rhs: Subscribers.Demand) -> Bool
```

#### Discussion

The `.unlimited` value isn’t equal to any integer.

## See Also

- [static func == (Int, Subscribers.Demand) -> Bool](subscribers/demand/==(_:_:)-4oy8i.md)
  Returns a Boolean value that indicates whether a given number of elements matches the request of a given demand.
- [static func == (Subscribers.Demand, Int) -> Bool](subscribers/demand/==(_:_:)-7246z.md)
  Returns a Boolean value that indicates whether a demand requests the given number of elements.
- [static func != (Subscribers.Demand, Int) -> Bool](subscribers/demand/!=(_:_:)-2dj1p.md)
  Returns a Boolean value that indicates whether a demand isn’t equal to an integer.
- [static func < (Int, Subscribers.Demand) -> Bool](subscribers/demand/_(_:_:)-1wuod.md)
  Returns a Boolean that indicates a given number of elements is less than the maximum specified by the demand.
- [static func < (Subscribers.Demand, Int) -> Bool](subscribers/demand/_(_:_:)-ciby.md)
  Returns a Boolean that indicates whether the demand requests fewer than the given number of elements.
- [static func < (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/_(_:_:)-8nf1g.md)
  Returns a Boolean that indicates whether the first demand requests fewer elements than the second.
- [static func <= (Int, Subscribers.Demand) -> Bool](subscribers/demand/_=(_:_:)-5f62z.md)
  Returns a Boolean value that indicates a given number of elements is less than or equal the maximum specified by the demand.
- [static func <= (Subscribers.Demand, Int) -> Bool](subscribers/demand/_=(_:_:)-2otvi.md)
  Returns a Boolean that indicates whether the demand requests fewer or the same number of elements as the given integer.
- [static func <= (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/_=(_:_:)-9cywv.md)
  Returns a Boolean value that indicates whether the first demand requests fewer or the same number of elements as the second.
- [static func > (Int, Subscribers.Demand) -> Bool](subscribers/demand/_(_:_:)-35p6f.md)
  Returns a Boolean that indicates a given number of elements is greater than the maximum specified by the demand.
- [static func > (Subscribers.Demand, Int) -> Bool](subscribers/demand/_(_:_:)-4k1xp.md)
  Returns a Boolean that indicates whether the demand requests more than the given number of elements.
- [static func > (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/_(_:_:)-74yle.md)
  Returns a Boolean that indicates whether the first demand requests more elements than the second.
- [static func >= (Int, Subscribers.Demand) -> Bool](subscribers/demand/_=(_:_:)-6lv9s.md)
  Returns a Boolean that indicates a given number of elements is greater than or equal to the maximum specified by the demand.
- [static func >= (Subscribers.Demand, Int) -> Bool](subscribers/demand/_=(_:_:)-28c1e.md)
  Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
- [static func >= (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/_=(_:_:)-5xnt.md)
  Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/!=(_:_:)-3j2h8)*