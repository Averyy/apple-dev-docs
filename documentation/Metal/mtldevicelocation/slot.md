# MTLDeviceLocation.slot

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A GPU location that indicates a person connected the GPU to a system’s internal slot.

**Availability**:
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Not applicable on Apple Silicon

## Declaration

```swift
case slot
```

```c
MTLDeviceLocationSlot
```

## See Also

### Determining the GPU’s location
- [MTLDeviceLocation.builtIn](./builtin.md)
  A location that indicates the GPU is permanently connected to the system internally.
- [MTLDeviceLocation.external](./external.md)
  A GPU location that indicates a person connected the GPU to the system with an external interface, such as Thunderbolt.
- [MTLDeviceLocation.unspecified](./unspecified.md)
  A value that indicates the system can’t determine how the GPU connects to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicelocation/slot)*