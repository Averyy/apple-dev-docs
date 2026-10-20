# MTLDeviceLocation.unspecified

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A value that indicates the system can’t determine how the GPU connects to it.

**Availability**:
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Not applicable on Apple Silicon

## Declaration

```swift
case unspecified
```

```c
MTLDeviceLocationUnspecified
```

## See Also

### Determining the GPU’s location
- [MTLDeviceLocation.builtIn](./builtin.md)
  A location that indicates the GPU is permanently connected to the system internally.
- [MTLDeviceLocation.slot](./slot.md)
  A GPU location that indicates a person connected the GPU to a system’s internal slot.
- [MTLDeviceLocation.external](./external.md)
  A GPU location that indicates a person connected the GPU to the system with an external interface, such as Thunderbolt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicelocation/unspecified)*