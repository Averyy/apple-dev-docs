# beaconIdentityConstraint

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The beacon identity constraint that defines the beacon region.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

## Declaration

```swift
@NSCopying
var beaconIdentityConstraint: CLBeaconIdentityConstraint { get }
```

```objc
@property (nonatomic, copy, readonly) CLBeaconIdentityConstraint * beaconIdentityConstraint;
```

## See Also

### Getting the beacon identity
- [var uuid: UUID](./uuid.md)
  The UUID value from the beacon identity constraint that defines the beacon region.
- [var major: NSNumber?](./major.md)
  The major value from the beacon identity constraint that defines the beacon region.
- [var minor: NSNumber?](./minor.md)
  The minor value from the beacon identity constraint that defines the beacon region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/beaconidentityconstraint)*