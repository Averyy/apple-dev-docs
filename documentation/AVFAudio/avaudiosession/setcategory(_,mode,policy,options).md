# setCategory(_:mode:policy:options:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) setCategory:(AVAudioSessionCategory) category mode:(AVAudioSessionMode) mode routeSharingPolicy:(AVAudioSessionRouteSharingPolicy) policy options:(AVAudioSessionCategoryOptions) options error:(NSError **) outError;
```

## Discussion

You specify options only with a default routing policy. With a long-form route-sharing policy, you can use the [`playback`](./category-swift.struct/playback.md) category and the [`default`](./mode-swift.struct/default.md), [`moviePlayback`](./mode-swift.struct/movieplayback.md), and [`spokenAudio`](./mode-swift.struct/spokenaudio.md) modes.

## Parameters

- `category`: The category to apply to the audio session. See [`AVAudioSession.Category`](./category-swift.struct.md) for supported category values.
- `mode`: The audio session mode to apply to the audio session. For a list of values, see [`AVAudioSession.Mode`](./mode-swift.struct.md).
- `policy`: The route-sharing policy to apply to the audio session. For a list of values, see [`AVAudioSession.RouteSharingPolicy`](./routesharingpolicy-swift.enum.md).
- `options`: A mask of additional options for handling audio. For a list of constants, see [`AVAudioSession.CategoryOptions`](./categoryoptions-swift.struct.md).

## See Also

### Configuring standard audio behaviors
- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, options: AVAudioSession.CategoryOptions) throws](./setcategory%28_,mode,options%29.md)
  Sets the audio session’s category, mode, and options.
- [func setCategory(AVAudioSession.Category, options: AVAudioSession.CategoryOptions) throws](./setcategory%28_,options%29.md)
  Sets the audio session’s category with the specified options.
- [func setCategory(AVAudioSession.Category) throws](./setcategory%28_%29.md)
  Sets the audio session’s category.
- [func setMode(AVAudioSession.Mode) throws](./setmode%28_%29.md)
  Sets the audio session’s mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setcategory(_:mode:policy:options:))*