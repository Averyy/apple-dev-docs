# driversLicenseRawData(retaining:notRetaining:issuerIdentifiers:)

**Framework**: ProximityReader  
**Kind**: method

A request which retrieves mobile driver’s license elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
static func driversLicenseRawData(retaining retainedElements: [MobileDriversLicenseRawDataRequest.Element] = [], notRetaining nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element] = [], issuerIdentifiers: [Data] = []) -> Self
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest/driverslicenserawdata(retaining:notretaining:issueridentifiers:))*