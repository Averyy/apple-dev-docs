# allocatedSize()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Queries the size of the internal memory heaps of this command allocator that support encoding commands into command buffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func allocatedSize() -> UInt64
```

```objc
- (uint64_t) allocatedSize;
```

## Return Value

A size in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandallocator/allocatedsize())*