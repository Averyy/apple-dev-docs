# bloodAlcoholContent

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures the user’s blood alcohol content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let bloodAlcoholContent: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierBloodAlcoholContent;
```

#### Discussion

These samples use percent units (described in [`HKUnit`](../hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

## See Also

### Alcohol consumption
- [static let numberOfAlcoholicBeverages: HKQuantityTypeIdentifier](./numberofalcoholicbeverages.md)
  A quantity sample type that measures the number of standard alcoholic drinks that the user has consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/bloodalcoholcontent)*