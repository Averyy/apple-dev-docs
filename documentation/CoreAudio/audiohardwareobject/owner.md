# owner

**Framework**: Core Audio  
**Kind**: property

An AudioHardwareObject that identifies this object’s owner. Note that all AudioHardwareObject are owned by some other AudioHardwareObject. The only exception is the AudioSystemObject, for which the value of this property is nil.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var owner: AudioHardwareObject? { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject/owner)*