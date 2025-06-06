# ==(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean value indicating whether two values are equal.

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
static func == (a: Subscribers.Demand, b: Subscribers.Demand) -> Bool
```

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func == (Subscribers.Demand, Int) -> Bool](subscribers/demand/==(_:_:)-7246z.md)
  Returns a Boolean value that indicates whether a demand requests the given number of elements.
- [static func == (Int, Subscribers.Demand) -> Bool](subscribers/demand/==(_:_:)-4oy8i.md)
  Returns a Boolean value that indicates whether a given number of elements matches the request of a given demand.
- [static func != (Self, Self) -> Bool](subscribers/demand/!=(_:_:)-5u2pg.md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func != (Subscribers.Demand, Int) -> Bool](subscribers/demand/!=(_:_:)-2dj1p.md)
  Returns a Boolean value that indicates whether a demand isn’t equal to an integer.
- [static func != (Int, Subscribers.Demand) -> Bool](subscribers/demand/!=(_:_:)-3j2h8.md)
  Returns a Boolean value that indicates whether an integer is unequal to a demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/==(_:_:)-28b3l)*