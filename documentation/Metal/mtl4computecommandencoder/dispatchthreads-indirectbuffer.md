# dispatchThreads(indirectBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func dispatchThreads(indirectBuffer: UInt64)
```

## Parameters

- `indirectBuffer`: GPUAddress of a   instance providing arguments. Lay out the data   in this buffer as described in the    structure. This address requires 4-byte alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreads(indirectbuffer:))*