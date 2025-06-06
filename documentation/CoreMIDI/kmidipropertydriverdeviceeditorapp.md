# kMIDIPropertyDriverDeviceEditorApp

**Framework**: Core MIDI  
**Kind**: var

The full path to an app on the system that configures driver-owned devices.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.3+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyDriverDeviceEditorApp: CFString
```

#### Discussion

Only drivers may set this property on their owned devices.

## See Also

- [let kMIDIPropertyNameConfigurationDictionary: CFString](kmidipropertynameconfigurationdictionary.md)
  The device’s current patch, note, and control name values in MIDINameDocument XML format.
- [let kMIDIPropertyMaxSysExSpeed: CFString](kmidipropertymaxsysexspeed.md)
  The maximum rate, in bytes per second, at which the system may reliably send System Exclusive (SysEx) messages to this object.
- [let kMIDIPropertyNameConfiguration: CFString](kmidipropertynameconfiguration.md)
  An XML representation of the device’s current patch, note, and control name values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertydriverdeviceeditorapp)*