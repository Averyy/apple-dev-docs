# allowedAudioSpatializationFormats

**Framework**: AVFoundation  
**Kind**: property

The source audio channel layouts the audio renderer supports for spatialization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var allowedAudioSpatializationFormats: AVAudioSpatializationFormats { get set }
```

#### Discussion

The default property value is [`multichannel`](avaudiospatializationformats/multichannel.md), which tells the player to spatialize any decodable multichannel layout. Setting the value to [`monoStereoAndMultichannel`](avaudiospatializationformats/monostereoandmultichannel.md) tells the player to spatialize any decodable mono, stereo, or multichannel layout. When this property value is [`monoAndStereo`](avaudiospatializationformats/monoandstereo.md) the player attempts to spatialize content tagged with a stereo channel layout (two-channel content with no layout specified as well as mono).

This property isn’t key-value observable.

> ❗ **Important**:  It’s incorrect to render binaural recordings with spatialization. Content tagged with a binaural channel layout ignores this property value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/allowedaudiospatializationformats)*