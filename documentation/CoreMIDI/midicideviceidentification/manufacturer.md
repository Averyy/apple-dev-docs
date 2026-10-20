# manufacturer

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The MIDI System Exclusive (SysEx) ID of the device manufacturer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var manufacturer: (UInt8, UInt8, UInt8)
```

```c
uint8_t manufacturer[3];
```

#### Discussion

This value is 3 bytes long.

The framework pads single-byte System Exclusive (SysEx) IDs with trailing zeros. For example, Apple’s SysEx ID, 0x11, is `0x110000`.

## See Also

### Configuring Device Identification
- [var modelNumber: (UInt8, UInt8)](./modelnumber.md)
  The device model number.
- [var family: (UInt8, UInt8)](./family.md)
  The group of familes to which the device belongs.
- [var revisionLevel: (UInt8, UInt8, UInt8, UInt8)](./revisionlevel.md)
  The revision number of the device model number.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  A reserved field whose value is always zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceidentification/manufacturer)*