# controls

**Framework**: Core Audio  
**Kind**: property

An array of AudioHardwareControls that represent the controls of the device.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var controls: [AudioHardwareControl] { get throws }
```

#### Discussion

If a notification is received for kAudioClockDevicePropertyControlList or kAudioObjectPropertyControlList, any cached AudioHardwareControl objects become invalid and need to be re-fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareclock/controls)*