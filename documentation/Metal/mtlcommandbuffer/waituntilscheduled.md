# waitUntilScheduled()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Blocks the current thread until the command queue schedules the buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func waitUntilScheduled()
```

## Mentions

- [Preparing your Metal app to run in the background](preparing-your-metal-app-to-run-in-the-background.md)

#### Discussion

This method returns after the following events:

- The command queue  (see [`status`](mtlcommandbuffer/status.md) and [`MTLCommandBufferStatus.scheduled`](mtlcommandbufferstatus/scheduled.md)) the command buffer to run on the GPU.
- The command buffer invokes all the completion handlers your app submits with [`addScheduledHandler(_:)`](mtlcommandbuffer/addscheduledhandler(_:).md).

Use the [`waitUntilCompleted()`](mtlcommandbuffer/waituntilcompleted().md) method to check for completion of the scheduled work.

## See Also

- [func waitUntilCompleted()](mtlcommandbuffer/waituntilcompleted.md)
  Blocks the current thread until the GPU finishes executing the command buffer and all of its completion handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilscheduled())*