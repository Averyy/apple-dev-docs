# enqueue()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Reserves the next available place for the command buffer in its command queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func enqueue()
```

#### Discussion

The [`enqueue()`](mtlcommandbuffer/enqueue().md) method adds the command buffer to the [`MTLCommandQueue`](mtlcommandqueue.md) instance that owns it, but doesn’t commit the command buffer to run on the GPU. You can call the command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method at a later time when it’s ready to run on the GPU. You can call a command buffer’s [`enqueue()`](mtlcommandbuffer/enqueue().md) method any time before you call [`commit()`](mtlcommandbuffer/commit().md), including before, after, or as you encode commands to it.

> **Note**:  The command buffer can only reserve a place in its queue a single time; all subsequent [`enqueue()`](mtlcommandbuffer/enqueue().md) calls have no effect.

 The command buffer can only reserve a place in its queue a single time; all subsequent [`enqueue()`](mtlcommandbuffer/enqueue().md) calls have no effect.

Enqueuing your command buffers first gives you the flexibility to arrange their relative order of execution before encoding commands to any of them. This approach lets you potentially encode each command buffer on a thread, in parallel, instead of encoding them one by one on a single thread. The order in which each worker thread finishes encoding and commits its command buffer doesn’t matter when you enqueue them in order before committing.

## See Also

- [func commit()](mtlcommandbuffer/commit.md)
  Submits the command buffer to run on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/enqueue())*