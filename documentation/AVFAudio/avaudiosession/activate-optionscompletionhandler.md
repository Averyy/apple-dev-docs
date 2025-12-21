# activate(options:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

Activates an audio session asynchronously on watchOS.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
func activate(options: AVAudioSessionActivationOptions = []) async throws -> Bool
```

#### Discussion

Use this method to play long-form audio—such as music, podcasts, or audio books—on Apple Watch. Before calling this method to activate longform playback, you must call [`setCategory(_:mode:policy:options:)`](avaudiosession/setcategory(_:mode:policy:options:).md), set the category to [`playback`](avaudiosession/category-swift.struct/playback.md), and route sharing policy to [`longForm`](avaudiosession/routesharingpolicy-swift.enum/longform.md).

This method asynchronously activates the audio session. The system calls the completion handler as soon as the session has successfully activated or if the activation fails.

Playback of long-form audio on watchOS requires a Bluetooth audio route. If necessary, the system presents an audio route picker to the user, letting them choose the Bluetooth route. If the user has previously selected a Bluetooth route or if AirPods or other W1-equipped Bluetooth headphones are nearby, the system automatically picks the audio route without displaying a picker view to the user. If no applicable Bluetooth route is selected (either automatically or by the user), the system passes an error to the completion handler.

> **Note**:  You may use the [`activate(options:completionHandler:)`](avaudiosession/activate(options:completionhandler:).md) method instead of the [`setActive(_:options:)`](avaudiosession/setactive(_:options:).md) method to authorize other categories and sharing policies. The system only presents the audio route picker for the [`playback`](avaudiosession/category-swift.struct/playback.md) category and [`longForm`](avaudiosession/routesharingpolicy-swift.enum/longform.md) route sharing policy.

## Parameters

- `options`: The options to apply when activating the session.
- `handler`: The callback the system invokes when the operation completes.

## See Also

- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](avaudiosession/setactive(_:options:).md)
  Activates or deactivates your app’s audio session using the specified options.
- [struct AVAudioSessionActivationOptions](avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/activate(options:completionhandler:))*