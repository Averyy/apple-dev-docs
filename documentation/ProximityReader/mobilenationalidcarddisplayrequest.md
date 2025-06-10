# MobileNationalIDCardDisplayRequest

**Framework**: ProximityReader  
**Kind**: struct

A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct MobileNationalIDCardDisplayRequest
```

## Topics

### Creating a display request
- [init(region: Locale.Region, elements: [MobileNationalIDCardDisplayRequest.Element], options: MobileNationalIDCardDisplayRequest.Options)](mobilenationalidcarddisplayrequest/init(region:elements:options:).md)
  Creates a new mobile national ID card display request.
### Determining the region availability
- [static func isSupportedRegion(Locale.Region) -> Bool](mobilenationalidcarddisplayrequest/issupportedregion(_:).md)
  Returns a Boolean value that indicates whether you can make a request for the specified region.
### Configuring the request details
- [var region: Locale.Region](mobilenationalidcarddisplayrequest/region.md)
  The region of the document you’re requesting.
- [var elements: [MobileNationalIDCardDisplayRequest.Element]](mobilenationalidcarddisplayrequest/elements.md)
  The document elements you’re requesting.
- [MobileNationalIDCardDisplayRequest.Element](mobilenationalidcarddisplayrequest/element.md)
  A type that represents an element you can request from a mobile national ID card.
- [var options: MobileNationalIDCardDisplayRequest.Options](mobilenationalidcarddisplayrequest/options-swift.property.md)
  An object that customizes how to perform a display request.
- [MobileNationalIDCardDisplayRequest.Options](mobilenationalidcarddisplayrequest/options-swift.struct.md)
  An object that customizes how to perform a display request.
### Handling the response
- [MobileNationalIDCardDisplayRequest.Response](mobilenationalidcarddisplayrequest/response.md)
  A type that contains the response information from a successful mobile national ID card display request.
### Operators
- [static func == (MobileNationalIDCardDisplayRequest, MobileNationalIDCardDisplayRequest) -> Bool](mobilenationalidcarddisplayrequest/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobilenationalidcarddisplayrequest/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcarddisplayrequest/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobilenationalidcarddisplayrequest/equatable-implementations.md)
- [MobileDocumentRequest Implementations](mobilenationalidcarddisplayrequest/mobiledocumentrequest-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest)*