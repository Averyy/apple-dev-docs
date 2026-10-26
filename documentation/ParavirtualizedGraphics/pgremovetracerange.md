# PGRemoveTraceRange

**Framework**: Paravirtualized Graphics  
**Kind**: typealias  
**Role**: Type Alias

The block signature for a routine that removes a trace range.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```c
typedef void (^)(struct PGTraceRange_s *) PGRemoveTraceRange;
```

## Parameters

- `range`: The trace to remove.

## See Also

### Specifying Trace Behavior
- [addTraceRange](./pgdevicedescriptor/addtracerange.md)
  A handler that the framework calls to add a trace range.
- [removeTraceRange](./pgdevicedescriptor/removetracerange.md)
  A handler that the framework calls to remove a trace range.
- [PGAddTraceRange](./pgaddtracerange.md)
  The block signature for a routine that adds a trace range.
- [PGTraceRangeHandler](./pgtracerangehandler.md)
  The block signature for a routine that handles trace requests.
- [PGTraceRange_t](./pgtracerange_t.md)
  An opaque data pointer representing a specific trace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgremovetracerange)*