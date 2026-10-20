# mmioWrite(atOffset:value:)

**Framework**: Paravirtualized Graphics  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Writes data to the virtual graphics device’s memory-mapped I/O region.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func mmioWrite(atOffset offset: Int, value: UInt32)
```

```objc
- (void) mmioWriteAtOffset:(size_t) offset value:(uint32_t) value;
```

#### Discussion

Call this method whenever the guest virtual machine writes to the graphics device’s memory-mapped I/O region.

## Parameters

- `offset`: The offset into the MMIO bar to write to.
- `value`: The value to write to memory.

## See Also

### Handling Memory-Mapped I/O
- [func mmioRead(atOffset: Int) -> UInt32](./mmioread%28atoffset%29.md)
  Reads data from the virtual graphics device’s memory-mapped I/O region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice/mmiowrite(atoffset:value:))*