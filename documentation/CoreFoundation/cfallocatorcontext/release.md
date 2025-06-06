# release

**Framework**: Core Foundation  
**Kind**: property

A prototype for a function callback that releases the data pointed to by the `info` field. In implementing this function, release (or free) the data you have defined for the allocator context. You may set this function pointer to `NULL`, but doing so might result in memory leaks.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var release: CFAllocatorReleaseCallBack!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/release)*