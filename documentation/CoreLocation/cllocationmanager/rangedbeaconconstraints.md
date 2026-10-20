# rangedBeaconConstraints

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The set of beacon constraints currently being tracked using ranging.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var rangedBeaconConstraints: Set<CLBeaconIdentityConstraint> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<CLBeaconIdentityConstraint *> * rangedBeaconConstraints;
```

## See Also

### Performing beacon ranging
- [func startRangingBeacons(satisfying: CLBeaconIdentityConstraint)](./startrangingbeacons%28satisfying%29.md)
  Starts the delivery of notifications for the specified beacon constraints.
- [func stopRangingBeacons(satisfying: CLBeaconIdentityConstraint)](./stoprangingbeacons%28satisfying%29.md)
  Stops the delivery of notifications for the specified beacon constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/rangedbeaconconstraints)*