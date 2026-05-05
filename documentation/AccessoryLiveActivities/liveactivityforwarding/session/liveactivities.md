# liveActivities

**Framework**: Accessory Live Activities  
**Kind**: property

The currently active Live Activities that the accessory is authorized to receive.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
final var liveActivities: [AccessoryLiveActivity] { get async throws }
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

## See Also

- [func send(message: AccessoryMessage) async throws](liveactivityforwarding/session/send(message:).md)
  Sends a message to the paired accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/session/liveactivities)*