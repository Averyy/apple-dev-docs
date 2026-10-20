# driversLicenseData(retaining:notRetaining:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Type Method

A request which retrieves elements from the holder and returns the validated document elements.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
static func driversLicenseData(retaining retainedElements: [MobileDriversLicenseDataRequest.Element], notRetaining nonRetainedElements: [MobileDriversLicenseDataRequest.Element]) -> Self
```

Available when `Self` is `MobileDriversLicenseDataRequest`.

## See Also

### Mobile driver’s license data request
- [struct MobileDriversLicenseDataRequest](../mobiledriverslicensedatarequest.md)
  A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest/driverslicensedata(retaining:notretaining:))*