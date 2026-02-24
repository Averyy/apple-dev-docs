# init(data:start:end:metadata:)

**Framework**: HealthKit  
**Kind**: init

Returns a CDA document sample containing the provided XML document and metadata.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(data documentData: Data, start startDate: Date, end endDate: Date, metadata: [String : Any]?) throws
```

#### Return Value

A valid CDA document sample with the provided metadata.

#### Discussion

To create a CDA document sample:

1. Create [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) objects to represent fallback start and end dates for the sample. Where possible, the system uses the effective date from the document’s XML data to set the sample’s start and end dates. The start and end date parameters are only used when the effective date is not available. Use the current date and time.
2. Create an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object that contains the CDA’s XML data.
3. (optionally) Create an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) object containing any additional metadata for this sample.
4. Call the `HKCDADocumentSample` class’s [`init(data:start:end:metadata:)`](hkcdadocumentsample/init(data:start:end:metadata:).md) method. Handle any errors that occur during XML validation.
5. Save the sample to the HealthKit store. Handle any errors that occur while saving.

```swift
// Creating a Health Document Using HKCDADocumentSample
let today = Date()
let documentData: Data = ... // Use XML data provided by a health organization
do {
    let cdaSample = try HKCDADocumentSample.init(data: documentData, start: today, end:
        today, metadata: nil)
    healthStore.save(cdaSample) { success, error in
        // Handle save error here...
    }
} catch {
    // Handle validation error here...
}
```

## Parameters

- `documentData`: The CDA document in an XML format that meets the CDA standard. For more information on the CDA document format, see the [`Clinical Document Architecture, R2`](https://developer.apple.comhttp://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) standard.
- `startDate`: A fallback start date for the sample. This date is only used when the XML document does not include the document’s effective date. This date must be equal to or earlier than the end date; otherwise, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)).
- `endDate`: A fallback end date for the sample. This date is only used when the XML document does not include the document’s effective date. This date must be equal to or later than the start date; otherwise, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)).
- `metadata`: The metadata dictionary contains extra information describing this sample. The dictionary’s keys are all [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects. The values may be [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects, or [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) objects. For a complete list of predefined metadata keys, see Metadata Keys in [`HealthKit Constants`](healthkit-constants.md). Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the sample’s capabilities.

## See Also

- [let HKDetailedCDAValidationErrorKey: String](hkdetailedcdavalidationerrorkey.md)
  A key for accessing validation error information from an error object’s user information dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample/init(data:start:end:metadata:))*