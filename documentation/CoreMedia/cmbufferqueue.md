# CMBufferQueue

**Framework**: Core Media  
**Kind**: class

A reference to a buffer queue instance.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CMBufferQueue
```

#### Overview

A `CMBufferQueue` is a queue of timed buffers backed by a Core Foundation object.

## Topics

### Managing a Queue
- [func enqueue(CMBuffer) throws](cmbufferqueue/enqueue(_:).md)
  Enqueues a buffer to the queue.
- [func dequeue() -> CMBuffer?](cmbufferqueue/dequeue.md)
  Dequeues a buffer from the queue.
- [func dequeueIfDataReady() -> CMBuffer?](cmbufferqueue/dequeueifdataready.md)
  Dequeues a buffer from the queue, if it’s ready.
- [func markEndOfData() throws](cmbufferqueue/markendofdata.md)
  Marks a buffer as being at the end of its data.
- [func reset() throws](cmbufferqueue/reset.md)
  Empties the queue and resets its end-of-data state.
- [func reset((CMBuffer) throws -> ()) throws](cmbufferqueue/reset(_:).md)
  Resets a buffer with a callback block.
### Managing Triggers
- [func installTrigger(condition: CMBufferQueue.TriggerCondition, CMBufferQueueTriggerHandler?) throws -> CMBufferQueue.TriggerToken](cmbufferqueue/installtrigger(condition:_:).md)
  Installs a trigger on the queue.
- [func removeTrigger(CMBufferQueue.TriggerToken) throws](cmbufferqueue/removetrigger(_:).md)
  Removes a trigger from the queue.
- [func testTrigger(CMBufferQueue.TriggerToken) -> Bool](cmbufferqueue/testtrigger(_:).md)
  Tests a trigger condition.
- [CMBufferQueue.TriggerToken](cmbufferqueue/triggertoken.md)
  A type alias for a trigger token.
- [CMBufferQueue.TriggerCondition](cmbufferqueue/triggercondition.md)
  An enumeration of trigger conditions.
### Inspecting Duration and Timing
- [var duration: CMTime](cmbufferqueue/duration.md)
  The sum of all durations of buffers in the queue.
- [var totalSize: Int](cmbufferqueue/totalsize.md)
  The total size of all buffers in the queue.
- [var firstDecodeTimeStamp: CMTime](cmbufferqueue/firstdecodetimestamp.md)
  The decode timestamp of the first buffer in the queue.
- [var firstPresentationTimeStamp: CMTime](cmbufferqueue/firstpresentationtimestamp.md)
  The presentation timestamp of the first buffer in the queue.
- [var endPresentationTimeStamp: CMTime](cmbufferqueue/endpresentationtimestamp.md)
  The greatest end presentation timestamp.
- [var minDecodeTimeStamp: CMTime](cmbufferqueue/mindecodetimestamp.md)
  The earliest decode timestamp.
- [var minPresentationTimeStamp: CMTime](cmbufferqueue/minpresentationtimestamp.md)
  The earliest presentation timestamp.
- [var maxPresentationTimeStamp: CMTime](cmbufferqueue/maxpresentationtimestamp.md)
  The greatest presentation timestamp.
### Inspecting a Queue
- [var isEmpty: Bool](cmbufferqueue/isempty.md)
  A Boolean value that indicates whether the queue contains buffers.
- [var bufferCount: CMItemCount](cmbufferqueue/buffercount.md)
  The count of buffers in the queue.
- [var head: CMBuffer?](cmbufferqueue/head.md)
  The element at the head of the queue.
- [var containsEndOfData: Bool](cmbufferqueue/containsendofdata.md)
  A Boolean value that indicates whether the buffer has its end-of-data state set.
- [var isAtEndOfData: Bool](cmbufferqueue/isatendofdata.md)
  A Boolean value that indicates whether that queue is at the end of its data.
### Validating a Queue
- [func setValidationHandler((CMBufferQueue, CMBuffer) throws -> Void)](cmbufferqueue/setvalidationhandler(_:).md)
  Sets validation handler for the queue to call before enqueuing buffers.
### Accessing Buffers
- [var buffers: CMBufferQueue.Buffers](cmbufferqueue/buffers-swift.property.md)
  The buffers that the queue contains.
### Accessing the Type Identifier
- [class var typeID: CFTypeID](cmbufferqueue/typeid.md)
  The type identifier for this object.
### Data Types
- [CMBufferQueue.Buffers](cmbufferqueue/buffers-swift.struct.md)
- [CMBufferQueue.Handlers](cmbufferqueue/handlers.md)
- [CMBufferQueue.Error](cmbufferqueue/error.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue)*