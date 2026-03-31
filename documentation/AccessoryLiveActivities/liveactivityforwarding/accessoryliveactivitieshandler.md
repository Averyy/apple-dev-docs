# LiveActivityForwarding.AccessoryLiveActivitiesHandler

**Framework**: Accessory Live Activities  
**Kind**: protocol

A protocol that defines methods for handling Live Activity life cycle events in your accessory’s data provider extension.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
protocol AccessoryLiveActivitiesHandler : Sendable
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Overview

Implement this protocol to receive forwarded Live Activity content and life cycle updates in your [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension.

Each `AccessoryLiveActivitiesHandler` object has one corresponding [`LiveActivityForwarding.Session`](liveactivityforwarding/session.md).

## Topics

### Managing the session life cycle
- [func activate(for: LiveActivityForwarding.Session)](liveactivityforwarding/accessoryliveactivitieshandler/activate(for:).md)
  Establishes communication between the data provider extension and the system.
- [func sessionInvalidated()](liveactivityforwarding/accessoryliveactivitieshandler/sessioninvalidated.md)
  Indicates that the system invalidated the session and stopped sending Live Activity updates.
### Receiving Live Activity updates
- [func activityUpdated(AccessoryLiveActivity)](liveactivityforwarding/accessoryliveactivitieshandler/activityupdated(_:).md)
  Provides an updated Live Activity.
- [func activityUpdatedForAlert(AccessoryLiveActivity) -> Bool](liveactivityforwarding/accessoryliveactivitieshandler/activityupdatedforalert(_:).md)
  Provides an updated Live Activity and requests confirmation that the accessory displayed an alert.
### Receiving data from your accessory
- [func messageReceived(TransportMessage)](liveactivityforwarding/accessoryliveactivitieshandler/messagereceived(_:).md)
  Delivers a message from the paired accessory to your data provider extension.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LiveActivityForwarding.Session](liveactivityforwarding/session.md)
  An object that represents the active connection between your data provider extension and the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/accessoryliveactivitieshandler)*