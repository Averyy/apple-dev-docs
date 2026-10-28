# deactivate(options:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Deactivates the audio session asynchronously.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func deactivate(options: AVAudioSessionDeactivationOptions = [], completionHandler handler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func deactivate(options: AVAudioSessionDeactivationOptions = []) async throws -> Bool
```

```objc
- (void) deactivateWithOptions:(AVAudioSessionDeactivationOptions) options completionHandler:(void (^)(BOOL deactivated, NSError *error)) handler;
```

## Discussion

This method returns immediately without blocking the calling thread. The system calls the completion handler with the result.

## Parameters

- `options`: Deactivation options.
- `handler`: A completion handler called with a success flag and an error if deactivation failed.

## See Also

### Activating and deactivating the session
- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](./setactive%28_,options%29.md)
  Activates or deactivates your app’s audio session using the specified options.
- [func activate(options: AVAudioSessionActivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](./activate%28options,completionhandler%29.md)
  Activates an audio session asynchronously.
- [struct AVAudioSessionActivationOptions](../avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.
- [struct AVAudioSessionDeactivationOptions](../avaudiosessiondeactivationoptions.md)
  Options for deactivating an AVAudioSession
- [- setActive:error:](./setactive_error_.md)
  Activates or deactivates your app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivate(options:completionhandler:))*