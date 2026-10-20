# rating

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

The relative impact of using electricity during this period of time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
let rating: Double
```

#### Discussion

Values are normalized between zero and one. A lower value indicates cleaner energy usage.

## See Also

### Creating a date interval
- [init(interval: DateInterval, rating: Double)](./init%28interval,rating%29.md)
  Creates an interval with the specified date and rating.
- [let interval: DateInterval](./interval.md)
  The interval to which the electrical guidance applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/value/rating)*