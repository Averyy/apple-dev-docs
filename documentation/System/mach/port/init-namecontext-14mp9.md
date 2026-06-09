# init(name:context:)

**Framework**: System  
**Kind**: init

Transfer ownership of an existing, unmanaged, but already guarded, Mach port right into a Mach.Port by name.

**Availability**:
- macOS 14.4+

## Declaration

```swift
init(name: mach_port_name_t, context: mach_port_context_t)
```

#### Discussion

This initializer aborts if name is MACH_PORT_NULL.

If the type of the right does not match the type T of Mach.Port being constructed, the behavior is undefined.

The underlying port right will be automatically deallocated when the Mach.Port object is destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach/port/init(name:context:)-14mp9)*