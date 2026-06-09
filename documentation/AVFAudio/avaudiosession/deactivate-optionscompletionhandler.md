# deactivate(options:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

Deactivates the audio session asynchronously.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func deactivate(options: AVAudioSessionDeactivationOptions = []) async throws -> Bool
```

#### Discussion

This method returns immediately without blocking the calling thread. The system calls the completion handler with the result.

## Parameters

- `options`: Deactivation options.
- `handler`: A completion handler called with a success flag and an error if deactivation failed.

## See Also

- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](avaudiosession/setactive(_:options:).md)
  Activates or deactivates your app’s audio session using the specified options.
- [func activate(options: AVAudioSessionActivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](avaudiosession/activate(options:completionhandler:).md)
  Activates an audio session asynchronously on watchOS.
- [struct AVAudioSessionActivationOptions](avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.
- [struct AVAudioSessionDeactivationOptions](avaudiosessiondeactivationoptions.md)
  Options for deactivating an AVAudioSession


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivate(options:completionhandler:))*