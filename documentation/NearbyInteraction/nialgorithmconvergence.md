# NIAlgorithmConvergence

**Framework**: Nearby Interaction  
**Kind**: class  
**Role**: Class

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

```objc
@interface NIAlgorithmConvergence : NSObject
```

#### Overview

This class conveys the current state of the framework’s Camera Assistance feature when you turn on [`isCameraAssistanceEnabled`](./ninearbypeerconfiguration/iscameraassistanceenabled.md). When the status indicates that user action is required to achieve the highest-quality results, instances of this class identify specific actions the user can do to help. To improve the status, the app needs to coach the user such as by presenting instructional text. The information you provide tells the user, for example, where and at what speed to pan the device around the environment.

To listen for the convergence status, implement [`session(_:didUpdateAlgorithmConvergence:for:)`](./nisessiondelegate/session%28_,didupdatealgorithmconvergence,for%29.md).

## Topics

### Determining convergence state
- [var status: NIAlgorithmConvergenceStatus](./nialgorithmconvergence/status-654t.md)
  The current state of the framework’s Camera Assistance feature.
### Initializers
- [init?(coder: NSCoder)](./nialgorithmconvergence/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergence)*