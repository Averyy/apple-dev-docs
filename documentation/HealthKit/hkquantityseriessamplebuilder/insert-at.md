# insert(_:at:)

**Framework**: HealthKit  
**Kind**: method

Adds a new quantity to the series at the provided date and time.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func insert(_ quantity: HKQuantity, at date: Date) throws
```

#### Discussion

This method calls [`insert(_:for:)`](hkquantityseriessamplebuilder/insert(_:for:).md), passing a date interval with the provided start date, and a duration of `0`.

## Parameters

- `quantity`: The quantity to insert.
- `date`: The start date associated with the quantity. If this is the same start date as a previously provided quantity, this quantity replaces the previous one. This method fails with an [`HKError.Code.errorInvalidArgument`](hkerror/code/errorinvalidargument.md) error if the `date` parameter is earlier than the series builder’s [`startDate`](hkquantityseriessamplebuilder/startdate.md) property.

## See Also

- [func insert(HKQuantity, for: DateInterval) throws](hkquantityseriessamplebuilder/insert(_:for:).md)
  Adds a new quantity to the series with the provided date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder/insert(_:at:))*