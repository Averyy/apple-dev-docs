# init(channelLayout:orientation:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a named ambient mixer with the given channel layout and orientation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(channelLayout layout: AVAudioChannelLayout, orientation: simd_quatf, identifier: String)
```

```objc
- (instancetype) initWithChannelLayout:(AVAudioChannelLayout *) layout orientation:(simd_quatf) orientation identifier:(NSString *) identifier;
```

## Parameters

- `layout`: The channel layout of input audio.
- `orientation`: A quaternion that describes the orientation of the speaker layout relative to the scene origin.
- `identifier`: A unique name for the mixer.

## See Also

### Creating an Ambient Mixer
- [init(channelLayout: AVAudioChannelLayout, orientation: simd_quatf)](./init%28channellayout,orientation%29.md)
  Creates an ambient mixer with the given channel layout and orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseambientmixerdefinition/init(channellayout:orientation:identifier:))*