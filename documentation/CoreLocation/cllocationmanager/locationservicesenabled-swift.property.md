# locationServicesEnabled

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether location services are enabled on the device.

**Availability**:
- macOS 10.15+ - Deprecated in 10.15

> **Deprecated**: Use the [`locationServicesEnabled()`](./locationservicesenabled%28%29.md) class method instead.

## Declaration

```swift
var locationServicesEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL locationServicesEnabled;
```

#### Discussion

In iOS, the user can enable or disable location services using the controls in Settings > Location Services. In macOS, the user can enable or disable location services from the Security & Privacy system preference.

If this property contains the value [`false`](../../Swift/false.md) and you start location updates anyway, the Core Location framework prompts the user with a confirmation alert asking whether location services should be reenabled.

##### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Properties
- [var headingAvailable: Bool](./headingavailable-swift.property.md)
  A Boolean value indicating whether the location manager is able to generate heading-related events.
- [var purpose: String?](./purpose.md)
  An app-provided string that describes the reason for using location services.
- [var rangedRegions: Set<CLRegion>](./rangedregions.md)
  The set of regions currently being tracked using ranging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/locationservicesenabled-swift.property)*