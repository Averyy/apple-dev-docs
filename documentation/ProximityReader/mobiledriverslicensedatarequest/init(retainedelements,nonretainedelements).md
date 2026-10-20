# init(retainedElements:nonRetainedElements:)

**Framework**: ProximityReader  
**Kind**: init  
**Role**: Initializer

Returns a mobile driver’s license data request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
init(retainedElements: [MobileDriversLicenseDataRequest.Element] = [], nonRetainedElements: [MobileDriversLicenseDataRequest.Element] = [])
```

## See Also

### Creating a data request
- [var retainedElements: [MobileDriversLicenseDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileDriversLicenseDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [MobileDriversLicenseDataRequest.Element](./element.md)
  A type that represents an element you can request from a mobile driver’s license.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest/init(retainedelements:nonretainedelements:))*