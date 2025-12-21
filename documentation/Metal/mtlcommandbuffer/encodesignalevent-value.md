# encodeSignalEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that updates an event’s value, which can clear the GPU to run passes from other command buffers waiting for the event.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func encodeSignalEvent(_ event: any MTLEvent, value: UInt64)
```

## Mentions

- [About synchronization events](about-synchronization-events.md)

#### Discussion

The method can unblock one or more command buffers that are waiting for `event`, including those in other command queues (see [`encodeWaitForEvent(_:value:)`](mtlcommandbuffer/encodewaitforevent(_:value:).md)).

A command buffer can signal an event only between passes, not within a pass. If a command buffer has an active encoder, finish using the encoder, call its [`endEncoding()`](mtlcommandencoder/endencoding().md) method, and then call this method before creating another encoder.

When the GPU device reaches the signal command that this method encodes, Metal updates the event after the GPU finishes the buffer’s prior commands. Updating the event’s value can signal any command buffer that’s waiting for a value equal to or less than the `value` parameter.

## Parameters

- `event`: Otherwise, the method can signal only command buffers from the same GPU device.
- `value`: A value that’s greater than or equal to the event’s current value; otherwise, the command has no effect.

## See Also

- [func encodeWaitForEvent(any MTLEvent, value: UInt64)](mtlcommandbuffer/encodewaitforevent(_:value:).md)
  Encodes a command into the command buffer that pauses the GPU from running the buffer’s subsequent passes until the event equals or exceeds a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/encodesignalevent(_:value:))*