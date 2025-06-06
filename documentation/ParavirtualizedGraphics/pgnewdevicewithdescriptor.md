# PGNewDeviceWithDescriptor(_:)

**Framework**: Paravirtualized Graphics  
**Kind**: func

Creates a new paravirtualized graphics device.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func PGNewDeviceWithDescriptor(_ descriptor: PGDeviceDescriptor) -> (any PGDevice)?
```

#### Return Value

A new paravirtualized graphics device.

## Parameters

- `descriptor`: The configuration to use for the new device.

## See Also

- [class PGDeviceDescriptor](pgdevicedescriptor.md)
  A description of the paravirtualized graphics device to create.
- [protocol PGDevice](pgdevice.md)
  A paravirtualized GPU device object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgnewdevicewithdescriptor(_:))*