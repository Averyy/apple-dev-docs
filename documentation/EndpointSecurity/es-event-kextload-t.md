# es_event_kextload_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the loading of a kernel extension.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_kextload_t
```

## Topics

### Inspecting Event Properties
- [var identifier: es_string_token_t](es_event_kextload_t/identifier.md)
  A string identifying the kernel extension.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_kextload_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_kextload_t/init.md)
- [init(identifier: es_string_token_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_kextload_t/init(identifier:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_iokit_open_t](es_event_iokit_open_t.md)
  A type for an event that indicates the opening of an IOKit device.
- [struct es_event_kextunload_t](es_event_kextunload_t.md)
  A type for an event that indicates the unloading of a Kernel Extension (KEXT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_kextload_t)*