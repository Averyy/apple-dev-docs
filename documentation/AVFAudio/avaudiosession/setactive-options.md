# setActive(_:options:)

**Framework**: AVFAudio  
**Kind**: method

Activates or deactivates your app’s audio session using the specified options.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setActive(_ active: Bool, options: AVAudioSession.SetActiveOptions = []) throws
```

#### Discussion

Your app may activate a session with category [`playback`](avaudiosession/category-swift.struct/playback.md) when another app is hosting a call, for example to start a `SharePlay` activity. However, your app isn’t permitted to capture the microphone of the active call.

> **Note**:  If you attempt to activate a session with category [`record`](avaudiosession/category-swift.struct/record.md) or [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) when another app is already hosting a call, then your session fails with the error [`AVAudioSessionErrorInsufficientPriority`](https://developer.apple.com/documentation/CoreAudioTypes/AVAudioSessionErrorInsufficientPriority).

 If you attempt to activate a session with category [`record`](avaudiosession/category-swift.struct/record.md) or [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) when another app is already hosting a call, then your session fails with the error [`AVAudioSessionErrorInsufficientPriority`](https://developer.apple.com/documentation/CoreAudioTypes/AVAudioSessionErrorInsufficientPriority).

The session fails to activate if another audio session has higher priority than yours (such as a phone call) and neither audio session allows mixing. Deactivating an audio session with running audio objects stops the objects, makes the session inactive, and returns an [`AVAudioSessionErrorCodeIsBusy`](https://developer.apple.com/documentation/coreaudiotypes/avaudiosessionerrorcode/avaudiosessionerrorcodeisbusy) error.

When your app deactivates a session, the return value is [`false`](https://developer.apple.com/documentation/foundation/nsexpression/1416488-false) but the active state changes to deactivate.

## Parameters

- `active`: Specify   to activate your app’s audio session, or   to deactivate it.
- `options`: An integer bit mask containing one or more constants from the   enumeration.

## Topics

### Data Types
- [AVAudioSession.SetActiveOptions](avaudiosession/setactiveoptions.md)
  Options that provide additional information about your app’s audio intentions upon session deactivation.

## See Also

- [func activate(options: AVAudioSessionActivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](avaudiosession/activate(options:completionhandler:).md)
  Activates an audio session asynchronously on watchOS.
- [struct AVAudioSessionActivationOptions](avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactive(_:options:))*