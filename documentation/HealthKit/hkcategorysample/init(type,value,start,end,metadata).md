# init(type:value:start:end:metadata:)

**Framework**: HealthKit  
**Kind**: init

Creates a newly instantiated category sample with the provided metadata.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(type: HKCategoryType, value: Int, start startDate: Date, end endDate: Date, metadata: [String : Any]?)
```

#### Return Value

A valid category sample with metadata.

#### Discussion

HealthKit uses category samples to represent data that can be classified into a finite set of categories. To create a category sample, you must first create the corresponding category type and then set its start date, end date, and metadata, as shown below.

**Swift**:

```swift
let metadata : [String : AnyObject] =
    [HKMetadataKeyDigitalSignature:digitalSignature,
     HKMetadataKeyTimeZone:timeZone]
 
guard let categoryType =
    HKObjectType.categoryTypeForIdentifier(HKCategoryTypeIdentifierSleepAnalysis) else {
        fatalError("*** Unable to create a sleep analysis category type ***")
}
 
let categorySample = HKCategorySample(type: categoryType,
                                      value: HKCategoryValueSleepAnalysis.Asleep.rawValue,
                                      startDate: start,
                                      endDate: end,
                                      metadata:metadata)
```

**Objective-C**:

```objc
NSDictionary *metadata =
@{HKMetadataKeyDigitalSignature:digitalSignature,
HKMetadataKeyTimeZone:timeZone};
 
HKCategoryType *categoryType =
[HKObjectType categoryTypeForIdentifier:HKCategoryTypeIdentifierSleepAnalysis];
 
HKCategorySample *categorySample =
[HKCategorySample categorySampleWithType:categoryType
                                   value:HKCategoryValueSleepAnalysisAsleep
                               startDate:start
                                 endDate:end
                                metadata:metadata];
```

## Parameters

- `type`: The category type for this sample. For a complete list, see [`HKCategoryTypeIdentifier`](hkcategorytypeidentifier.md).
- `value`: The value for this sample. This value must come from the appropriate category value enumeration. Each category type uses its own enumeration. For more information, see Category Type Identifiers in [`HealthKit Constants`](healthkit-constants.md).
- `startDate`: The start date for the sample. This must be equal to or earlier than the end date; otherwise, this method throws an exception (`NSInvalidArgumentException`).
- `endDate`: The end date for the sample. This must be equal to or later than the start date; otherwise, this method throws an exception (`NSInvalidArgumentException`).
- `metadata`: The metadata dictionary contains extra information describing this sample. The dictionary’s keys are all [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) objects. The values may be [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) objects, [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) objects or [`NSDate`](https://developer.apple.com/documentation/foundation/nsdate) objects. For a complete list of predefined metadata keys, see Metadata Keys in [`HealthKit Constants`](healthkit-constants.md). Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the HealthKit category sample’s capabilities.

## See Also

- [var value: Int](hkcategorysample/value.md)
  The category value for this sample.
- [class func categoryType(forIdentifier: HKCategoryTypeIdentifier) -> HKCategoryType?](hkobjecttype/categorytype(foridentifier:).md)
  Returns the shared category type for the provided identifier.
- [var endDate: Date](hksample/enddate.md)
  The sample’s end date.
- [var metadata: [String : Any]?](hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var categoryType: HKCategoryType](hkcategorysample/categorytype.md)
  The category type for this sample.
- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date)](hkcategorysample/init(type:value:start:end:).md)
  Creates a newly instantiated category sample.
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](hkcategorysample/init(type:value:start:end:device:metadata:).md)
  Creates a newly instantiated category sample including the provided device and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorysample/init(type:value:start:end:metadata:))*