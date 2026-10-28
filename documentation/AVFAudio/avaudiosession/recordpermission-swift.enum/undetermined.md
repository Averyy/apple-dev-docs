# AVAudioSession.RecordPermission.undetermined

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A value that indicates that the user hasn’t granted or denied recording permission.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0 (renamed: AVAudioApplication.recordPermission.undetermined)
- iPadOS 8.0+ - Deprecated in 17.0 (renamed: AVAudioApplication.recordPermission.undetermined)
- Mac Catalyst 13.1+ - Deprecated in 17.0 (renamed: AVAudioApplication.recordPermission.undetermined)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: AVAudioApplication.recordPermission.undetermined)
- watchOS 4.0+ - Deprecated in 10.0 (renamed: AVAudioApplication.recordPermission.undetermined)

## Declaration

```swift
case undetermined
```

```c
AVAudioSessionRecordPermissionUndetermined
```

## Discussion

A permission of [`AVAudioSession.RecordPermission.undetermined`](./undetermined.md) typically means that your app hasn’t requested, or is in the process of requesting, recording permission.

## See Also

### Checking record permissions
- [AVAudioSession.RecordPermission.denied](./denied.md)
  A value that indicates that the user has denied recording permission.
- [AVAudioSession.RecordPermission.granted](./granted.md)
  A value that indicates that the user has granted recording permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/recordpermission-swift.enum/undetermined)*