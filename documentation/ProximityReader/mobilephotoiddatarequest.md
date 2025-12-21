# MobilePhotoIDDataRequest

**Framework**: ProximityReader  
**Kind**: struct

A photo ID request that retrieves elements from the holder and returns the validated document elements.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
struct MobilePhotoIDDataRequest
```

## Topics

### Creating a data request
- [init(retainedElements: [MobilePhotoIDDataRequest.Element], nonRetainedElements: [MobilePhotoIDDataRequest.Element])](mobilephotoiddatarequest/init(retainedelements:nonretainedelements:).md)
  Returns a photo ID data request.
- [MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element.md)
  A type that represents an element you can request from a photo ID.
- [var nonRetainedElements: [MobilePhotoIDDataRequest.Element]](mobilephotoiddatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDDataRequest.Element]](mobilephotoiddatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
### Handling the response
- [MobilePhotoIDDataRequest.Response](mobilephotoiddatarequest/response.md)
  A type that contains the response information from a successful photo ID data request.
### Default Implementations
- [MobileDocumentRequest Implementations](mobilephotoiddatarequest/mobiledocumentrequest-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MobileDocumentDataRequest](mobiledocumentdatarequest.md)
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
- [struct MobilePhotoIDRawDataRequest](mobilephotoidrawdatarequest.md)
  A photo ID request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileDocumentAnyOfDataRequest](mobiledocumentanyofdatarequest.md)
  A type that describes a data request for any mobile document from a group of requests.
- [struct MobileDocumentAnyOfRawDataRequest](mobiledocumentanyofrawdatarequest.md)
  A type that describes a raw data request for any mobile document from a group of requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest)*