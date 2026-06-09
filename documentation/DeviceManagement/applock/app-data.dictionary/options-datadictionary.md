# AppLock.App.Options

**Framework**: Device Management  
**Kind**: dictionary

The dictionary of options to set for the app.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS 10.2+

## Declaration

```swift
object AppLock.App.Options
```

## Properties

- `DisableAutoLock` (boolean): If `true`, the device doesn’t automatically go to sleep after an idle period.
- `DisableDeviceRotation` (boolean): If `true`, the system disables device rotation sensing. Available: iOS 7+ | iPadOS 7+
- `DisableRingerSwitch` (boolean): If `true`, the system disables the ringer switch. When disabled, the ringer behavior depends on what position the switch was in when it was first disabled. Available: iOS 7+ | iPadOS 7+
- `DisableSleepWakeButton` (boolean): If `true`, the system disables the sleep/wake button. Available: iOS 7+ | iPadOS 7+
- `DisableTouch` (boolean): If `true`, the system disables the touch screen. In tvOS, it disables the touch surface on the Apple TV Remote.
- `DisableVolumeButtons` (boolean): If `true`, the system disables the volume buttons. Available: iOS 7+ | iPadOS 7+
- `EnableAssistiveTouch` (boolean): If `true`, the system enables AssistiveTouch. Available: iOS 7+ | iPadOS 7+
- `EnableInvertColors` (boolean): If `true`, the system enables Invert Colors.
- `EnableMonoAudio` (boolean): If `true`, the system enables Mono Audio. Available: iOS 7+ | iPadOS 7+
- `EnableSpeakSelection` (boolean): If `true`, the system enables Speak Selection. Available: iOS 7+ | iPadOS 7+
- `EnableVoiceControl` (boolean): If `true`, the system enables Voice Control. Available: iOS 13+ | iPadOS 13+
- `EnableVoiceOver` (boolean): If `true`, the system enables VoiceOver.
- `EnableZoom` (boolean): If `true`, the system enables Zoom.

## See Also

- [object AppLock.App.UserEnabledOptions](applock/app-data.dictionary/userenabledoptions-data.dictionary.md)
  The dictionary of user-editable options to set for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/applock/app-data.dictionary/options-data.dictionary)*