# family

**Framework**: Core MIDI  
**Kind**: property

The group of familes to which the device belongs.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var family: (UInt8, UInt8)
```

#### Discussion

This value is 2 bytes long.

## See Also

- [var manufacturer: (UInt8, UInt8, UInt8)](midicideviceidentification/manufacturer.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var modelNumber: (UInt8, UInt8)](midicideviceidentification/modelnumber.md)
  The device model number.
- [var revisionLevel: (UInt8, UInt8, UInt8, UInt8)](midicideviceidentification/revisionlevel.md)
  The revision number of the device model number.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8)](midicideviceidentification/reserved.md)
  A reserved field whose value is always zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceidentification/family)*