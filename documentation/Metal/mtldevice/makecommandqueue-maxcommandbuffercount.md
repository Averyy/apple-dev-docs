# makeCommandQueue(maxCommandBufferCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a queue you use to submit rendering and computation commands to a GPU that has a fixed number of uncompleted command buffers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeCommandQueue(maxCommandBufferCount: Int) -> (any MTLCommandQueue)?
```

#### Return Value

A new [`MTLCommandQueue`](mtlcommandqueue.md) instance if the method completed successfully; otherwise `nil`.

#### Discussion

A Command queue can only submit commands to the GPU device instance that created it.

## Parameters

- `maxCommandBufferCount`: An integer that sets the maximum number of uncompleted command buffers the queue can allow.

## See Also

- [func makeCommandQueue() -> (any MTLCommandQueue)?](mtldevice/makecommandqueue.md)
  Creates a queue you use to submit rendering and computation commands to a GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecommandqueue(maxcommandbuffercount:))*