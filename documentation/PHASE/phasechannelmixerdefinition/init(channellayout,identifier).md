# init(channelLayout:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a named channel mixer with the given channel layout.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(channelLayout layout: AVAudioChannelLayout, identifier: String)
```

```objc
- (instancetype) initWithChannelLayout:(AVAudioChannelLayout *) layout identifier:(NSString *) identifier;
```

## Parameters

- `layout`: A channel configuration for the mixer’s input audio.
- `identifier`: A unique name for the channel mixer.

## See Also

### Creating a Channel Mixer
- [init(channelLayout: AVAudioChannelLayout)](./init%28channellayout%29.md)
  Creates a channel mixer with the given channel layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasechannelmixerdefinition/init(channellayout:identifier:))*