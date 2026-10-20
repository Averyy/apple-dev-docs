# AppLock.App.Options

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary of options to set for the app.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS 10.2+

## Declaration

```
object AppLock.App.Options
```

## Properties

- `DisableAutoLock` (boolean): If `true`, the device doesn’t automatically go to sleep after an idle period.

  **Default**: `false`
- `DisableDeviceRotation` (boolean): If `true`, the system disables device rotation sensing.

  Available: iOS 7+ | iPadOS 7+

  **Default**: `false`
- `DisableRingerSwitch` (boolean): If `true`, the system disables the ringer switch. When disabled, the ringer behavior depends on what position the switch was in when it was first disabled.

  Available: iOS 7+ | iPadOS 7+

  **Default**: `false`
- `DisableSleepWakeButton` (boolean): If `true`, the system disables the sleep/wake button.

  Available: iOS 7+ | iPadOS 7+

  **Default**: `false`
- `DisableTouch` (boolean): If `true`, the system disables the touch screen. In tvOS, it disables the touch surface on the Apple TV Remote.

  **Default**: `false`
- `DisableVolumeButtons` (boolean): If `true`, the system disables the volume buttons.

  Available: iOS 7+ | iPadOS 7+

  **Default**: `false`
- `EnableAssistiveTouch` (boolean): If `true`, the system enables AssistiveTouch.

  Available: iOS 7+ | iPadOS 7+

  **Default**: `false`
- `EnableInvertColors` (boolean): If `true`, the system enables Invert Colors.

  **Default**: `false`
- `EnableMonoAudio` (boolean): If `true`, the system enables Mono Audio.

  Available: iOS 7+ | iPadOS 7+

  **Default**: `false`
- `EnableSpeakSelection` (boolean): If `true`, the system enables Speak Selection.

  Available: iOS 7+ | iPadOS 7+

  **Default**: `false`
- `EnableVoiceControl` (boolean): If `true`, the system enables Voice Control.

  Available: iOS 13+ | iPadOS 13+

  **Default**: `false`
- `EnableVoiceOver` (boolean): If `true`, the system enables VoiceOver.

  **Default**: `false`
- `EnableZoom` (boolean): If `true`, the system enables Zoom.

  **Default**: `false`

## See Also

### Objects
- [object AppLock.App.UserEnabledOptions](./userenabledoptions-data.dictionary.md)
  The dictionary of user-editable options to set for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/applock/app-data.dictionary/options-data.dictionary)*