# ARKitSession.AuthorizationType

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

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
- [ARKitSession.AuthorizationType.handTracking](./authorizationtype/handtracking.md)
  The authorization for access to detailed hand-tracking data.
- [ARKitSession.AuthorizationType.worldSensing](./authorizationtype/worldsensing.md)
  The authorization for access to plane detection, scene reconstruction, and image tracking.
- [ARKitSession.AuthorizationType.cameraAccess](./authorizationtype/cameraaccess.md)
  The authorization for camera access.
### Enumeration Cases
- [ARKitSession.AuthorizationType.accessoryTracking](./authorizationtype/accessorytracking.md)
  The authorization for access to accessory tracking data.
### Instance Properties
- [var description: String](./authorizationtype/description.md)
  A textual representation of AuthorizationType

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting authorization
- [func requestAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](./requestauthorization%28for%29.md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [func queryAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](./queryauthorization%28for%29.md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ARKitSession.AuthorizationStatus](./authorizationstatus.md)
  The authorization states for a type of ARKit data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/authorizationtype)*