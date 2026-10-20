# uuid

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The UUID value from the beacon identity constraint that defines the beacon region.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * UUID;
```

#### Discussion

Typically, the UUID is unique to your company and is the same for all of the beacons that you install. Use the [`major`](./major.md) and [`minor`](./minor.md) values to differentiate the beacons in your installation.

## See Also

### Getting the beacon identity
- [var major: NSNumber?](./major.md)
  The major value from the beacon identity constraint that defines the beacon region.
- [var minor: NSNumber?](./minor.md)
  The minor value from the beacon identity constraint that defines the beacon region.
- [var beaconIdentityConstraint: CLBeaconIdentityConstraint](./beaconidentityconstraint.md)
  The beacon identity constraint that defines the beacon region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/uuid)*