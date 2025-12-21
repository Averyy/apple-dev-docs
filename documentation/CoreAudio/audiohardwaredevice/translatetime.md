# translateTime(_:)

**Framework**: Core Audio  
**Kind**: method

Translates the time in the device’s time base from one representation to another. Note that the device has to be running

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func translateTime(_ timestamp: AudioTimeStamp) throws -> AudioTimeStamp
```

#### Return Value

An AudioTimeStamp containing the translated time.

## Parameters

- `timestamp`: An AudioTimeStamp containing the time to be translated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/translatetime(_:))*