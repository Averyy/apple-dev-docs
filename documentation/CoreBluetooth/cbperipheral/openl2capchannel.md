# openL2CAPChannel(_:)

**Framework**: Core Bluetooth  
**Kind**: method

Attempts to open an L2CAP channel to the peripheral using the supplied Protocol/Service Multiplexer (PSM).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func openL2CAPChannel(_ PSM: CBL2CAPPSM)
```

## Parameters

- `PSM`: The PSM of the channel to open.

## See Also

- [class CBL2CAPChannel](cbl2capchannel.md)
  A live L2CAP connection to a remote device.
- [typealias CBL2CAPPSM](cbl2cappsm.md)
  The type of PSM identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/openl2capchannel(_:))*