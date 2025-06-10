# MobileDriversLicenseDisplayRequest

**Framework**: ProximityReader  
**Kind**: struct

A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct MobileDriversLicenseDisplayRequest
```

## Topics

### Creating a display request
- [init(elements: [MobileDriversLicenseDisplayRequest.Element], options: MobileDriversLicenseDisplayRequest.Options)](mobiledriverslicensedisplayrequest/init(elements:options:).md)
  Creates a new mobile driver’s license display request.
- [var elements: [MobileDriversLicenseDisplayRequest.Element]](mobiledriverslicensedisplayrequest/elements.md)
  The document elements you’re requesting.
- [MobileDriversLicenseDisplayRequest.Element](mobiledriverslicensedisplayrequest/element.md)
  A type that represents an element you can request from a mobile driver’s license.
### Configuring a display request
- [var options: MobileDriversLicenseDisplayRequest.Options](mobiledriverslicensedisplayrequest/options-swift.property.md)
  An object that customizes how to perform a display request.
- [MobileDriversLicenseDisplayRequest.Options](mobiledriverslicensedisplayrequest/options-swift.struct.md)
  An object that customizes how to perform a display request.
### Handling the response
- [MobileDriversLicenseDisplayRequest.Response](mobiledriverslicensedisplayrequest/response.md)
  A type that contains the response information from a successful mobile driver’s license display request.
### Operators
- [static func == (MobileDriversLicenseDisplayRequest, MobileDriversLicenseDisplayRequest) -> Bool](mobiledriverslicensedisplayrequest/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledriverslicensedisplayrequest/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicensedisplayrequest/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledriverslicensedisplayrequest/equatable-implementations.md)
- [MobileDocumentRequest Implementations](mobiledriverslicensedisplayrequest/mobiledocumentrequest-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MobileDocumentRequest](mobiledocumentrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [struct MobileDocumentAnyOfDataRequest](mobiledocumentanyofdatarequest.md)
  A type that describes a data request for any mobile document from a group of requests.
- [struct MobileDocumentAnyOfRawDataRequest](mobiledocumentanyofrawdatarequest.md)
  A type that describes a raw data request for any mobile document from a group of requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest)*