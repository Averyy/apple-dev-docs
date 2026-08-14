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

**Swift**:

```swift
guard let quantityType = HKObjectType.quantityTypeForIdentifier(HKQuantityTypeIdentifierHeartRate) else {
    fatalError("*** Unable to create a heart rate quantity type ***")
}
 
let bpm = HKUnit(fromString: "count/min")
let quantity = HKQuantity(unit: bpm, doubleValue: 72.0)
 
let quantitySample = HKQuantitySample(type: quantityType,
                                      quantity: quantity,
                                      startDate: start,
                                      endDate: end)
```

**Objective-C**:

```objc
HKQuantityType *quantityType =
[HKObjectType quantityTypeForIdentifier:HKQuantityTypeIdentifierHeartRate];
 
HKUnit *bpm = [HKUnit unitFromString:@"count/min"];
 
HKQuantity *quantity = [HKQuantity quantityWithUnit:bpm
                                        doubleValue:72.0];
 
HKQuantitySample *sample =
[HKQuantitySample quantitySampleWithType:quantityType
                                quantity:quantity
                               startDate:start
                                 endDate:end];
```

## Parameters

- `quantityType`: The type of sample to be created. HealthKit defines a number of different quantity types, representing different types of health and fitness data. For the complete list of quantity type identifiers, see [`HKQuantityTypeIdentifier`](hkquantitytypeidentifier.md).
- `quantity`: The value to be stored in the sample. The quantity object must use units that are compatible with the provided quantity type. If the units are not compatible, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/invalidargumentexception)).
- `startDate`: The start date for the sample. This date must be equal to or earlier than the end date; otherwise, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/invalidargumentexception)).
- `endDate`: The end date for the sample. This date must be equal to or later than the start date; otherwise, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/invalidargumentexception)).

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