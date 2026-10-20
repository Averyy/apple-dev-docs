# reserved

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

A reserved field whose value is always zero.

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
var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8)
```

```c
uint8_t reserved[5];
```

## See Also

### Configuring Device Identification
- [var manufacturer: (UInt8, UInt8, UInt8)](./manufacturer.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var modelNumber: (UInt8, UInt8)](./modelnumber.md)
  The device model number.
- [var family: (UInt8, UInt8)](./family.md)
  The group of familes to which the device belongs.
- [var revisionLevel: (UInt8, UInt8, UInt8, UInt8)](./revisionlevel.md)
  The revision number of the device model number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceidentification/reserved)*