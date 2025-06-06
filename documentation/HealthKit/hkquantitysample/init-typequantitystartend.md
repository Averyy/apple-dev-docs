# init(type:quantity:start:end:)

**Framework**: HealthKit  
**Kind**: init

Returns a sample containing a numeric measurement.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(type quantityType: HKQuantityType, quantity: HKQuantity, start startDate: Date, end endDate: Date)
```

#### Return Value

A valid quantity sample.

#### Discussion

HealthKit uses quantity samples to represent sample data using a numeric value. To create a quantity sample, first create the corresponding quantity type and quantity, and then set its start and end dates. You produce a new quantity sample.

## Parameters

- `quantityType`: The type of sample to be created. HealthKit defines a number of different quantity types, representing different types of health and fitness data. For the complete list of quantity type identifiers, see  .
- `quantity`: The value to be stored in the sample. The quantity object must use units that are compatible with the provided quantity type. If the units are not compatible, this method throws an exception ( ).
- `startDate`: The start date for the sample. This date must be equal to or earlier than the end date; otherwise, this method throws an exception ( ).
- `endDate`: The end date for the sample. This date must be equal to or later than the start date; otherwise, this method throws an exception ( ).

## See Also

- [var quantityType: HKQuantityType](hkquantitysample/quantitytype.md)
  The quantity type for this sample.
- [var quantity: HKQuantity](hkquantitysample/quantity.md)
  The quantity for this sample.
- [var endDate: Date](hksample/enddate.md)
  The sample’s end date.
- [class func quantityType(forIdentifier: HKQuantityTypeIdentifier) -> HKQuantityType?](hkobjecttype/quantitytype(foridentifier:).md)
  Returns the shared quantity type for the provided identifier.
- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [convenience init(type: HKQuantityType, quantity: HKQuantity, start: Date, end: Date, metadata: [String : Any]?)](hkquantitysample/init(type:quantity:start:end:metadata:).md)
  Returns a sample containing a numeric measurement with the provided metadata.
- [convenience init(type: HKQuantityType, quantity: HKQuantity, start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](hkquantitysample/init(type:quantity:start:end:device:metadata:).md)
  Returns a sample containing a numeric measurement with the provided device and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitysample/init(type:quantity:start:end:))*