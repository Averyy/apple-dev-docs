# authorizationStatus

**Framework**: SensorKit  
**Kind**: property

The current authorization status for accessing the sensor data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
final var authorizationStatus: SRAuthorizationStatus { get }
```

#### Return Value

Current `SRAuthorizationStatus` indicating whether the app has permission to access the sensor data.

#### Discussion

This observable property automatically updates when the user changes sensor permissions in system settings, allowing to react to authorization changes in real-time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srreader/authorizationstatus)*