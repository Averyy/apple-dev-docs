# activate(options:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

Activates an audio session asynchronously.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 5.0+

## Declaration

```swift
func activate(options: AVAudioSessionActivationOptions = []) async throws -> Bool
```

#### Discussion

Configure the session before activating it: call [`setCategory(_:mode:policy:options:)`](avaudiosession/setcategory(_:mode:policy:options:).md) to set the category and route sharing policy you need.

This method begins activating the audio session asynchronously. The system calls the completion handler as soon as the session has successfully activated or if the activation fails.

#### Activate Playback on Watchos

On watchOS, activating a session with the [`playback`](avaudiosession/category-swift.struct/playback.md) category and the [`AVAudioSession.RouteSharingPolicy.longFormAudio`](avaudiosession/routesharingpolicy-swift.enum/longformaudio.md) or [`AVAudioSession.RouteSharingPolicy.longFormVideo`](avaudiosession/routesharingpolicy-swift.enum/longformvideo.md) route-sharing policy requires a Bluetooth output route. On supported Apple Watch models running watchOS 11.0 or later, the built-in speaker also satisfies this routing requirement.

The system selects a reachable route automatically when one is available. If no Bluetooth route is available, or when supported AirPods or Beats headphones are nearby:

- If the watch supports speaker playback, the system routes to the watch’s built-in speaker.
- If the watch does not support speaker playback, the system presents the route picker. If the user dismisses the picker without selecting a valid route, the system calls the completion handler with false.

The system only presents the audio route picker for the [`playback`](avaudiosession/category-swift.struct/playback.md) category and [`longForm`](avaudiosession/routesharingpolicy-swift.enum/longform.md) route sharing policy. Use the [`activate(options:completionHandler:)`](avaudiosession/activate(options:completionhandler:).md) method instead of [`setActive(_:options:)`](avaudiosession/setactive(_:options:).md) to authorize other categories and sharing policies.

> **Note**: On watchOS, long-form audio can’t play through the built-in speaker while the watch is charging.

## Parameters

- `options`: The options to apply when activating the session.
- `handler`: The callback the system invokes when the operation completes.

## See Also

- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](avaudiosession/setactive(_:options:).md)
  Activates or deactivates your app’s audio session using the specified options.
- [func deactivate(options: AVAudioSessionDeactivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](avaudiosession/deactivate(options:completionhandler:).md)
  Deactivates the audio session asynchronously.
- [struct AVAudioSessionActivationOptions](avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.
- [struct AVAudioSessionDeactivationOptions](avaudiosessiondeactivationoptions.md)
  Options for deactivating an AVAudioSession


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/activate(options:completionhandler:))*