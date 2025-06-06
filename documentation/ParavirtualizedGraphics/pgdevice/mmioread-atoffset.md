# mmioRead(atOffset:)

**Framework**: Paravirtualized Graphics  
**Kind**: method  
**Required**: Yes

Reads data from the virtual graphics device’s memory-mapped I/O region.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func mmioRead(atOffset offset: Int) -> UInt32
```

#### Return Value

The 32-bit unsigned integer from the MMIO region.

#### Discussion

Call this method whenever the guest virtual machine reads from the graphics device’s memory-mapped I/O region.

## Parameters

- `offset`: The offset into the MMIO bar to write to.

## See Also

- [func mmioWrite(atOffset: Int, value: UInt32)](pgdevice/mmiowrite(atoffset:value:).md)
  Writes data to the virtual graphics device’s memory-mapped I/O region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice/mmioread(atoffset:))*