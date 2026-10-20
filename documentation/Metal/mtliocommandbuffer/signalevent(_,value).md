# signalEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) signalEvent:(id<MTLSharedEvent>) event value:(uint64_t) value;
```

## Parameters

- `event`: A shared event instance the method waits for.
- `value`: A value the command uses to signal for the event to other parts of your app.

## See Also

### Synchronizing a command buffer
- [func waitForEvent(any MTLSharedEvent, value: UInt64)](./waitforevent%28_,value%29.md)
  Encodes a command that pauses the command buffer’s execution until another part of your app signals a shared event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/signalevent(_:value:))*