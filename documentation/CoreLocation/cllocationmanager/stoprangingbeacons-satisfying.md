# stopRangingBeacons(satisfying:)

**Framework**: Core Location  
**Kind**: method

Stops the delivery of notifications for the specified beacon constraints.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
func stopRangingBeacons(satisfying constraint: CLBeaconIdentityConstraint)
```

## Parameters

- `constraint`: A   constraint.

## See Also

- [func startRangingBeacons(satisfying: CLBeaconIdentityConstraint)](cllocationmanager/startrangingbeacons(satisfying:).md)
  Starts the delivery of notifications for the specified beacon constraints.
- [var rangedBeaconConstraints: Set<CLBeaconIdentityConstraint>](cllocationmanager/rangedbeaconconstraints.md)
  The set of beacon constraints currently being tracked using ranging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/stoprangingbeacons(satisfying:))*