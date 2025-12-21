# locationServicesEnabled

**Framework**: Core Location  
**Kind**: property

A Boolean value indicating whether location services are enabled on the device.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var locationServicesEnabled: Bool { get }
```

#### Discussion

In iOS, the user can enable or disable location services using the controls in Settings > Location Services. In macOS, the user can enable or disable location services from the Security & Privacy system preference.

If this property contains the value [`false`](https://developer.apple.com/documentation/Swift/false) and you start location updates anyway, the Core Location framework prompts the user with a confirmation alert asking whether location services should be reenabled.

##### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

- [var headingAvailable: Bool](cllocationmanager/headingavailable-swift.property.md)
  A Boolean value indicating whether the location manager is able to generate heading-related events.
- [var purpose: String?](cllocationmanager/purpose.md)
  An app-provided string that describes the reason for using location services.
- [var rangedRegions: Set<CLRegion>](cllocationmanager/rangedregions.md)
  The set of regions currently being tracked using ranging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/locationservicesenabled-swift.property)*