# addTraceRange

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property

A handler that the framework calls to add a trace range.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite, nullable) PGAddTraceRange addTraceRange;
```

## See Also

### Specifying Trace Behavior
- [removeTraceRange](./removetracerange.md)
  A handler that the framework calls to remove a trace range.
- [PGAddTraceRange](../pgaddtracerange.md)
  The block signature for a routine that adds a trace range.
- [PGRemoveTraceRange](../pgremovetracerange.md)
  The block signature for a routine that removes a trace range.
- [PGTraceRangeHandler](../pgtracerangehandler.md)
  The block signature for a routine that handles trace requests.
- [PGTraceRange_t](../pgtracerange_t.md)
  An opaque data pointer representing a specific trace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor/addtracerange)*