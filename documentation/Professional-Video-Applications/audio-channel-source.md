# audio-channel-source

**Framework**: Professional-Video-Applications  
**Role**: Article

Defines an audio component by its source channels.

#### Overview

The `audio-channel-source` element defines an audio component for `clip` and `asset-clip` elements in terms of source channels in the underlying assets.

##### Audio Channel Attributes

The `audio-channel-source` element uses the attributes listed below to define its audio channel configuration:

| Attribute | Description |
| --- | --- |
| `srcCh` | The audio source channels in the containing `clip` element, such as “`1`, `2`”. Final Cut Pro sorts the channels from underlying assets by their `srcID` and then by their `srcCh`. |
| `outCh` | An indication of how the audio source channels are assigned to the output, such as “`L`, `R`”. |

The next code example reconfigures the audio on the primary timeline as dual mono, while mapping the audio on the anchored item to reverse stereo. Additionally, the example mutes the last 1 second of the anchored audio. The two mono audio components on the primary timeline has roles as `dialogue.dialogue-1` and `dialog.dialogue-2`, while the reverse stereo audio component in the anchored item has a role as `music.music-1`.

```swift
<asset-clip name="MyVideo" ref="r2" start="0s" duration="5s" audioRole="dialogue">
   <asset-clip name="MyAudio" ref="r3" lane="-1" start="10s" duration="5s" audioRole="music">
      <audio-channel-source role="music.music-1" srcCh="2, 1">
         <mute start="14s" duration="1s" />
      </audio-channel-source>
   </asset-clip>
   <audio-channel-source role="dialogue.dialogue-1" srcCh="1" />
   <audio-channel-source role="dialogue.dialogue-2" srcCh="2" />
</asset-clip>
```

## See Also

### Audio Component Configuration
- [audio-role-source](./audio-role-source.md)
  Defines an audio component by its role.
- [mute](./mute.md)
  Suppresses audio output for the audio component over a range of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/audio-channel-source)*