# init(type:value:start:end:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Creates a newly instantiated category sample.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(type: HKCategoryType, value: Int, start startDate: Date, end endDate: Date)
```

```objc
+ (instancetype) categorySampleWithType:(HKCategoryType *) type value:(NSInteger) value startDate:(NSDate *) startDate endDate:(NSDate *) endDate;
```

## Return Value

A valid category sample.

## Discussion

HealthKit uses category samples to represent data that can be classified into a finite set of categories. To create a category sample, you must first create the corresponding category type, and then set its start and end dates, as shown below.

**Swift**:

```swift
guard let categoryType =
    HKObjectType.categoryTypeForIdentifier(HKCategoryTypeIdentifierSleepAnalysis) else {
        fatalError("*** Unable to create a sleep analysis category type ***")
}
 
let categorySample = HKCategorySample(type: categoryType,
                                      value: HKCategoryValueSleepAnalysis.Asleep.rawValue,
                                      startDate: start,
                                      endDate: end)
```

**Objective-C**:

```objc
HKCategoryType *categoryType =
[HKObjectType categoryTypeForIdentifier:HKCategoryTypeIdentifierSleepAnalysis];
 
HKCategorySample *categorySample =
[HKCategorySample categorySampleWithType:categoryType
                                   value:HKCategoryValueSleepAnalysisAsleep
                               startDate:start
                                 endDate:end];
```

## Parameters

- `type`: The category type for this sample. For a complete list, see [`HKCategoryTypeIdentifier`](../hkcategorytypeidentifier.md).
- `value`: The value for this sample. This value must come from the appropriate category value enumeration. Each category type uses its own enumeration. For more information, see [`HKCategoryTypeIdentifier`](../hkcategorytypeidentifier.md).
- `startDate`: The start date for the sample. This must be equal to or earlier than the end date; otherwise, this method throws an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)).
- `endDate`: The end date for the sample. This must be equal to or later than the start date; otherwise, this method throws an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)).

## See Also

### Related Documentation
- [var value: Int](./value.md)
  The category value for this sample.
- [class func categoryType(forIdentifier: HKCategoryTypeIdentifier) -> HKCategoryType?](../hkobjecttype/categorytype%28foridentifier%29.md)
  Returns the shared category type for the provided identifier.
- [var endDate: Date](../hksample/enddate.md)
  The sample’s end date.
- [var categoryType: HKCategoryType](./categorytype.md)
  The category type for this sample.
- [var startDate: Date](../hksample/startdate.md)
  The sample’s start date.
### Creating Category Samples
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date, metadata: [String : Any]?)](./init%28type,value,start,end,metadata%29.md)
  Creates a newly instantiated category sample with the provided metadata.
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](./init%28type,value,start,end,device,metadata%29.md)
  Creates a newly instantiated category sample including the provided device and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorysample/init(type:value:start:end:))*