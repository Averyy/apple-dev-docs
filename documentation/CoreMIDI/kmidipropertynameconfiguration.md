# kMIDIPropertyNameConfiguration

**Framework**: Core MIDI  
**Kind**: var  
**Role**: Global Variable

An XML representation of the device’s current patch, note, and control name values.

**Availability**:
- iOS 4.2+ - Deprecated in 13.0 (renamed: kMIDIPropertyNameConfigurationDictionary)
- iPadOS 4.2+ - Deprecated in 13.0 (renamed: kMIDIPropertyNameConfigurationDictionary)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: kMIDIPropertyNameConfigurationDictionary)
- macOS 10.2+ - Deprecated in 10.15 (renamed: kMIDIPropertyNameConfigurationDictionary)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: kMIDIPropertyNameConfigurationDictionary)

> **Deprecated**: Use [`kMIDIPropertyNameConfigurationDictionary`](./kmidipropertynameconfigurationdictionary.md) instead.

## Declaration

```swift
let kMIDIPropertyNameConfiguration: CFString
```

```c
extern CFStringRef const kMIDIPropertyNameConfiguration;
```

## See Also

### Configuration
- [let kMIDIPropertyNameConfigurationDictionary: CFString](./kmidipropertynameconfigurationdictionary.md)
  The device’s current patch, note, and control name values in MIDINameDocument XML format.
- [let kMIDIPropertyMaxSysExSpeed: CFString](./kmidipropertymaxsysexspeed.md)
  The maximum rate, in bytes per second, at which the system may reliably send System Exclusive (SysEx) messages to this object.
- [let kMIDIPropertyDriverDeviceEditorApp: CFString](./kmidipropertydriverdeviceeditorapp.md)
  The full path to an app on the system that configures driver-owned devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertynameconfiguration)*