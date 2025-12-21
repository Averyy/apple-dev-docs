# powerHint

**Framework**: Core Audio  
**Kind**: property

An AudioHardwarePowerHint enum which allows a process to indicate how aggressive the system can be with optimizations that save power. The default value is none.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var powerHint: AudioHardwarePowerHint { get throws }
```

#### Discussion

Note that the value of this property can be set in an application’s info.plist using the key, “AudioHardwarePowerHint”. The values for this key are the strings that correspond to the values in the Power Hints enum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/powerhint)*