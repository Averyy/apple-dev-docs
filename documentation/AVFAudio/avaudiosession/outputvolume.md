# outputVolume

**Framework**: AVFAudio  
**Kind**: property

The systemwide output volume set by the user.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var outputVolume: Float { get }
```

#### Discussion

This property returns a value in the range `0.0` to `1.0`, with `0.0` representing the minimum volume, and `1.0` representing the maximum volume.

Only the user can directly set the system volume. Provide a volume control in your app, using [`MPVolumeView`](https://developer.apple.com/documentation/MediaPlayer/MPVolumeView), to provide the interface to adjust the system volume.

You can observe changes to the value of this property by using [`Key-value observing`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/outputvolume)*