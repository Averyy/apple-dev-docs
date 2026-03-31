# LiveActivityForwarding.Session

**Framework**: Accessory Live Activities  
**Kind**: class

An object that represents the active connection between your data provider extension and the system.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
final class Session
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Overview

Each `Session` has one corresponding [`LiveActivityForwarding.AccessoryLiveActivitiesHandler`](liveactivityforwarding/accessoryliveactivitieshandler.md).

## Topics

### Working with Live Activities
- [var liveActivities: [AccessoryLiveActivity]](liveactivityforwarding/session/liveactivities.md)
  The currently active Live Activities that the accessory is authorized to receive.
- [func send(message: AccessoryMessage) async throws](liveactivityforwarding/session/send(message:).md)
  Sends a message to the paired accessory.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LiveActivityForwarding.AccessoryLiveActivitiesHandler](liveactivityforwarding/accessoryliveactivitieshandler.md)
  A protocol that defines methods for handling Live Activity life cycle events in your accessory’s data provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/session)*