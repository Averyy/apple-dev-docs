# init(retainedElements:nonRetainedElements:)

**Framework**: ProximityReader  
**Kind**: init  
**Role**: Initializer

Returns a mobile driver’s license raw data request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
init(retainedElements: [MobileDriversLicenseRawDataRequest.Element] = [], nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element] = [])
```

## See Also

### Creating a raw data request
- [var retainedElements: [MobileDriversLicenseRawDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.
- [MobileDriversLicenseRawDataRequest.Element](./element.md)
  A type representing an element that you can request from a mobile driver’s license.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest/init(retainedelements:nonretainedelements:))*