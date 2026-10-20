# AudioServicesPlayAlertSoundWithCompletion(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioServicesPlayAlertSoundWithCompletion(_ inSystemSoundID: SystemSoundID, _ inCompletionBlock: (() -> Void)?)
```

```c
extern void AudioServicesPlayAlertSoundWithCompletion(SystemSoundID inSystemSoundID, void (^inCompletionBlock)());
```

## See Also

### Playing Sounds
- [func AudioServicesPlaySystemSoundWithCompletion(SystemSoundID, (() -> Void)?)](./audioservicesplaysystemsoundwithcompletion%28_,_%29.md)
- [func AudioServicesPlayAlertSound(SystemSoundID)](./audioservicesplayalertsound%28_%29.md)
  Plays a system sound as an alert.
- [func AudioServicesPlaySystemSound(SystemSoundID)](./audioservicesplaysystemsound%28_%29.md)
  Plays a system sound object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesplayalertsoundwithcompletion(_:_:))*