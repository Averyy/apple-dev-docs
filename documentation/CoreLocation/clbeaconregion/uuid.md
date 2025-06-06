# uuid

**Framework**: Core Location  
**Kind**: property

The UUID value from the beacon identity constraint that defines the beacon region.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var uuid: UUID { get }
```

#### Discussion

Typically, the UUID is unique to your company and is the same for all of the beacons that you install. Use the [`major`](clbeaconregion/major.md) and [`minor`](clbeaconregion/minor.md) values to differentiate the beacons in your installation.

## See Also

- [var major: NSNumber?](clbeaconregion/major.md)
  The major value from the beacon identity constraint that defines the beacon region.
- [var minor: NSNumber?](clbeaconregion/minor.md)
  The minor value from the beacon identity constraint that defines the beacon region.
- [var beaconIdentityConstraint: CLBeaconIdentityConstraint](clbeaconregion/beaconidentityconstraint.md)
  The beacon identity constraint that defines the beacon region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/uuid)*