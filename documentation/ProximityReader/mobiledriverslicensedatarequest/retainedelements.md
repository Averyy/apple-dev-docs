# retainedElements

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The document elements you’re requesting and intend to retain for an indefinite period of time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var retainedElements: [MobileDriversLicenseDataRequest.Element]
```

## See Also

### Creating a data request
- [init(retainedElements: [MobileDriversLicenseDataRequest.Element], nonRetainedElements: [MobileDriversLicenseDataRequest.Element])](./init%28retainedelements,nonretainedelements%29.md)
  Returns a mobile driver’s license data request.
- [var nonRetainedElements: [MobileDriversLicenseDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [MobileDriversLicenseDataRequest.Element](./element.md)
  A type that represents an element you can request from a mobile driver’s license.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest/retainedelements)*