# ARKitSession.AuthorizationType

**Framework**: ARKit  
**Kind**: enum

The authorization types you can request from ARKit.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum AuthorizationType
```

## Topics

### Requesting authorization
- [ARKitSession.AuthorizationType.handTracking](arkitsession/authorizationtype/handtracking.md)
  The authorization for access to detailed hand-tracking data.
- [ARKitSession.AuthorizationType.worldSensing](arkitsession/authorizationtype/worldsensing.md)
  The authorization for access to plane detection, scene reconstruction, and image tracking.
- [ARKitSession.AuthorizationType.cameraAccess](arkitsession/authorizationtype/cameraaccess.md)
  The authorization for camera access.
### Enumeration Cases
- [ARKitSession.AuthorizationType.accessoryTracking](arkitsession/authorizationtype/accessorytracking.md)
  Accessory Tracking
### Instance Properties
- [var description: String](arkitsession/authorizationtype/description.md)
  A textual representation of AuthorizationType

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](arkitsession/requestauthorization(for:).md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [func queryAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](arkitsession/queryauthorization(for:).md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ARKitSession.AuthorizationStatus](arkitsession/authorizationstatus.md)
  The authorization states for a type of ARKit data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/authorizationtype)*