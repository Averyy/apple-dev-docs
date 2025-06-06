# setCategory(_:mode:policy:options:)

**Framework**: AVFAudio  
**Kind**: method

Sets the session category, mode, route-sharing policy, and options.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func setCategory(_ category: AVAudioSession.Category, mode: AVAudioSession.Mode, policy: AVAudioSession.RouteSharingPolicy, options: AVAudioSession.CategoryOptions = []) throws
```

#### Discussion

You specify options only with a default routing policy. With a long-form route-sharing policy, you can use the [`playback`](avaudiosession/category-swift.struct/playback.md) category and the [`default`](avaudiosession/mode-swift.struct/default.md), [`moviePlayback`](avaudiosession/mode-swift.struct/movieplayback.md), and [`spokenAudio`](avaudiosession/mode-swift.struct/spokenaudio.md) modes.

## Parameters

- `category`: The category to apply to the audio session. See   for supported category values.
- `mode`: The audio session mode to apply to the audio session. For a list of values, see  .
- `policy`: The route-sharing policy to apply to the audio session. For a list of values, see  .
- `options`: A mask of additional options for handling audio. For a list of constants, see  .

## See Also

- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:mode:options:).md)
  Sets the audio session’s category, mode, and options.
- [func setCategory(AVAudioSession.Category, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:options:).md)
  Sets the audio session’s category with the specified options.
- [func setCategory(AVAudioSession.Category) throws](avaudiosession/setcategory(_:).md)
  Sets the audio session’s category.
- [func setMode(AVAudioSession.Mode) throws](avaudiosession/setmode(_:).md)
  Sets the audio session’s mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setcategory(_:mode:policy:options:))*