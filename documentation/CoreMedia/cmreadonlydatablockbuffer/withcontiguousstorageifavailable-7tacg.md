# withContiguousStorageIfAvailable(_:)

**Framework**: Core Media  
**Kind**: method

Access contents of the buffer if available as contiguous memory block.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func withContiguousStorageIfAvailable<R>(_ body: (UnsafeRawBufferPointer) throws -> sending R) rethrows -> sending R?
```

#### Discussion

This method calls body(buffer), where buffer is a pointer to the block buffers contiguous storage. If the contiguous storage doesn’t exist,  the method doesn’t call body — it immediately returns nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/withcontiguousstorageifavailable(_:)-7tacg)*