# makeCommandAllocator()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new command allocator.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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