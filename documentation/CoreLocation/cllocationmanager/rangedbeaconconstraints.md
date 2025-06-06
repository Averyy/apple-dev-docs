# rangedBeaconConstraints

**Framework**: Core Location  
**Kind**: property

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

## See Also

- [func startRangingBeacons(satisfying: CLBeaconIdentityConstraint)](cllocationmanager/startrangingbeacons(satisfying:).md)
  Starts the delivery of notifications for the specified beacon constraints.
- [func stopRangingBeacons(satisfying: CLBeaconIdentityConstraint)](cllocationmanager/stoprangingbeacons(satisfying:).md)
  Stops the delivery of notifications for the specified beacon constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/rangedbeaconconstraints)*