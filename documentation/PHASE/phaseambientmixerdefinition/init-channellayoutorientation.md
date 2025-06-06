# init(channelLayout:orientation:)

**Framework**: PHASE  
**Kind**: init

Creates an ambient mixer with the given channel layout and orientation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(channelLayout layout: AVAudioChannelLayout, orientation: simd_quatf)
```

## Parameters

- `layout`: The channel layout of input audio.
- `orientation`: A quaternion that describes the orientation of the speaker layout relative to the scene origin.

## See Also

- [convenience init(channelLayout: AVAudioChannelLayout, orientation: simd_quatf, identifier: String)](phaseambientmixerdefinition/init(channellayout:orientation:identifier:).md)
  Creates a named ambient mixer with the given channel layout and orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseambientmixerdefinition/init(channellayout:orientation:))*