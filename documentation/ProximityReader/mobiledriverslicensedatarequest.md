# MobileDriversLicenseDataRequest

**Framework**: ProximityReader  
**Kind**: struct

A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct MobileDriversLicenseDataRequest
```

## Topics

### Creating a data request
- [init(retainedElements: [MobileDriversLicenseDataRequest.Element], nonRetainedElements: [MobileDriversLicenseDataRequest.Element])](mobiledriverslicensedatarequest/init(retainedelements:nonretainedelements:).md)
  Returns a mobile driver’s license data request.
- [var retainedElements: [MobileDriversLicenseDataRequest.Element]](mobiledriverslicensedatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileDriversLicenseDataRequest.Element]](mobiledriverslicensedatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element.md)
  A type that represents an element you can request from a mobile driver’s license.
### Handling the Response
- [MobileDriversLicenseDataRequest.Response](mobiledriverslicensedatarequest/response.md)
  A type that contains the response information from a successful mobile driver’s license data request.
### Operators
- [static func == (MobileDriversLicenseDataRequest, MobileDriversLicenseDataRequest) -> Bool](mobiledriverslicensedatarequest/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledriverslicensedatarequest/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicensedatarequest/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledriverslicensedatarequest/equatable-implementations.md)
- [MobileDocumentRequest Implementations](mobiledriverslicensedatarequest/mobiledocumentrequest-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MobileDocumentDataRequest](mobiledocumentdatarequest.md)
- [MobileDocumentRequest](mobiledocumentrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MobileDriversLicenseDisplayRequest](mobiledriverslicensedisplayrequest.md)
  A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
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
- [struct MobilePhotoIDRawDataRequest](mobilephotoidrawdatarequest.md)
  A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileDocumentAnyOfDataRequest](mobiledocumentanyofdatarequest.md)
  A type that describes a data request for any mobile document from a group of requests.
- [struct MobileDocumentAnyOfRawDataRequest](mobiledocumentanyofrawdatarequest.md)
  A type that describes a raw data request for any mobile document from a group of requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest)*