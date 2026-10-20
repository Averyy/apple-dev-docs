# isProximityMonitoringEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether proximity monitoring is enabled.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isProximityMonitoringEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isProximityMonitoringEnabled) BOOL proximityMonitoringEnabled;
```

#### Discussion

Enable proximity monitoring only when your application needs to be notified of changes to the proximity state. Otherwise, disable proximity monitoring. The default value is [`false`](../../Swift/false.md).

Not all iOS devices have proximity sensors. To determine if proximity monitoring is available, attempt to enable it. If the value of the [`isProximityMonitoringEnabled`](./isproximitymonitoringenabled.md) property remains [`false`](../../Swift/false.md), proximity monitoring isn’t available.

## See Also

### Using the proximity sensor
- [var proximityState: Bool](./proximitystate.md)
  A Boolean value that indicates whether the proximity sensor is close to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/isproximitymonitoringenabled)*