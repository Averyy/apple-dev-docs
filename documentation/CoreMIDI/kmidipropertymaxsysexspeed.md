# kMIDIPropertyMaxSysExSpeed

**Framework**: Core MIDI  
**Kind**: var

The maximum rate, in bytes per second, at which the system may reliably send System Exclusive (SysEx) messages to this object.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyMaxSysExSpeed: CFString
```

#### Discussion

The owning driver may set an integer value for this property.

## See Also

- [let kMIDIPropertyNameConfigurationDictionary: CFString](kmidipropertynameconfigurationdictionary.md)
  The device’s current patch, note, and control name values in MIDINameDocument XML format.
- [let kMIDIPropertyDriverDeviceEditorApp: CFString](kmidipropertydriverdeviceeditorapp.md)
  The full path to an app on the system that configures driver-owned devices.
- [let kMIDIPropertyNameConfiguration: CFString](kmidipropertynameconfiguration.md)
  An XML representation of the device’s current patch, note, and control name values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertymaxsysexspeed)*