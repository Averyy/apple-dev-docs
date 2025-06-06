# isProximityMonitoringEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether proximity monitoring is enabled.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isProximityMonitoringEnabled: Bool { get set }
```

#### Discussion

Enable proximity monitoring only when your application needs to be notified of changes to the proximity state. Otherwise, disable proximity monitoring. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

Not all iOS devices have proximity sensors. To determine if proximity monitoring is available, attempt to enable it. If the value of the [`isProximityMonitoringEnabled`](uidevice/isproximitymonitoringenabled.md) property remains [`false`](https://developer.apple.com/documentation/swift/false), proximity monitoring isn’t available.

## See Also

- [var proximityState: Bool](uidevice/proximitystate.md)
  A Boolean value that indicates whether the proximity sensor is close to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/isproximitymonitoringenabled)*