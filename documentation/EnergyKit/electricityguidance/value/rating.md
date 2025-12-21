# rating

**Framework**: EnergyKit  
**Kind**: property

The relative impact of using electricity during this period of time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
let rating: Double
```

#### Discussion

Values are normalized between zero and one. A lower value indicates cleaner energy usage.

## See Also

- [init(interval: DateInterval, rating: Double)](electricityguidance/value/init(interval:rating:).md)
  Creates an interval with the specified date and rating.
- [let interval: DateInterval](electricityguidance/value/interval.md)
  The interval to which the electrical guidance applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/value/rating)*