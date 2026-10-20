# driversLicenseRawData(retaining:notRetaining:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Type Method

A request which retrieves mobile driver’s license elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
static func driversLicenseRawData(retaining retainedElements: [MobileDriversLicenseRawDataRequest.Element], notRetaining nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element]) -> Self
```

Available when `Self` is `MobileDriversLicenseRawDataRequest`.

## See Also

### Mobile driver’s license raw data request
- [struct MobileDriversLicenseRawDataRequest](../mobiledriverslicenserawdatarequest.md)
  A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest/driverslicenserawdata(retaining:notretaining:))*