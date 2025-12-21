# makeCommandAllocator()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new command allocator.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeCommandAllocator() -> (any MTL4CommandAllocator)?
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Return Value

A [`MTL4CommandAllocator`](mtl4commandallocator.md) instance, or `nil` if the function failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecommandallocator())*