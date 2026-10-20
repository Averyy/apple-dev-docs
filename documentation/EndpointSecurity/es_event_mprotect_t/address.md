# address

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The starting memory address to protect.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var address: user_addr_t
```

```c
user_addr_t address;
```

## See Also

### Inspecting Event Properties
- [var size: user_size_t](./size.md)
  The length of the address range to protect.
- [var protection: Int32](./protection.md)
  The protection to apply to the memory-mapped range.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mprotect_t/address)*