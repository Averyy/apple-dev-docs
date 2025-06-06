# signalEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that signals a shared event to other parts of your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func signalEvent(_ event: any MTLSharedEvent, value: UInt64)
```

## Parameters

- `event`: A shared event instance the method waits for.
- `value`: A value the command uses to signal for the event to other parts of your app.

## See Also

- [func waitForEvent(any MTLSharedEvent, value: UInt64)](mtliocommandbuffer/waitforevent(_:value:).md)
  Encodes a command that pauses the command buffer’s execution until another part of your app signals a shared event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/signalevent(_:value:))*