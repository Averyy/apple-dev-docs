# MobileDocumentAnyOfDataRequest

**Framework**: ProximityReader  
**Kind**: struct

A type that describes a data request for any mobile document from a group of requests.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct MobileDocumentAnyOfDataRequest
```

## Topics

### Initializing a request
- [init()](mobiledocumentanyofdatarequest/init.md)
  Returns a composite mobile document data request.
### Handling the response
- [MobileDocumentAnyOfDataRequest.Response](mobiledocumentanyofdatarequest/response.md)
  A type that contains the response information from a successful data request.
### Operators
- [static func == (MobileDocumentAnyOfDataRequest, MobileDocumentAnyOfDataRequest) -> Bool](mobiledocumentanyofdatarequest/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledocumentanyofdatarequest/hashvalue.md)
  The hash value.
### Instance Methods
- [func addRequest(any MobileDocumentDataRequest)](mobiledocumentanyofdatarequest/addrequest(_:).md)
  Adds the request as a candidate of this composite request.
- [func hash(into: inout Hasher)](mobiledocumentanyofdatarequest/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledocumentanyofdatarequest/equatable-implementations.md)
- [MobileDocumentRequest Implementations](mobiledocumentanyofdatarequest/mobiledocumentrequest-implementations.md)

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
- [struct MobileDocumentAnyOfRawDataRequest](mobiledocumentanyofrawdatarequest.md)
  A type that describes a raw data request for any mobile document from a group of requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofdatarequest)*