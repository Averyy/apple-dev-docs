# distance(to:)

**Framework**: Foundation  
**Kind**: method

Returns the distance from this date to another date, specified as a time interval.

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
func distance(to other: Date) -> TimeInterval
```

#### Return Value

The distance from this date to the other date, as a [`TimeInterval`](timeinterval.md).

## Parameters

- `other`: Another date.

## See Also

- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
- [static func > (Date, Date) -> Bool](date/_(_:_:)-880ns.md)
  Returns true if the left hand `Date` is later in time than the right hand `Date`.
- [static func < (Date, Date) -> Bool](date/_(_:_:)-42kro.md)
  Returns true if the left hand `Date` is earlier in time than the right hand `Date`.
- [func compare(Date) -> ComparisonResult](date/compare(_:).md)
  Compares another date to this one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/distance(to:))*