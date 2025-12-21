# MobileDocumentDisplayRequest

**Framework**: ProximityReader  
**Kind**: struct

A mobile document request that retrieves elements from the holder and displays the results onscreen for visual inspection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
struct MobileDocumentDisplayRequest
```

## Topics

### Creating a display request
- [init(elements: [MobileDocumentDisplayRequest.Element], options: MobileDocumentDisplayRequest.Options)](mobiledocumentdisplayrequest/init(elements:options:).md)
  Creates a new mobile document display request.
- [MobileDocumentDisplayRequest.Element](mobiledocumentdisplayrequest/element.md)
  A type that represents an element you can request from a mobile document.
### Configuring a display request
- [MobileDocumentDisplayRequest.Options](mobiledocumentdisplayrequest/options-swift.struct.md)
  An object that customizes how to perform a display request.
- [var options: MobileDocumentDisplayRequest.Options](mobiledocumentdisplayrequest/options-swift.property.md)
  An object that customizes how to perform a display request.
### Handling the response
- [MobileDocumentDisplayRequest.Response](mobiledocumentdisplayrequest/response.md)
  A type that contains the response information from a successful mobile document display request.
### Instance Properties
- [var elements: [MobileDocumentDisplayRequest.Element]](mobiledocumentdisplayrequest/elements.md)
  The document elements you’re requesting.
### Default Implementations
- [MobileDocumentRequest Implementations](mobiledocumentdisplayrequest/mobiledocumentrequest-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [protocol MobileDocumentRequest](mobiledocumentrequest.md)
  A type that represents a mobile document request.
- [protocol MobileDocumentDataRequest](mobiledocumentdatarequest.md)
  A type that represents a mobile document data request.
- [protocol MobileDocumentRawDataRequest](mobiledocumentrawdatarequest.md)
  A type that represents a mobile document raw data request.
- [struct MobilePhotoIDDataRequest](mobilephotoiddatarequest.md)
  A photo ID request that retrieves elements from the holder and returns the validated document elements.
- [struct MobilePhotoIDRawDataRequest](mobilephotoidrawdatarequest.md)
  A photo ID request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileDocumentAnyOfDataRequest](mobiledocumentanyofdatarequest.md)
  A type that describes a data request for any mobile document from a group of requests.
- [struct MobileDocumentAnyOfRawDataRequest](mobiledocumentanyofrawdatarequest.md)
  A type that describes a raw data request for any mobile document from a group of requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest)*