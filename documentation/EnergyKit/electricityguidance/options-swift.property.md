# options

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

The additional factors that influence the weight of a value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
let options: Set<ElectricityGuidance.Options>
```

## Discussion

A person’s utility rate plan is an example of an additional factor that influences the weight of the value.

## See Also

### Getting the electrical load weight
- [ElectricityGuidance.Value](./value.md)
  A normalized weighting value associated with a period of time, describing when to shift or reduce electricity use.
- [let values: [ElectricityGuidance.Value]](./values.md)
  A series of weighted values for intervals of time, describing when to shift or reduce electricity use.
- [ElectricityGuidance.Options](./options-swift.enum.md)
  An enumeration that describes additional factors that influence the weight of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/options-swift.property)*