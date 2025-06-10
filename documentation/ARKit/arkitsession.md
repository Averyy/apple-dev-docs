# ARKitSession

**Framework**: ARKit  
**Kind**: class

The main entry point for receiving data from ARKit.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
final class ARKitSession
```

#### Overview

Sessions in ARKit require either implicit or explicit authorization. To explicitly ask for permission for a particular kind of data and choose when a person is prompted for that permission, call [`requestAuthorization(for:)`](arkitsession/requestauthorization(for:).md) before [`run(_:)`](arkitsession/run(_:).md).

The following shows a session that starts by requesting implicit authorization to use world sensing:

```swift
let planeData = PlaneDetectionProvider(alignments: [.horizontal, .vertical])

Task {
    do {
        try await self.session.run([planeData])
        // Update app based on the planeData.anchorUpdates async sequence.
    } catch {
        print("ARKitSession error:", error)
    }
}
```

Because a [`PlaneDetectionProvider`](planedetectionprovider.md) instance’s required authorizations include [`ARKitSession.AuthorizationType.worldSensing`](arkitsession/authorizationtype/worldsensing.md), the system asks someone using your app to permit world sensing before ARKit supplies any of that kind of data.

> **Note**:  ARKit stops sessions when they’re deinitialized; keep a reference to a session instance for as long as the session needs to run.

## Topics

### Starting and stopping a session
- [convenience init()](arkitsession/init.md)
  Creates a new session.
- [func run([any DataProvider]) async throws](arkitsession/run(_:).md)
  Runs a session with the data providers you supply.
- [func stop()](arkitsession/stop.md)
  Stops all data providers running in this session.
- [ARKitSession.Error](arkitsession/error.md)
  An error that might occur when running data providers on an ARKit session.
### Getting authorization
- [func requestAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](arkitsession/requestauthorization(for:).md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ARKitSession.AuthorizationType](arkitsession/authorizationtype.md)
  The authorization types you can request from ARKit.
- [func queryAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](arkitsession/queryauthorization(for:).md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ARKitSession.AuthorizationStatus](arkitsession/authorizationstatus.md)
  The authorization states for a type of ARKit data.
### Observing a session
- [var events: ARKitSession.Events](arkitsession/events-swift.property.md)
  An asynchronous sequence of events that provide updates to the current authorization status of the session.
- [ARKitSession.Events](arkitsession/events-swift.struct.md)
  A sequence of events.
- [ARKitSession.Event](arkitsession/event.md)
  The kinds of events that can occur in a session.
- [var description: String](arkitsession/description.md)
  A textual representation of this session.
### Initializers
- [convenience init(device: RemoteDeviceIdentifier)](arkitsession/init(device:).md)
  Create a new session connected to the specified device.
### Instance Properties
- [var dataProviders: [any DataProvider]](arkitsession/dataproviders.md)
  A list of all data providers on this session.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [protocol DataProvider](dataprovider.md)
  A source of live data from ARKit.
- [protocol Anchor](anchor.md)
  The identity, location, and orientation of an object in world space.
- [ARKit in visionOS](arkit-in-visionos.md)
  Create immersive augmented reality experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession)*