# setActive(_:options:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) setActive:(BOOL) active withOptions:(AVAudioSessionSetActiveOptions) options error:(NSError **) outError;
```

#### Discussion

Your app may activate a session with category [`playback`](./category-swift.struct/playback.md) when another app is hosting a call, for example to start a `SharePlay` activity. However, your app isn’t permitted to capture the microphone of the active call.

> **Note**:  If you attempt to activate a session with category [`record`](./category-swift.struct/record.md) or [`playAndRecord`](./category-swift.struct/playandrecord.md) when another app is already hosting a call, then your session fails with the error [`AVAudioSessionErrorInsufficientPriority`](../../CoreAudioTypes/avaudiosessionerrorinsufficientpriority.md).

The session fails to activate if another audio session has higher priority than yours (such as a phone call) and neither audio session allows mixing. Deactivating an audio session with running audio objects stops the objects, makes the session inactive, and returns an [`AVAudioSession.ErrorCode.isBusy`](../../CoreAudioTypes/avaudiosession/errorcode/isbusy.md) error.

When your app deactivates a session, the return value is [`false`](../../Foundation/nsexpression/false.md) but the active state changes to deactivate.

## Parameters

- `active`: Specify [`true`](../../Swift/true.md) to activate your app’s audio session, or [`false`](../../Swift/false.md) to deactivate it.
- `options`: An integer bit mask containing one or more constants from the [`AVAudioSession.SetActiveOptions`](./setactiveoptions.md) enumeration.

## Topics

### Activation options
- [AVAudioSession.SetActiveOptions](./setactiveoptions.md)
  Options that provide additional information about your app’s audio intentions upon session deactivation.

## See Also

### Activating and deactivating the session
- [func activate(options: AVAudioSessionActivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](./activate%28options,completionhandler%29.md)
  Activates an audio session asynchronously.
- [func deactivate(options: AVAudioSessionDeactivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](./deactivate%28options,completionhandler%29.md)
  Deactivates the audio session asynchronously.
- [struct AVAudioSessionActivationOptions](../avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.
- [struct AVAudioSessionDeactivationOptions](../avaudiosessiondeactivationoptions.md)
  Options for deactivating an AVAudioSession


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactive(_:options:))*