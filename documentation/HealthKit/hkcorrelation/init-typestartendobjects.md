# init(type:start:end:objects:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a new correlation instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(type correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects: Set<HKSample>)
```

#### Return Value

A new correlation instance.

#### Discussion

Use a correlation object to represent composite data—that is, a sample that requires more than a single value. To create a correlation sample, first create the quantity and category samples you intend to combine into the correlation. Next, create the correlation’s type. Finally, instantiate the correlation, passing in the type, start date, end date, and samples, as shown below.

Use this method when you do not need to include additional metadata and the data was not recorded using external hardware.

## Parameters

- `correlationType`: The type for this correlation. For a complete list of correlation type identifiers, see  .
- `startDate`: The start date for the sample. This date must be equal to or earlier than the end date; otherwise, this method throws an exception ( ).
- `endDate`: The end date for the sample. This date must be equal to or later than the start date; otherwise, this method throws an exception ( ).
- `objects`: A set of   objects. Specifically, this set contains the quantity and category samples to be grouped into this correlation.

## See Also

- [var objects: Set<HKSample>](hkcorrelation/objects.md)
  The set of sample objects that make up the correlation.
- [class func correlationType(forIdentifier: HKCorrelationTypeIdentifier) -> HKCorrelationType?](hkobjecttype/correlationtype(foridentifier:).md)
  Returns the shared correlation type for the provided identifier.
- [var endDate: Date](hksample/enddate.md)
  The sample’s end date.
- [var correlationType: HKCorrelationType](hkcorrelation/correlationtype.md)
  The type for this correlation.
- [var metadata: [String : Any]?](hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [convenience init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>, metadata: [String : Any]?)](hkcorrelation/init(type:start:end:objects:metadata:).md)
  Instantiates and returns a new correlation instance with the provided metadata.
- [convenience init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>, device: HKDevice?, metadata: [String : Any]?)](hkcorrelation/init(type:start:end:objects:device:metadata:).md)
  Instantiates and returns a new correlation instance with the provided device and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelation/init(type:start:end:objects:))*