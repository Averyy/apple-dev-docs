# NIAlgorithmConvergence

**Framework**: Nearby Interaction  
**Kind**: class

An object that provides the state and reason for user coaching recommendations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
class NIAlgorithmConvergence
```

#### Overview

This class conveys the current state of the framework’s Camera Assistance feature when you turn on [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md). When the status indicates that user action is required to achieve the highest-quality results, instances of this class identify specific actions the user can do to help. To improve the status, the app needs to coach the user such as by presenting instructional text. The information you provide tells the user, for example, where and at what speed to pan the device around the environment.

To listen for the convergence status, implement [`session(_:didUpdateAlgorithmConvergence:for:)`](nisessiondelegate/session(_:didupdatealgorithmconvergence:for:).md).

## Topics

### Determining convergence state
- [var status: NIAlgorithmConvergenceStatus](nialgorithmconvergence/status-654t.md)
  The current state of the framework’s Camera Assistance feature.
### Initializers
- [init?(coder: NSCoder)](nialgorithmconvergence/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Finding devices with precision](finding-devices-with-precision.md)
  Leverage the spatial awareness of ARKit and Apple Ultra Wideband Chips in your app to guide users to a nearby device.
- [enum NIAlgorithmConvergenceStatus](nialgorithmconvergencestatus-2fnve.md)
  The possible states of Camera Assistance.
- [Algorithm Convergence Status](algorithm-convergence-status.md)
  The possible Objective-C states of Camera Assistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergence)*