# MobileDocumentRequest

**Framework**: ProximityReader  
**Kind**: protocol

A type that represents a mobile document request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
protocol MobileDocumentRequest : Hashable, Sendable
```

## Mentions

- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md)

## Topics

### Mobile driver’s license display request
- [struct MobileDriversLicenseDisplayRequest](mobiledriverslicensedisplayrequest.md)
  A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [static func displayDriversLicense([MobileDriversLicenseDisplayRequest.Element], options: MobileDriversLicenseDisplayRequest.Options) -> Self](mobiledocumentrequest/displaydriverslicense(_:options:).md)
  A request that displays driver’s license elements onscreen.
### Mobile driver’s license data request
- [struct MobileDriversLicenseDataRequest](mobiledriverslicensedatarequest.md)
  A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.
- [static func driversLicenseData(retaining: [MobileDriversLicenseDataRequest.Element], notRetaining: [MobileDriversLicenseDataRequest.Element]) -> Self](mobiledocumentrequest/driverslicensedata(retaining:notretaining:).md)
  A request which retrieves elements from the holder and returns the validated document elements.
### Mobile driver’s license raw data request
- [struct MobileDriversLicenseRawDataRequest](mobiledriverslicenserawdatarequest.md)
  A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.
- [static func driversLicenseRawData(retaining: [MobileDriversLicenseRawDataRequest.Element], notRetaining: [MobileDriversLicenseRawDataRequest.Element]) -> Self](mobiledocumentrequest/driverslicenserawdata(retaining:notretaining:).md)
  A request which retrieves mobile driver’s license elements from the holder and returns the raw response data for processing.
### National ID card display request
- [struct MobileNationalIDCardDisplayRequest](mobilenationalidcarddisplayrequest.md)
  A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [static func nationalIDCard(region: Locale.Region, [MobileNationalIDCardDisplayRequest.Element], options: MobileNationalIDCardDisplayRequest.Options) -> Self](mobiledocumentrequest/nationalidcard(region:_:options:).md)
  A request that displays national ID card elements onscreen.
### National ID card license data request
- [struct MobileNationalIDCardDataRequest](mobilenationalidcarddatarequest.md)
  A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- [static func nationalIDCardData(region: Locale.Region, retaining: [MobileNationalIDCardDataRequest.Element], notRetaining: [MobileNationalIDCardDataRequest.Element]) -> Self](mobiledocumentrequest/nationalidcarddata(region:retaining:notretaining:).md)
  A request which retrieves elements from the holder and returns the validated document elements.
### National ID card license raw data request
- [struct MobileNationalIDCardRawDataRequest](mobilenationalidcardrawdatarequest.md)
  A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- [static func nationalIDCardRawData(region: Locale.Region, retaining: [MobileNationalIDCardRawDataRequest.Element], notRetaining: [MobileNationalIDCardRawDataRequest.Element]) -> Self](mobiledocumentrequest/nationalidcardrawdata(region:retaining:notretaining:).md)
  A request which retrieves mobile national ID card elements from the holder and returns the raw response data for processing.
### Associated Types
- [associatedtype Response : Hashable, Sendable](mobiledocumentrequest/response.md)
  A type that represents the response type of the request.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [MobileDriversLicenseDataRequest](mobiledriverslicensedatarequest.md)
- [MobileDriversLicenseDisplayRequest](mobiledriverslicensedisplayrequest.md)
- [MobileDriversLicenseRawDataRequest](mobiledriverslicenserawdatarequest.md)
- [MobileNationalIDCardDataRequest](mobilenationalidcarddatarequest.md)
- [MobileNationalIDCardDisplayRequest](mobilenationalidcarddisplayrequest.md)
- [MobileNationalIDCardRawDataRequest](mobilenationalidcardrawdatarequest.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest)*