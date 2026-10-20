# CLBeaconIdentityConstraint

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

Identity characteristics that can match one or more beacons.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: Use [`CLBeaconIdentityCondition`](./clbeaconidentitycondition.md) instead.

## Declaration

```swift
class CLBeaconIdentityConstraint
```

```objc
@interface CLBeaconIdentityConstraint : CLBeaconIdentityCondition
```

#### Overview

A constraint specifies beacon identity characteristics. Use constraints to check for matching beacons by comparing the beacon’s identity characteristics ([`uuid`](./clbeacon/uuid.md), [`major`](./clbeacon/major.md), and [`minor`](./clbeacon/minor.md)) to those in the constraint.

Constraints always specify a UUID value, but the major and minor values are optional. A beacon satisfies the constraint if all three identity characteristics of the beacon match the same characteristic of the constraint. Major and minor characteristics are wildcards if they have no value. A major or minor wildcard value matches any value in the beacon’s corresponding characteristic.

## Topics

### Getting the beacon identity
- [var major: UInt16?](./clbeaconidentityconstraint/major.md)
  The constraint’s value for the major identity characteristic.
- [var minor: UInt16?](./clbeaconidentityconstraint/minor.md)
  The constraint’s value for the minor identity characteristic.

## Relationships

### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class CLBeaconRegion](./clbeaconregion.md)
  A region for detecting the presence of iBeacon devices.
- [class CLCircularRegion](./clcircularregion.md)
  A circular geographic region that a center point and radius deine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconidentityconstraint)*