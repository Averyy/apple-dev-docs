# Compound Clip Media

**Framework**: Professional-Video-Applications  
**Role**: Article

Group combination of clips as a unit.

#### Overview

A compound clip media is a clip you construct out of audio or video clip components, and which you can reference as a unit. Use the `sequence` element to describe its top-level sequence.

The code example below shows a compound clip definition with two clips laid down in series inside a `spine` element and then under a `sequence` element:

```swift
<resources>
   <media id="r1" name="MyCompoundClip">
      <sequence format="r2">
         <spine>
            <asset-clip name="MyMovie1" offset="0s" ref="r3" duration="10s" audioRole="dialogue" />
            <asset-clip name="MyMovie2" offset="0s" ref="r4" duration="20s" audioRole="dialogue" />
         </spine>
      </sequence>
   </media>
   <format id="r2" name="FFVideoFormat1080p30" />
   <asset id="r3" name="MyMovie1" src="file:///Volumes/Media/MyMovie1.mov" start="0s" duration="10s" hasVideo="1" format="r2" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000" />
   <asset id="r4" name="MyMovie2" src="file:///Volumes/Media/MyMovie2.mov" start="0s" duration="20s" hasVideo="1" format="r2" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000" />
</resources>

```

##### Using Compound Clip

To use the compound clip media as a clip, add a `ref-clip` element that references the media in the timeline. Each `ref-clip` element uses audio and video from the compound clip media. Call out audio components from the compound clip by their roles and apply adjustments or effects. For information on configuring audio components in compound clips, see [Audio Components in Compound Clips](./audio-components-in-compound-clips.md).

The code listing below refers to the compound clip defined in the previous code example:

```swift
<ref-clip ref="r4" name="MyCompoundClip" duration="10s"/>
```

## See Also

### Compound Clip Media
- [Audio Components in Compound Clips](./audio-components-in-compound-clips.md)
  Manipulate audio components in compound clips based on each clip’s role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/compound-clip-media)*