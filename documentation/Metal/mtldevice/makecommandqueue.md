# makeCommandQueue()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a queue you use to submit rendering and computation commands to a GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeCommandQueue() -> (any MTLCommandQueue)?
```

## Mentions

- [Setting Up a Command Structure](setting-up-a-command-structure.md)

#### Return Value

A new [`MTLCommandQueue`](mtlcommandqueue.md) instance if the method completed successfully; otherwise `nil`.

#### Discussion

A command queue can only submit commands to the GPU device instance that created it.

> ❗ **Important**:  The command queues you create with this method allow up to 64 uncompleted command buffers at time.

 The command queues you create with this method allow up to 64 uncompleted command buffers at time.

This method is the equivalent of passing `64` to the [`makeCommandQueue(maxCommandBufferCount:)`](mtldevice/makecommandqueue(maxcommandbuffercount:).md) method.

## See Also

- [func makeCommandQueue(maxCommandBufferCount: Int) -> (any MTLCommandQueue)?](mtldevice/makecommandqueue(maxcommandbuffercount:).md)
  Creates a queue you use to submit rendering and computation commands to a GPU that has a fixed number of uncompleted command buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecommandqueue())*