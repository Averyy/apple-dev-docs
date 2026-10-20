# ElectricityGuidance.Value

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

A normalized weighting value associated with a period of time, describing when to shift or reduce electricity use.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
struct Value
```

## Mentions

- [Providing charging history for electric vehicles](../providing-informative-charging-history-for-electric-vehicles.md)

## Topics

### Creating a date interval
- [init(interval: DateInterval, rating: Double)](./value/init%28interval,rating%29.md)
  Creates an interval with the specified date and rating.
- [let interval: DateInterval](./value/interval.md)
  The interval to which the electrical guidance applies.
- [let rating: Double](./value/rating.md)
  The relative impact of using electricity during this period of time.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the electrical load weight
- [let values: [ElectricityGuidance.Value]](./values.md)
  A series of weighted values for intervals of time, describing when to shift or reduce electricity use.
- [ElectricityGuidance.Options](./options-swift.enum.md)
  An enumeration that describes additional factors that influence the weight of a value.
- [let options: Set<ElectricityGuidance.Options>](./options-swift.property.md)
  The additional factors that influence the weight of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/value)*