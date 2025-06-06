# encodeWaitForEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command into the command buffer that pauses the GPU from running the buffer’s subsequent passes until the event equals or exceeds a value.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func encodeWaitForEvent(_ event: any MTLEvent, value: UInt64)
```

## Mentions

- [About Synchronization Events](about-synchronization-events.md)

#### Discussion

This method prevents the GPU from starting the next pass in the command buffer until another command buffer signals `event` (see [`encodeSignalEvent(_:value:)`](mtlcommandbuffer/encodesignalevent(_:value:).md).

A command buffer can instruct the GPU to wait for an event only between passes, not within a pass. If a command buffer has an active encoder, finish using the encoder, call its [`endEncoding()`](mtlcommandencoder/endencoding().md) method, and then call this method before creating another encoder.

When the GPU device reaches the wait command that this method encodes into the buffer, it checks the event’s current value. If the event’s value — which increases monotonically — is less than the `value` parameter, the GPU waits before running the next pass in the buffer. The GPU starts the next pass when the event signals a value that’s equal to or greater than the `value` parameter (see [`encodeSignalEvent(_:value:)`](mtlcommandbuffer/encodesignalevent(_:value:).md)). However, If the event’s value is already greater than or equal to the `value` parameter, the GPU immediately starts the next pass without waiting.

## Parameters

- `event`: If   is an   instance, a command buffer from any GPU device can signal this command buffer. Otherwise, only command buffers from the same GPU device can signal this command buffer.
- `value`: The event’s smallest value that allows the GPU to continue running the remaining passes in the command buffer.

## See Also

- [func encodeSignalEvent(any MTLEvent, value: UInt64)](mtlcommandbuffer/encodesignalevent(_:value:).md)
  Encodes a command that updates an event’s value, which can clear the GPU to run passes from other command buffers waiting for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/encodewaitforevent(_:value:))*