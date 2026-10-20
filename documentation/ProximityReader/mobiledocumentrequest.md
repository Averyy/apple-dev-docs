# MobileDocumentRequest

**Framework**: ProximityReader  
**Kind**: protocol  
**Role**: Protocol

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

- [Adopting the Verifier API in your iPhone app](./adopting-the-verifier-api-in-your-iphone-app.md)

## Topics

### Mobile driver’s license display request
- [struct MobileDriversLicenseDisplayRequest](./mobiledriverslicensedisplayrequest.md)
  A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [static func displayDriversLicense([MobileDriversLicenseDisplayRequest.Element], options: MobileDriversLicenseDisplayRequest.Options) -> Self](./mobiledocumentrequest/displaydriverslicense%28_,options%29.md)
  A request that displays driver’s license elements onscreen.
### Mobile driver’s license data request
- [struct MobileDriversLicenseDataRequest](./mobiledriverslicensedatarequest.md)
  A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.
- [static func driversLicenseData(retaining: [MobileDriversLicenseDataRequest.Element], notRetaining: [MobileDriversLicenseDataRequest.Element]) -> Self](./mobiledocumentrequest/driverslicensedata%28retaining,notretaining%29.md)
  A request which retrieves elements from the holder and returns the validated document elements.
### Mobile driver’s license raw data request
- [struct MobileDriversLicenseRawDataRequest](./mobiledriverslicenserawdatarequest.md)
  A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.
- [static func driversLicenseRawData(retaining: [MobileDriversLicenseRawDataRequest.Element], notRetaining: [MobileDriversLicenseRawDataRequest.Element]) -> Self](./mobiledocumentrequest/driverslicenserawdata%28retaining,notretaining%29.md)
  A request which retrieves mobile driver’s license elements from the holder and returns the raw response data for processing.
### National ID card display request
- [struct MobileNationalIDCardDisplayRequest](./mobilenationalidcarddisplayrequest.md)
  A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [static func nationalIDCard(region: Locale.Region, [MobileNationalIDCardDisplayRequest.Element], options: MobileNationalIDCardDisplayRequest.Options) -> Self](./mobiledocumentrequest/nationalidcard%28region,_,options%29.md)
  A request that displays national ID card elements onscreen.
### National ID card license data request
- [struct MobileNationalIDCardDataRequest](./mobilenationalidcarddatarequest.md)
  A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- [static func nationalIDCardData(region: Locale.Region, retaining: [MobileNationalIDCardDataRequest.Element], notRetaining: [MobileNationalIDCardDataRequest.Element]) -> Self](./mobiledocumentrequest/nationalidcarddata%28region,retaining,notretaining%29.md)
  A request which retrieves elements from the holder and returns the validated document elements.
### National ID card license raw data request
- [struct MobileNationalIDCardRawDataRequest](./mobilenationalidcardrawdatarequest.md)
  A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- [static func nationalIDCardRawData(region: Locale.Region, retaining: [MobileNationalIDCardRawDataRequest.Element], notRetaining: [MobileNationalIDCardRawDataRequest.Element]) -> Self](./mobiledocumentrequest/nationalidcardrawdata%28region,retaining,notretaining%29.md)
  A request which retrieves mobile national ID card elements from the holder and returns the raw response data for processing.
### Associated Types
- [associatedtype Response : Hashable, Sendable](./mobiledocumentrequest/response.md)
  A type that represents the response type of the request.
### Type Methods
- [static func displayDocument([MobileDocumentDisplayRequest.Element], options: MobileDocumentDisplayRequest.Options) -> Self](./mobiledocumentrequest/displaydocument%28_,options%29.md)
  A request that displays document elements onscreen.
- [static func driversLicenseRawData(retaining: [MobileDriversLicenseRawDataRequest.Element], notRetaining: [MobileDriversLicenseRawDataRequest.Element], issuerIdentifiers: [Data]) -> Self](./mobiledocumentrequest/driverslicenserawdata%28retaining,notretaining,issueridentifiers%29.md)
  A request which retrieves mobile driver’s license elements from the holder and returns the raw response data for processing.
- [static func nationalIDCardRawData(region: Locale.Region, retaining: [MobileNationalIDCardRawDataRequest.Element], notRetaining: [MobileNationalIDCardRawDataRequest.Element], issuerIdentifiers: [Data]) -> Self](./mobiledocumentrequest/nationalidcardrawdata%28region,retaining,notretaining,issueridentifiers%29.md)
  A request which retrieves mobile national ID card elements from the holder and returns the raw response data for processing.
- [static func photoIDData(retaining: [MobilePhotoIDDataRequest.Element], notRetaining: [MobilePhotoIDDataRequest.Element]) -> Self](./mobiledocumentrequest/photoiddata%28retaining,notretaining%29.md)
  A request which retrieves elements from the holder and returns the validated document elements.
- [static func photoIDRawData(retaining: [MobilePhotoIDRawDataRequest.Element], notRetaining: [MobilePhotoIDRawDataRequest.Element]) -> Self](./mobiledocumentrequest/photoidrawdata%28retaining,notretaining%29.md)
  A request which retrieves photo ID elements from the holder and returns the raw response data for processing.
- [static func photoIDRawData(retaining: [MobilePhotoIDRawDataRequest.Element], notRetaining: [MobilePhotoIDRawDataRequest.Element], issuerIdentifiers: [Data]) -> Self](./mobiledocumentrequest/photoidrawdata%28retaining,notretaining,issueridentifiers%29.md)
  A request which retrieves photo ID elements from the holder and returns the raw response data for processing.

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Inherited By
- [MobileDocumentDataRequest](./mobiledocumentdatarequest.md)
- [MobileDocumentRawDataRequest](./mobiledocumentrawdatarequest.md)
### Conforming Types
- [MobileDocumentAnyOfDataRequest](./mobiledocumentanyofdatarequest.md)
- [MobileDocumentAnyOfRawDataRequest](./mobiledocumentanyofrawdatarequest.md)
- [MobileDocumentDisplayRequest](./mobiledocumentdisplayrequest.md)
- [MobileDriversLicenseDataRequest](./mobiledriverslicensedatarequest.md)
- [MobileDriversLicenseDisplayRequest](./mobiledriverslicensedisplayrequest.md)
- [MobileDriversLicenseRawDataRequest](./mobiledriverslicenserawdatarequest.md)
- [MobileNationalIDCardDataRequest](./mobilenationalidcarddatarequest.md)
- [MobileNationalIDCardDisplayRequest](./mobilenationalidcarddisplayrequest.md)
- [MobileNationalIDCardRawDataRequest](./mobilenationalidcardrawdatarequest.md)
- [MobilePhotoIDDataRequest](./mobilephotoiddatarequest.md)
- [MobilePhotoIDRawDataRequest](./mobilephotoidrawdatarequest.md)

## See Also

### Mobile document requests
- [struct MobileDriversLicenseDisplayRequest](./mobiledriverslicensedisplayrequest.md)
  A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [struct MobileDriversLicenseDataRequest](./mobiledriverslicensedatarequest.md)
  A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileDriversLicenseRawDataRequest](./mobiledriverslicenserawdatarequest.md)
  A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileNationalIDCardDisplayRequest](./mobilenationalidcarddisplayrequest.md)
  A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [struct MobileNationalIDCardDataRequest](./mobilenationalidcarddatarequest.md)
  A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileNationalIDCardRawDataRequest](./mobilenationalidcardrawdatarequest.md)
  A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileDocumentDisplayRequest](./mobiledocumentdisplayrequest.md)
  A mobile document request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [protocol MobileDocumentDataRequest](./mobiledocumentdatarequest.md)
  A type that represents a mobile document data request.
- [protocol MobileDocumentRawDataRequest](./mobiledocumentrawdatarequest.md)
  A type that represents a mobile document raw data request.
- [struct MobilePhotoIDDataRequest](./mobilephotoiddatarequest.md)
  A photo ID request that retrieves elements from the holder and returns the validated document elements.
- [struct MobilePhotoIDRawDataRequest](./mobilephotoidrawdatarequest.md)
  A photo ID request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileDocumentAnyOfDataRequest](./mobiledocumentanyofdatarequest.md)
  A type that describes a data request for any mobile document from a group of requests.
- [struct MobileDocumentAnyOfRawDataRequest](./mobiledocumentanyofrawdatarequest.md)
  A type that describes a raw data request for any mobile document from a group of requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest)*