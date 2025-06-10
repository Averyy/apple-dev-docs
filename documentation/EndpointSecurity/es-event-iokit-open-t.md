# es_event_iokit_open_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the opening of an IOKit device.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_iokit_open_t
```

#### Overview

Endpoint Security generates this event when a process calls [`IOServiceOpen(_:_:_:_:)`](https://developer.apple.com/documentation/iokit/1514515-ioserviceopen) in order to open a communications channel with an IOKit driver. The event doesn’t correspond to driver/device communication and provides neither visibility nor access control into devices.

## Topics

### Inspecting Event Properties
- [var user_client_class: es_string_token_t](es_event_iokit_open_t/user_client_class.md)
  The name of the IOKit service client.
- [var user_client_type: UInt32](es_event_iokit_open_t/user_client_type.md)
  The type of the IOKit client.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_iokit_open_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_iokit_open_t/init.md)
- [init(user_client_type: UInt32, user_client_class: es_string_token_t, parent_registry_id: UInt64, parent_path: es_string_token_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_iokit_open_t/init(user_client_type:user_client_class:parent_registry_id:parent_path:reserved:).md)
### Instance Properties
- [var parent_path: es_string_token_t](es_event_iokit_open_t/parent_path.md)
- [var parent_registry_id: UInt64](es_event_iokit_open_t/parent_registry_id.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_kextload_t](es_event_kextload_t.md)
  A type for an event that indicates the loading of a kernel extension.
- [struct es_event_kextunload_t](es_event_kextunload_t.md)
  A type for an event that indicates the unloading of a Kernel Extension (KEXT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_iokit_open_t)*