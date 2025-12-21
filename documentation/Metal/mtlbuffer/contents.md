# contents()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Gets the system address of the buffer’s storage allocation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func contents() -> UnsafeMutableRawPointer
```

#### Return Value

A pointer to the shared copy of the buffer data, or `NULL` for buffers allocated with a private resource storage mode ([`MTLStorageMode.private`](mtlstoragemode/private.md)).

#### Discussion

Private resources aren’t CPU-accessible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/contents())*