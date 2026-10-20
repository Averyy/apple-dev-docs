# waitUntilScheduled()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Blocks the current thread until the command queue schedules the buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func waitUntilScheduled()
```

```objc
- (void) waitUntilScheduled;
```

## Mentions

- [Preparing your Metal app to run in the background](../preparing-your-metal-app-to-run-in-the-background.md)

#### Discussion

This method returns after the following events:

- The command queue *schedules* (see [`status`](./status.md) and [`MTLCommandBufferStatus.scheduled`](../mtlcommandbufferstatus/scheduled.md)) the command buffer to run on the GPU.
- The command buffer invokes all the completion handlers your app submits with [`addScheduledHandler(_:)`](./addscheduledhandler%28_%29.md).

Use the [`waitUntilCompleted()`](./waituntilcompleted%28%29.md) method to check for completion of the scheduled work.

## See Also

### Waiting for state changes
- [func waitUntilCompleted()](./waituntilcompleted%28%29.md)
  Blocks the current thread until the GPU finishes executing the command buffer and all of its completion handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilscheduled())*