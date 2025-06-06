# !=(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean value that indicates whether a demand isn’t equal to an integer.

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
static func != (lhs: Subscribers.Demand, rhs: Int) -> Bool
```

#### Discussion

The `.unlimited` value isn’t equal to any integer.

## See Also

- [static func == (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/==(_:_:)-28b3l.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func == (Subscribers.Demand, Int) -> Bool](subscribers/demand/==(_:_:)-7246z.md)
  Returns a Boolean value that indicates whether a demand requests the given number of elements.
- [static func == (Int, Subscribers.Demand) -> Bool](subscribers/demand/==(_:_:)-4oy8i.md)
  Returns a Boolean value that indicates whether a given number of elements matches the request of a given demand.
- [static func != (Self, Self) -> Bool](subscribers/demand/!=(_:_:)-5u2pg.md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func != (Int, Subscribers.Demand) -> Bool](subscribers/demand/!=(_:_:)-3j2h8.md)
  Returns a Boolean value that indicates whether an integer is unequal to a demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/!=(_:_:)-2dj1p)*