# PGAddTraceRange

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that adds a trace range.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGAddTraceRange = (UnsafeMutablePointer<PGPhysicalMemoryRange_t>, @escaping PGTraceRangeHandler) -> OpaquePointer?
```

#### Return Value

A [`PGTraceRange_t`](pgtracerange_t.md) pointer, or `NULL` if an error occurred.

#### Discussion

The framework uses traces to provide a low-overhead framebuffer implementation that the virtual graphics device uses before the guest OS loads the driver.

The block also records any data it needs to keep track of this trace and returns a pointer to that data. The framework doesn’t read from this pointer.

Until the framework destroys the trace, the app must detect whenever the guest alters the contents of memory within the trace range. When the app detects memory changes, call the handler to notify the framework. Where possible, coalesce the handling of these notifications over a period of several milliseconds to reduce the number of calls to the handler.

## Parameters

- `range`: The range of guest physical memory to monitor.
- `handler`: The block for the app to call when it detects any writes to the memory range.

## See Also

- [var addTraceRange: PGAddTraceRange?](pgdevicedescriptor/addtracerange.md)
  A handler that the framework calls to add a trace range.
- [var removeTraceRange: PGRemoveTraceRange?](pgdevicedescriptor/removetracerange.md)
  A handler that the framework calls to remove a trace range.
- [typealias PGRemoveTraceRange](pgremovetracerange.md)
  The block signature for a routine that removes a trace range.
- [typealias PGTraceRangeHandler](pgtracerangehandler.md)
  The block signature for a routine that handles trace requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgaddtracerange)*