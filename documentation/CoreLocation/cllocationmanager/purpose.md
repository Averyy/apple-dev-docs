# purpose

**Framework**: Core Location  
**Kind**: property

An app-provided string that describes the reason for using location services.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var purpose: String? { get set }
```

#### Discussion

If this property isn’t `nil` and the system needs to ask for the user’s consent to use location services, it displays the provided string. You can use this string to explain why your app is using location services.

You must set the value of this property prior to starting any location services. Because the string is ultimately displayed to the user, you should always load it from a localized strings file.

## See Also

- [var headingAvailable: Bool](cllocationmanager/headingavailable-swift.property.md)
  A Boolean value indicating whether the location manager is able to generate heading-related events.
- [var locationServicesEnabled: Bool](cllocationmanager/locationservicesenabled-swift.property.md)
  A Boolean value indicating whether location services are enabled on the device.
- [var rangedRegions: Set<CLRegion>](cllocationmanager/rangedregions.md)
  The set of regions currently being tracked using ranging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/purpose)*