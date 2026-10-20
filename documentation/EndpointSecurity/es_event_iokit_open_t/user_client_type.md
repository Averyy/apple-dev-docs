# user_client_type

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The type of the IOKit client.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var user_client_type: UInt32
```

```c
uint32_t user_client_type;
```

#### Discussion

The value of this type and its semantics depend on the kernel extension the caller is connecting to.

## See Also

### Inspecting Event Properties
- [var user_client_class: es_string_token_t](./user_client_class.md)
  The name of the IOKit service client.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_iokit_open_t/user_client_type)*