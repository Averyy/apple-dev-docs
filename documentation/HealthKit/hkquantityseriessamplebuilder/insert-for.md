# insert(_:for:)

**Framework**: HealthKit  
**Kind**: method

Adds a new quantity to the series with the provided date interval.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func insert(_ quantity: HKQuantity, for dateInterval: DateInterval) throws
```

#### Discussion

Use this method to add a quantity to the series. The quantity must have a unit that is compatible with the series builder’s quantity type (see [`is(compatibleWith:)`](hkquantitytype/is(compatiblewith:).md)).

> **Note**:  You can insert quantities in any order. The builder sorts them by the date interval’s [`startDate`](https://developer.apple.com/documentation/Foundation/NSDateInterval/startDate) property when you finish the series.

## Parameters

- `quantity`: The quantity to insert.
- `dateInterval`: The date interval associated with the quantity. If the interval’s   parameter is the same as the start date for a previously provided quantity, this quantity replaces the previous one. This method fails with an   error if the date parameter is earlier than the series builder’s   property.

## See Also

- [func insert(HKQuantity, at: Date) throws](hkquantityseriessamplebuilder/insert(_:at:).md)
  Adds a new quantity to the series at the provided date and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder/insert(_:for:))*