# MobilePhotoIDRawDataRequest

**Framework**: ProximityReader  
**Kind**: struct

A photo ID request which retrieves elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
struct MobilePhotoIDRawDataRequest
```

## Topics

### Creating a raw data request
- [init(retainedElements: [MobilePhotoIDRawDataRequest.Element], nonRetainedElements: [MobilePhotoIDRawDataRequest.Element])](mobilephotoidrawdatarequest/init(retainedelements:nonretainedelements:).md)
  Returns a photo ID raw data request.
- [MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element.md)
  A type representing an element that you can request from a photo ID.
- [var nonRetainedElements: [MobilePhotoIDRawDataRequest.Element]](mobilephotoidrawdatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDRawDataRequest.Element]](mobilephotoidrawdatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
### Handling the response
- [MobilePhotoIDRawDataRequest.Response](mobilephotoidrawdatarequest/response.md)
  A type that contains the response information from a successful photo ID raw data request.
### Default Implementations
- [MobileDocumentRequest Implementations](mobilephotoidrawdatarequest/mobiledocumentrequest-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MobileDocumentRawDataRequest](mobiledocumentrawdatarequest.md)
- [MobileDocumentRequest](mobiledocumentrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MobileDriversLicenseDisplayRequest](mobiledriverslicensedisplayrequest.md)
  A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [struct MobileDriversLicenseDataRequest](mobiledriverslicensedatarequest.md)
  A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileDriversLicenseRawDataRequest](mobiledriverslicenserawdatarequest.md)
  A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileNationalIDCardDisplayRequest](mobilenationalidcarddisplayrequest.md)
  A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [struct MobileNationalIDCardDataRequest](mobilenationalidcarddatarequest.md)
  A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileNationalIDCardRawDataRequest](mobilenationalidcardrawdatarequest.md)
  A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileDocumentDisplayRequest](mobiledocumentdisplayrequest.md)
  A mobile document request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [protocol MobileDocumentRequest](mobiledocumentrequest.md)
  A type that represents a mobile document request.
- [protocol MobileDocumentDataRequest](mobiledocumentdatarequest.md)
  A type that represents a mobile document data request.
- [protocol MobileDocumentRawDataRequest](mobiledocumentrawdatarequest.md)
  A type that represents a mobile document raw data request.
- [struct MobilePhotoIDDataRequest](mobilephotoiddatarequest.md)
  A photo ID request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileDocumentAnyOfDataRequest](mobiledocumentanyofdatarequest.md)
  A type that describes a data request for any mobile document from a group of requests.
- [struct MobileDocumentAnyOfRawDataRequest](mobiledocumentanyofrawdatarequest.md)
  A type that describes a raw data request for any mobile document from a group of requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoidrawdatarequest)*