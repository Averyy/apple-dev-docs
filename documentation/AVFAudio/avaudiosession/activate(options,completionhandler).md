# activate(options:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Activates an audio session asynchronously.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 5.0+

## Declaration

```swift
func activate(options: AVAudioSessionActivationOptions = [], completionHandler handler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func activate(options: AVAudioSessionActivationOptions = []) async throws -> Bool
```

```objc
- (void) activateWithOptions:(AVAudioSessionActivationOptions) options completionHandler:(void (^)(BOOL activated, NSError *error)) handler;
```

## Discussion

Configure the session before activating it: call [`setCategory(_:mode:policy:options:)`](./setcategory%28_,mode,policy,options%29.md) to set the category and route sharing policy you need.

This method begins activating the audio session asynchronously. The system calls the completion handler as soon as the session has successfully activated or if the activation fails.

## Activate playback on watchOS

On watchOS, activating a session with the [`playback`](./category-swift.struct/playback.md) category and the [`AVAudioSession.RouteSharingPolicy.longFormAudio`](./routesharingpolicy-swift.enum/longformaudio.md) or [`AVAudioSession.RouteSharingPolicy.longFormVideo`](./routesharingpolicy-swift.enum/longformvideo.md) route-sharing policy requires a Bluetooth output route. On supported Apple Watch models running watchOS 11.0 or later, the built-in speaker also satisfies this routing requirement.

The system selects a reachable route automatically when one is available. If no Bluetooth route is available, or when supported AirPods or Beats headphones are nearby:

- If the watch supports speaker playback, the system routes to the watch’s built-in speaker.
- If the watch does not support speaker playback, the system presents the route picker. If the user dismisses the picker without selecting a valid route, the system calls the completion handler with false.

The system only presents the audio route picker for the [`playback`](./category-swift.struct/playback.md) category and [`longForm`](./routesharingpolicy-swift.enum/longform.md) route sharing policy. Use the [`activate(options:completionHandler:)`](./activate%28options,completionhandler%29.md) method instead of [`setActive(_:options:)`](./setactive%28_,options%29.md) to authorize other categories and sharing policies.

> **Note**: On watchOS, long-form audio can’t play through the built-in speaker while the watch is charging.

## Parameters

- `options`: The options to apply when activating the session.
- `handler`: The callback the system invokes when the operation completes.

## See Also

### Activating and deactivating the session
- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](./setactive%28_,options%29.md)
  Activates or deactivates your app’s audio session using the specified options.
- [func deactivate(options: AVAudioSessionDeactivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](./deactivate%28options,completionhandler%29.md)
  Deactivates the audio session asynchronously.
- [struct AVAudioSessionActivationOptions](../avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.
- [struct AVAudioSessionDeactivationOptions](../avaudiosessiondeactivationoptions.md)
  Options for deactivating an AVAudioSession
- [- setActive:error:](./setactive_error_.md)
  Activates or deactivates your app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/activate(options:completionhandler:))*