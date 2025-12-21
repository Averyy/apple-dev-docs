# makeCommandAllocator(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new command allocator from a command allocator descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeCommandAllocator(descriptor: MTL4CommandAllocatorDescriptor) throws -> any MTL4CommandAllocator
```

#### Return Value

A [`MTL4CommandAllocator`](mtl4commandallocator.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: A   instance that configures the    instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecommandallocator(descriptor:))*