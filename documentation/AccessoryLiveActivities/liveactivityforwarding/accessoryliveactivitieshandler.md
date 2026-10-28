# LiveActivityForwarding.AccessoryLiveActivitiesHandler

**Framework**: Accessory Live Activities  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines methods for handling Live Activity life cycle events in your accessory’s data provider extension.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
protocol AccessoryLiveActivitiesHandler : Sendable
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](../receiving-live-activities-on-an-accessory.md)

## Overview

Implement this protocol to receive forwarded Live Activity content and life cycle updates in your [`AccessoryDataProvider`](../../AccessoryTransportExtension/accessorydataprovider.md) extension.

Each `AccessoryLiveActivitiesHandler` object has one corresponding [`LiveActivityForwarding.Session`](./session.md).

## Topics

### Managing the session life cycle
- [func activate(for: LiveActivityForwarding.Session)](./accessoryliveactivitieshandler/activate%28for%29.md)
  Establishes communication between the data provider extension and the system.
- [func sessionInvalidated()](./accessoryliveactivitieshandler/sessioninvalidated%28%29.md)
  Indicates that the system invalidated the session and stopped sending Live Activity updates.
### Receiving Live Activity updates
- [func activityUpdated(AccessoryLiveActivity)](./accessoryliveactivitieshandler/activityupdated%28_%29.md)
  Provides an updated Live Activity.
- [func activityUpdatedForAlert(AccessoryLiveActivity) -> Bool](./accessoryliveactivitieshandler/activityupdatedforalert%28_%29.md)
  Provides an updated Live Activity and requests confirmation that the accessory displayed an alert.
### Receiving data from your accessory
- [func messageReceived(TransportMessage)](./accessoryliveactivitieshandler/messagereceived%28_%29.md)
  Delivers a message from the paired accessory to your data provider extension.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Live Activity forwarding
- [LiveActivityForwarding.Session](./session.md)
  An object that represents the active connection between your data provider extension and the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/accessoryliveactivitieshandler)*