# init(channelLayout:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a channel mixer with the given channel layout.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(channelLayout layout: AVAudioChannelLayout)
```

```objc
- (instancetype) initWithChannelLayout:(AVAudioChannelLayout *) layout;
```

## Parameters

- `layout`: A channel configuration for the mixer’s input audio.

## See Also

### Creating a Channel Mixer
- [convenience init(channelLayout: AVAudioChannelLayout, identifier: String)](./init%28channellayout,identifier%29.md)
  Creates a named channel mixer with the given channel layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasechannelmixerdefinition/init(channellayout:))*