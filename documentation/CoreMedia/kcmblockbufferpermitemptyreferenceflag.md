# kCMBlockBufferPermitEmptyReferenceFlag

**Framework**: Core Media  
**Kind**: var

Passed to [`CMBlockBuffer`](cmblockbuffer.md) and [`CMBlockBuffer`](cmblockbuffer.md) to allow references into a `CMBlockBuffer` that may not yet be populated.

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
var kCMBlockBufferPermitEmptyReferenceFlag: CMBlockBufferFlags { get }
```

## See Also

- [var kCMBlockBufferAssureMemoryNowFlag: CMBlockBufferFlags](kcmblockbufferassurememorynowflag.md)
  When passed to routines that accept block allocators, causes the memory block to be allocated immediately.
- [var kCMBlockBufferAlwaysCopyDataFlag: CMBlockBufferFlags](kcmblockbufferalwayscopydataflag.md)
  Used with [`CMBlockBuffer`](cmblockbuffer.md) to cause it to always produce an allocated copy of the desired data.
- [var kCMBlockBufferDontOptimizeDepthFlag: CMBlockBufferFlags](kcmblockbufferdontoptimizedepthflag.md)
  Passed to block buffers to suppress reference depth optimization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmblockbufferpermitemptyreferenceflag)*