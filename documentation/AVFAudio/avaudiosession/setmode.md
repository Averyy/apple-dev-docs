# setMode(_:)

**Framework**: Avfaudio  
**Kind**: method

Sets the audio session’s mode.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setMode(_ mode: AVAudioSession.Mode) throws
```

#### Discussion

The audio session’s category and mode together define how your app uses audio. Typically, you set the category and mode before activating the session. You can also set the category or mode while the session is active, but doing so results in an immediate change.

> **Note**:  Instead of setting your [`category`](avaudiosession/category-swift.property.md) and [`mode`](avaudiosession/mode-swift.property.md) properties independently, set them at the same time using the [`setCategory(_:mode:options:)`](avaudiosession/setcategory(_:mode:options:).md) or [`setCategory(_:mode:policy:options:)`](avaudiosession/setcategory(_:mode:policy:options:).md) method.

## Parameters

- `mode`: The audio session mode to apply to the audio session. See   for supported mode values.

## See Also

- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, policy: AVAudioSession.RouteSharingPolicy, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:mode:policy:options:).md)
  Sets the session category, mode, route-sharing policy, and options.
- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:mode:options:).md)
  Sets the audio session’s category, mode, and options.
- [func setCategory(AVAudioSession.Category, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:options:).md)
  Sets the audio session’s category with the specified options.
- [func setCategory(AVAudioSession.Category) throws](avaudiosession/setcategory(_:).md)
  Sets the audio session’s category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setmode(_:))*