# discrete

**Framework**: HealthKit  
**Kind**: property

Discrete samples may be averaged over time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var discrete: HKQuantityAggregationStyle { get }
```

#### Discussion

You typically use discrete types to monitor the change in the value over time. For example, body mass, heart rate, temperature, and respiratory rate are all discrete quantity types. You can also query for the minimum or maximum value in a given time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle/discrete)*