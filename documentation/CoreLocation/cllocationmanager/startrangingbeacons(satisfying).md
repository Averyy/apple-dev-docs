# startRangingBeacons(satisfying:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Starts the delivery of notifications for the specified beacon constraints.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
func startRangingBeacons(satisfying constraint: CLBeaconIdentityConstraint)
```

```objc
- (void) startRangingBeaconsSatisfyingConstraint:(CLBeaconIdentityConstraint *) constraint;
```

## Parameters

- `constraint`: A [`CLBeaconIdentityConstraint`](../clbeaconidentityconstraint.md) constraint.

## See Also

### Performing beacon ranging
- [func stopRangingBeacons(satisfying: CLBeaconIdentityConstraint)](./stoprangingbeacons%28satisfying%29.md)
  Stops the delivery of notifications for the specified beacon constraints.
- [var rangedBeaconConstraints: Set<CLBeaconIdentityConstraint>](./rangedbeaconconstraints.md)
  The set of beacon constraints currently being tracked using ranging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startrangingbeacons(satisfying:))*