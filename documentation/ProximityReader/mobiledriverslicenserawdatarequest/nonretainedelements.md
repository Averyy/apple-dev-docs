# nonRetainedElements

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element]
```

## See Also

### Creating a raw data request
- [init(retainedElements: [MobileDriversLicenseRawDataRequest.Element], nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element])](./init%28retainedelements,nonretainedelements%29.md)
  Returns a mobile driver’s license raw data request.
- [var retainedElements: [MobileDriversLicenseRawDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [MobileDriversLicenseRawDataRequest.Element](./element.md)
  A type representing an element that you can request from a mobile driver’s license.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest/nonretainedelements)*