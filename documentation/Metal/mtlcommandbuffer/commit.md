# commit()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Submits the command buffer to run on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func commit()
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Discussion

The [`commit()`](mtlcommandbuffer/commit().md) method sends the command buffer to the [`MTLCommandQueue`](mtlcommandqueue.md) instance that owns it, which then schedules it to run on the GPU. If your app calls [`commit()`](mtlcommandbuffer/commit().md) for a command buffer that isn’t enqueued, the method effectively calls [`enqueue()`](mtlcommandbuffer/enqueue().md) for you.

The [`commit()`](mtlcommandbuffer/commit().md) method has several restrictions, including:

- You can commit a command buffer to its command queue only one time.
- You can only commit a command buffer when it doesn’t have an active encoder (see [`MTLCommandBuffer`](mtlcommandbuffer.md) and [`MTLCommandEncoder`](mtlcommandencoder.md)).
- You can’t encode additional commands to a command buffer after you commit it.
- You can’t call the [`addScheduledHandler(_:)`](mtlcommandbuffer/addscheduledhandler(_:).md) or [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md) methods after you commit a command buffer.

The GPU starts the command buffer after it starts any command buffers that are ahead of it in the same command queue.

## See Also

- [func enqueue()](mtlcommandbuffer/enqueue.md)
  Reserves the next available place for the command buffer in its command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/commit())*