# PGCreateDeviceWithDescriptor(_:)

**Framework**: Paravirtualized Graphics  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 14.0+
- macOS 15.2+

## Declaration

```swift
func PGCreateDeviceWithDescriptor(_ descriptor: PGDeviceDescriptor) -> (any PGDevice)?
```

```c
extern id<PGDevice>PGCreateDeviceWithDescriptor(PGDeviceDescriptor *descriptor);
```

## Discussion

Create a new PGDevice implementation object based on the provided descriptor.

## Parameters

- `descriptor`: The device descriptor for the new device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgcreatedevicewithdescriptor(_:))*