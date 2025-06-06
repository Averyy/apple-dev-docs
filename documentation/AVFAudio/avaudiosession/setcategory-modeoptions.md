# setCategory(_:mode:options:)

**Framework**: AVFAudio  
**Kind**: method

Sets the audio session’s category, mode, and options.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func setCategory(_ category: AVAudioSession.Category, mode: AVAudioSession.Mode, options: AVAudioSession.CategoryOptions = []) throws
```

#### Discussion

The audio session’s [`category`](avaudiosession/category-swift.property.md) and [`mode`](avaudiosession/mode-swift.property.md) together define how your app uses audio. Typically, you set the category and mode before activating the session. You can also set the category or mode while the session is active, but doing so results in an immediate change.

## Parameters

- `category`: The category to apply to the audio session. See   for supported category values.
- `mode`: The audio session mode to apply to the audio session. For a list of values, see  .
- `options`: A mask of additional options for handling audio. For a list of constants, see  .

## See Also

- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, policy: AVAudioSession.RouteSharingPolicy, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:mode:policy:options:).md)
  Sets the session category, mode, route-sharing policy, and options.
- [func setCategory(AVAudioSession.Category, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:options:).md)
  Sets the audio session’s category with the specified options.
- [func setCategory(AVAudioSession.Category) throws](avaudiosession/setcategory(_:).md)
  Sets the audio session’s category.
- [func setMode(AVAudioSession.Mode) throws](avaudiosession/setmode(_:).md)
  Sets the audio session’s mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setcategory(_:mode:options:))*