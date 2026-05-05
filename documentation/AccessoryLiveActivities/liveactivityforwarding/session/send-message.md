# send(message:)

**Framework**: Accessory Live Activities  
**Kind**: method

Sends a message to the paired accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
final func send(message: AccessoryMessage) async throws
```

#### Overview

Use this method to send data to the paired accessory. To receive responses from the accessory, implement the [`messageReceived(_:)`](liveactivityforwarding/accessoryliveactivitieshandler/messagereceived(_:).md) method in your [`LiveActivityForwarding.AccessoryLiveActivitiesHandler`](liveactivityforwarding/accessoryliveactivitieshandler.md).

## Parameters

- `message`: The message to send to the accessory device.

## See Also

- [var liveActivities: [AccessoryLiveActivity]](liveactivityforwarding/session/liveactivities.md)
  The currently active Live Activities that the accessory is authorized to receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/session/send(message:))*