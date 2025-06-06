# PGRemoveTraceRange

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that removes a trace range.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGRemoveTraceRange = (OpaquePointer) -> Void
```

## Parameters

- `range`: The trace to remove.

## See Also

- [var addTraceRange: PGAddTraceRange?](pgdevicedescriptor/addtracerange.md)
  A handler that the framework calls to add a trace range.
- [var removeTraceRange: PGRemoveTraceRange?](pgdevicedescriptor/removetracerange.md)
  A handler that the framework calls to remove a trace range.
- [typealias PGAddTraceRange](pgaddtracerange.md)
  The block signature for a routine that adds a trace range.
- [typealias PGTraceRangeHandler](pgtracerangehandler.md)
  The block signature for a routine that handles trace requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgremovetracerange)*