# PGRaiseInterrupt

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that raises interrupts in the guest environment.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGRaiseInterrupt = (UInt32) -> Void
```

## Parameters

- `vector  `: The MSI vector to raise the interrupt on.

## See Also

- [var raiseInterrupt: PGRaiseInterrupt?](pgdevicedescriptor/raiseinterrupt.md)
  A handler that the system calls to raise an interrupt in the guest environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgraiseinterrupt)*