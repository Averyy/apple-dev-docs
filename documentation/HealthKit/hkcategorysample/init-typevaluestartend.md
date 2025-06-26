# init(type:value:start:end:)

**Framework**: HealthKit  
**Kind**: init

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

#### Return Value

A valid category sample.

#### Discussion

HealthKit uses category samples to represent data that can be classified into a finite set of categories. To create a category sample, you must first create the corresponding category type, and then set its start and end dates, as shown below.

## Parameters

- `type`: The category type for this sample. For a complete list, see  .
- `value`: The value for this sample. This value must come from the appropriate category value enumeration. Each category type uses its own enumeration. For more information, see  .
- `startDate`: The start date for the sample. This must be equal to or earlier than the end date; otherwise, this method throws an exception ( ).
- `endDate`: The end date for the sample. This must be equal to or later than the start date; otherwise, this method throws an exception ( ).

## See Also

- [var value: Int](hkcategorysample/value.md)
  The category value for this sample.
- [class func categoryType(forIdentifier: HKCategoryTypeIdentifier) -> HKCategoryType?](hkobjecttype/categorytype(foridentifier:).md)
  Returns the shared category type for the provided identifier.
- [var endDate: Date](hksample/enddate.md)
  The sample’s end date.
- [var categoryType: HKCategoryType](hkcategorysample/categorytype.md)
  The category type for this sample.
- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date, metadata: [String : Any]?)](hkcategorysample/init(type:value:start:end:metadata:).md)
  Creates a newly instantiated category sample with the provided metadata.
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](hkcategorysample/init(type:value:start:end:device:metadata:).md)
  Creates a newly instantiated category sample including the provided device and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorysample/init(type:value:start:end:))*