# numberOfAlcoholicBeverages

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the number of standard alcoholic drinks that the user has consumed.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let numberOfAlcoholicBeverages: HKQuantityTypeIdentifier
```

#### Discussion

Samples matching the [`numberOfAlcoholicBeverages`](hkquantitytypeidentifier/numberofalcoholicbeverages.md) identifier measure the number of standard alcoholic drinks consumed by the user. A standard drink is one beer, glass of wine, or mixed drink made with spirits. The samples use count units (described in [`HKUnit`](hkunit.md)) to measure cumulative values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)).

The following code listing saves a single standard drink to the HealthKit store.

```swift
// Create the alcoholic beverage sample type.
let alcoholConsumptionType = HKQuantityType(.numberOfAlcoholicBeverages)

// Create a quantity for the number of standard beverages consumed.
let beverageCount = HKQuantity(unit:HKUnit.count(), doubleValue:1.0)

// Get the current date.
let date = Date()

// Create the alcoholic beverage consumption sample.
let beverageSample = HKQuantitySample(type: alcoholConsumptionType,
                                      quantity: beverageCount,
                                      start: date,
                                      end: date)

// Save the sample to the HealthKit store.
store.save(beverageSample) { (success, error) in
    
    if success {
        // The system successfully saved the sample.
        
    } else {
        if let error = error {
            // Handle the error here.
        }
    }
}
```

## See Also

- [static let bloodAlcoholContent: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodalcoholcontent.md)
  A quantity sample type that measures the user’s blood alcohol content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/numberofalcoholicbeverages)*