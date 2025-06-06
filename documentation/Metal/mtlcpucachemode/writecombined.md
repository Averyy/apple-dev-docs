# MTLCPUCacheMode.writeCombined

**Framework**: Metal  
**Kind**: case

A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case writeCombined
```

#### Discussion

Write-combined memory is optimized for resources that the CPU writes into, but never reads. On some implementations, writes may bypass caches to avoid cache pollution. Read actions may perform very poorly.

Applications should use write combining only if writing to normally cached buffers is known to cause performance issues due to cache pollution, as write-combined memory can have surprising performance pitfalls.  Another approach is to use non-temporal writes to normally cached memory (STNP on ARMv8, _mm_stream_* on x86_64).

## See Also

- [MTLCPUCacheMode.defaultCache](mtlcpucachemode/defaultcache.md)
  The default CPU cache mode for the resource, which guarantees that read and write operations are executed in the expected order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcpucachemode/writecombined)*