# modelNumber

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The device model number.

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
var modelNumber: (UInt8, UInt8)
```

```c
uint8_t modelNumber[2];
```

## Discussion

This value is 2 bytes long.

## See Also

### Configuring Device Identification
- [var manufacturer: (UInt8, UInt8, UInt8)](./manufacturer.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var family: (UInt8, UInt8)](./family.md)
  The group of familes to which the device belongs.
- [var revisionLevel: (UInt8, UInt8, UInt8, UInt8)](./revisionlevel.md)
  The revision number of the device model number.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  A reserved field whose value is always zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceidentification/modelnumber)*