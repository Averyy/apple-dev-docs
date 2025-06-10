# MobileNationalIDCardRawDataRequest

**Framework**: ProximityReader  
**Kind**: struct

A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct MobileNationalIDCardRawDataRequest
```

## Topics

### Creating a raw data request
- [init(region: Locale.Region, retainedElements: [MobileNationalIDCardRawDataRequest.Element], nonRetainedElements: [MobileNationalIDCardRawDataRequest.Element])](mobilenationalidcardrawdatarequest/init(region:retainedelements:nonretainedelements:).md)
  Creates a mobile national ID card raw data request.
### Determining the region availability
- [static func isSupportedRegion(Locale.Region) -> Bool](mobilenationalidcardrawdatarequest/issupportedregion(_:).md)
  Returns a Boolean value that indicates whether you can make a request for the specified region.
### Configuring the request details
- [var region: Locale.Region](mobilenationalidcardrawdatarequest/region.md)
  The region of the document you’re requesting.
- [var retainedElements: [MobileNationalIDCardRawDataRequest.Element]](mobilenationalidcardrawdatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileNationalIDCardRawDataRequest.Element]](mobilenationalidcardrawdatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.
- [MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element.md)
  A type representing an element that you can request from a mobile national ID card.
### Handling the response
- [MobileNationalIDCardRawDataRequest.Response](mobilenationalidcardrawdatarequest/response.md)
  A type that contains the response information from a successful mobile national ID card raw data request.
### Operators
- [static func == (MobileNationalIDCardRawDataRequest, MobileNationalIDCardRawDataRequest) -> Bool](mobilenationalidcardrawdatarequest/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobilenationalidcardrawdatarequest/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcardrawdatarequest/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobilenationalidcardrawdatarequest/equatable-implementations.md)
- [MobileDocumentRequest Implementations](mobilenationalidcardrawdatarequest/mobiledocumentrequest-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest)*