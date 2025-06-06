# MTLIOCommandBuffer

**Framework**: Metal  
**Kind**: protocol

A command buffer that contains input/output commands that work with files in the file systems and Metal resources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIOCommandBuffer : NSObjectProtocol
```

#### Overview

Add commands an input/output command buffer to load assets from the file system directly into Metal resources. Your app can then use those resources with other commands it submits to [`MTLCommandQueue`](mtlcommandqueue.md).

## Topics

### Loading Assets
- [func load(any MTLBuffer, offset: Int, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](mtliocommandbuffer/load(_:offset:size:sourcehandle:sourcehandleoffset:).md)
  Encodes a command that loads data from a file handle into a GPU buffer.
- [func load(any MTLTexture, slice: Int, level: Int, size: MTLSize, sourceBytesPerRow: Int, sourceBytesPerImage: Int, destinationOrigin: MTLOrigin, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](mtliocommandbuffer/load(_:slice:level:size:sourcebytesperrow:sourcebytesperimage:destinationorigin:sourcehandle:sourcehandleoffset:).md)
  Encodes a command that loads data from a file handle into a GPU texture.
- [func loadBytes(UnsafeMutableRawPointer, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](mtliocommandbuffer/loadbytes(_:size:sourcehandle:sourcehandleoffset:).md)
  Encodes a command that loads data from a file handle into CPU-accessible memory buffer.
### Adding a Barrier
- [func addBarrier()](mtliocommandbuffer/addbarrier.md)
  Encodes a barrier into the command buffer.
### Synchronizing a Command Buffer
- [func signalEvent(any MTLSharedEvent, value: UInt64)](mtliocommandbuffer/signalevent(_:value:).md)
  Encodes a command that signals a shared event to other parts of your app.
- [func waitForEvent(any MTLSharedEvent, value: UInt64)](mtliocommandbuffer/waitforevent(_:value:).md)
  Encodes a command that pauses the command buffer’s execution until another part of your app signals a shared event.
### Adding Final Commands
- [func copyStatus(buffer: any MTLBuffer, offset: Int)](mtliocommandbuffer/copystatus(buffer:offset:).md)
  Encodes a command that writes the input/output command buffer’s status to a buffer.
- [func addCompletedHandler(MTLIOCommandBufferHandler)](mtliocommandbuffer/addcompletedhandler(_:).md)
  Adds a closure that Metal calls immediately after the GPU finishes executing the commands in the input/output command buffer.
### Submitting a Command Buffer
- [func commit()](mtliocommandbuffer/commit.md)
  Submits the command buffer to the queue for execution on the GPU.
- [func enqueue()](mtliocommandbuffer/enqueue.md)
  Reserves a place for the input/output command buffer in the input/output command queue without committing the command buffer.
### Canceling a Command Buffer
- [func tryCancel()](mtliocommandbuffer/trycancel.md)
  Submits a request to abandon a command buffer the queue is currently running.
### Waiting for a Command Buffer
- [func waitUntilCompleted()](mtliocommandbuffer/waituntilcompleted.md)
  Blocks the current thread until the GPU finishes executing the input/output command buffer and all of its completion handlers.
### Checking the State of a Command Buffer
- [var status: MTLIOStatus](mtliocommandbuffer/status.md)
  Represents the state of the input/output command buffer.
- [var error: (any Error)?](mtliocommandbuffer/error.md)
  Stores the details of an error when the GPU experienced a problem with the input/output command buffer.
### Debugging a Command Buffer
- [var label: String?](mtliocommandbuffer/label.md)
  An optional name for the input/output command buffer.
- [func pushDebugGroup(String)](mtliocommandbuffer/pushdebuggroup(_:).md)
  Sets the current name for this input/output command encoder by adding it to the top of the debug name stack.
- [func popDebugGroup()](mtliocommandbuffer/popdebuggroup.md)
  Restores the previous name for this input/output command encoder by removing the top item of the debug name stack.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLIOFileHandle](mtliofilehandle.md)
  Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [typealias MTLIOCommandBufferHandler](mtliocommandbufferhandler.md)
  A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [enum MTLIOStatus](mtliostatus.md)
  Represents the state of an input/output command buffer.
- [MTLIOError.Code](mtlioerror-swift.struct/code.md)
  The error codes for creating an input/output file handle.
- [let MTLIOErrorDomain: String](mtlioerrordomain.md)
  The domain for input/output command queue errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer)*