# makeMTL4CommandQueue(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new command queue from a queue descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeMTL4CommandQueue(descriptor: MTL4CommandQueueDescriptor) throws -> any MTL4CommandQueue
```

#### Return Value

A [`MTL4CommandQueue`](mtl4commandqueue.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: A [`MTL4CommandQueueDescriptor`](mtl4commandqueuedescriptor.md) instance that configures the [`MTL4CommandQueue`](mtl4commandqueue.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makemtl4commandqueue(descriptor:))*