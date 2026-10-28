# Audio Components in Compound Clips

**Framework**: Professional-Video-Applications  
**Role**: Article

Manipulate audio components in compound clips based on each clip’s role.

## Overview

When you reference a compound clip in a timeline, you can manipulate its audio components based on the clip’s role. By default, Final Cut Pro merges components from the compound clip with the same main role into a single component. Override this behavior to see the individual subroles by setting the `ref-clip` element’s `useAudioSubroles` attribute to 1.

In the code listing below, the `ref-clip` element references a compound clip, created from the clip from the first clode listing in the [Compound Clip Media](./compound-clip-media.md) page. Because the `useAudioSubroles` attribute is set to `1`, all subroles are accessible. The example applies `Rumble Reducer` effect on the two components with the `dialogue` subroles. The volume on the component with the `music.music-1` subrole is turned down by `6dB`.

```swift
<ref-clip name="MyCompoundClip" ref="r1" duration="5s" useAudioSubroles="1">   <audio-role-source role="dialogue.dialogue-1">
      <filter-audio ref="r6" name="Rumble Reducer" />
   </audio-role-source>
   <audio-role-source role="dialogue.dialogue-2">
      <filter-audio ref="r6" name="Rumble Reducer" />
   </audio-role-source>
   <audio-role-source role="music.music-1">
      <adjust-volume amount="-6dB" />
   </audio-role-source>
</ref-clip>
```

## See Also

### Compound Clip Media
- [Compound Clip Media](./compound-clip-media.md)
  Group combination of clips as a unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/audio-components-in-compound-clips)*