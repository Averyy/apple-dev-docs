# setCategory(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets the audio session’s category.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setCategory(_ category: AVAudioSession.Category) throws
```

```objc
- (BOOL) setCategory:(AVAudioSessionCategory) category error:(NSError **) outError;
```

#### Discussion

The audio session’s category defines how the app uses audio. Typically, you set the category before activating the session. You can also set the category while the session is active, but this results in an immediate route change.

> **Note**:  Instead of setting your [`category`](./category-swift.property.md) and [`mode`](./mode-swift.property.md) properties independently, set them at the same time using the [`setCategory(_:mode:options:)`](./setcategory%28_,mode,options%29.md) or [`setCategory(_:mode:policy:options:)`](./setcategory%28_,mode,policy,options%29.md) method.

## Parameters

- `category`: The category to apply to the audio session. See [`AVAudioSession.Category`](./category-swift.struct.md) for supported category values.

## See Also

### Configuring standard audio behaviors
- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, policy: AVAudioSession.RouteSharingPolicy, options: AVAudioSession.CategoryOptions) throws](./setcategory%28_,mode,policy,options%29.md)
  Sets the session category, mode, route-sharing policy, and options.
- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, options: AVAudioSession.CategoryOptions) throws](./setcategory%28_,mode,options%29.md)
  Sets the audio session’s category, mode, and options.
- [func setCategory(AVAudioSession.Category, options: AVAudioSession.CategoryOptions) throws](./setcategory%28_,options%29.md)
  Sets the audio session’s category with the specified options.
- [func setMode(AVAudioSession.Mode) throws](./setmode%28_%29.md)
  Sets the audio session’s mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setcategory(_:))*