# LiveActivityForwarding

**Framework**: Accessory Live Activities  
**Kind**: class

A class for requesting permission to forward Live Activities to your accessory and handle them in your accessory’s data provider extension.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
final class LiveActivityForwarding
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Overview

Use this class from your accessory’s data provider extension.

## Topics

### Requesting Live Activity forwarding
- [init(() -> any LiveActivityForwarding.AccessoryLiveActivitiesHandler)](liveactivityforwarding/init(_:).md)
  Creates an object you use to manage Live Activity forwarding for your accessory.
- [static func authorization(forAccessory: ASAccessory) async throws -> AccessoryAuthorizationResult](liveactivityforwarding/authorization(foraccessory:).md)
  Checks whether someone permits the system to forward Live Activities to the given accessory.
- [static func presentAuthorizationSheet(forAccessory: ASAccessory) async throws -> AccessoryAuthorizationResult](liveactivityforwarding/presentauthorizationsheet(foraccessory:).md)
  Presents the system UI that allows people to manage their permission to forward Live Activities to an accessory.
- [static let featureID: String](liveactivityforwarding/featureid.md)
  A constant you use to configure your data provider extension’s capability to forward Live Activities to your accessory.
### Handling Live Activities
- [LiveActivityForwarding.AccessoryLiveActivitiesHandler](liveactivityforwarding/accessoryliveactivitieshandler.md)
  A protocol that defines methods for handling Live Activity life cycle events in your accessory’s data provider extension.
- [LiveActivityForwarding.Session](liveactivityforwarding/session.md)
  An object that represents the active connection between your data provider extension and the system.

## Relationships

### Conforms To
- [AccessoryFeature](../accessorytransportextension/accessoryfeature.md)
- [AppExtensionPoint.Capability](../extensionfoundation/appextensionpoint/capability.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum AccessoryAuthorizationResult](accessoryauthorizationresult.md)
  Responses to the Live Activity forwarding permission prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding)*