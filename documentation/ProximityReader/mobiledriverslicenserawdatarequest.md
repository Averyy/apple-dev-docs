# MobileDriversLicenseRawDataRequest

**Framework**: ProximityReader  
**Kind**: struct

A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct MobileDriversLicenseRawDataRequest
```

## Topics

### Creating a raw data request
- [init(retainedElements: [MobileDriversLicenseRawDataRequest.Element], nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element])](mobiledriverslicenserawdatarequest/init(retainedelements:nonretainedelements:).md)
  Returns a mobile driver’s license raw data request.
- [var retainedElements: [MobileDriversLicenseRawDataRequest.Element]](mobiledriverslicenserawdatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element]](mobiledriverslicenserawdatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.
- [MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element.md)
  A type representing an element that you can request from a mobile driver’s license.
### Handling the response
- [MobileDriversLicenseRawDataRequest.Response](mobiledriverslicenserawdatarequest/response.md)
  A type that contains the response information from a successful mobile driver’s license raw data request.
### Operators
- [static func == (MobileDriversLicenseRawDataRequest, MobileDriversLicenseRawDataRequest) -> Bool](mobiledriverslicenserawdatarequest/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledriverslicenserawdatarequest/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicenserawdatarequest/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledriverslicenserawdatarequest/equatable-implementations.md)
- [MobileDocumentRequest Implementations](mobiledriverslicenserawdatarequest/mobiledocumentrequest-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MobileDocumentRequest](mobiledocumentrequest.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MobileDriversLicenseDisplayRequest](mobiledriverslicensedisplayrequest.md)
  A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [struct MobileDriversLicenseDataRequest](mobiledriverslicensedatarequest.md)
  A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileNationalIDCardDisplayRequest](mobilenationalidcarddisplayrequest.md)
  A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [struct MobileNationalIDCardDataRequest](mobilenationalidcarddatarequest.md)
  A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileNationalIDCardRawDataRequest](mobilenationalidcardrawdatarequest.md)
  A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- [protocol MobileDocumentRequest](mobiledocumentrequest.md)
  A type that represents a mobile document request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest)*