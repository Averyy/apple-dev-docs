# makeMTL4CommandQueue(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new command queue from a queue descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeMTL4CommandQueue(descriptor: MTL4CommandQueueDescriptor) throws -> any MTL4CommandQueue
```

#### Return Value

A [`MTL4CommandQueue`](mtl4commandqueue.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: A   instance that configures the    instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makemtl4commandqueue(descriptor:))*