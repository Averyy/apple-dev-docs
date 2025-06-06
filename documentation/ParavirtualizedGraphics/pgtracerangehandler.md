# PGTraceRangeHandler

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that handles trace requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGTraceRangeHandler = (UnsafeMutablePointer<PGPhysicalMemoryRange_t>) -> Void
```

#### Discussion

The returned range may be larger than the range that the guest wrote into. For example, if you can only determine which memory the guest accessed at virtual memory page boundaries, you’d report that the entire page changed. Where possible, coalesce writes over a period of time into a single activity notification.

## Parameters

- `dirty  `: The range of memory that the guest changed.

## See Also

- [var addTraceRange: PGAddTraceRange?](pgdevicedescriptor/addtracerange.md)
  A handler that the framework calls to add a trace range.
- [var removeTraceRange: PGRemoveTraceRange?](pgdevicedescriptor/removetracerange.md)
  A handler that the framework calls to remove a trace range.
- [typealias PGAddTraceRange](pgaddtracerange.md)
  The block signature for a routine that adds a trace range.
- [typealias PGRemoveTraceRange](pgremovetracerange.md)
  The block signature for a routine that removes a trace range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgtracerangehandler)*