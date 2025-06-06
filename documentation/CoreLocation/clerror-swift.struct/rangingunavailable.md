# rangingUnavailable

**Framework**: Core Location  
**Kind**: property

A constant that indicates ranging is disabled.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var rangingUnavailable: CLError.Code { get }
```

#### Discussion

This error might occur if the device is in Airplane mode or if Bluetooth or location services are disabled.

## See Also

- [static var locationUnknown: CLError.Code](clerror-swift.struct/locationunknown.md)
  A constant that indicates the location manager was unable to obtain a location value right now.
- [static var denied: CLError.Code](clerror-swift.struct/denied.md)
  A constant that indicates the user denied access to the location service.
- [static var promptDeclined: CLError.Code](clerror-swift.struct/promptdeclined.md)
  A constant that indicates the user didn’t grant the requested temporary authorization.
- [static var network: CLError.Code](clerror-swift.struct/network.md)
  A constant that indicates the network was unavailable or a network error occurred.
- [static var headingFailure: CLError.Code](clerror-swift.struct/headingfailure.md)
  A constant that indicates the location manager can’t determine the heading.
- [static var rangingFailure: CLError.Code](clerror-swift.struct/rangingfailure.md)
  A constant that indicates a general ranging error occurred.
- [CLError.Code](clerror-swift.struct/code.md)
  Error codes returned by the location manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/rangingunavailable)*