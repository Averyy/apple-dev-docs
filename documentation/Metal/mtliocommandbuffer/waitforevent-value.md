# waitForEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that pauses the command buffer’s execution until another part of your app signals a shared event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func waitForEvent(_ event: any MTLSharedEvent, value: UInt64)
```

## Parameters

- `event`: A shared event instance the method waits for.
- `value`: A value the method compares to the event’s value. The method returns when the event’s value is greater than or equal to  .

## See Also

- [func signalEvent(any MTLSharedEvent, value: UInt64)](mtliocommandbuffer/signalevent(_:value:).md)
  Encodes a command that signals a shared event to other parts of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/waitforevent(_:value:))*