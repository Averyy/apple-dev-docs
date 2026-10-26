# Audio Components and Multicam

**Framework**: Professional-Video-Applications  
**Role**: Article

Specify configuration of audio components using the `mc-clip` element.

#### Overview

Configure the following audio components using the `mc-clip` element:

- Enabling or disabling the component
- Mute ranges
- Volume and other audio adjustments
- Audio filters

The code listing below is a multicam project example based on the first code listing in the [Multicam Media](./multicam-media.md) page, with two multicam clips that have reconfigured audio components. The first clip has its audio trimmed at both ends as a JL cut. The second angle in the second clip has its audio muted for 5 seconds in its middle section.

```swift
<project name="MyProject">   
  <sequence duration="40s" format="r2">
      <spine>
         <mc-clip name="MyMulticamClip" offset="0s" ref="r1" duration="20s">
            <mc-source angleID="a1" srcEnable="all">
               <audio-role-source role="dialogue.dialogue-1" start="1s" duration="18s" />
            </mc-source>
         </mc-clip>
         <mc-clip name="MyMulticamClip" offset="20s" ref="r1" duration="20s">
            <mc-source angleID="a1" srcEnable="video" />
            <mc-source angleID="a2" srcEnable="audio">
               <audio-role-source role="dialogue.dialogue-1">
                  <mute start="5s" duration="10s" />
               </audio-role-source>
            </mc-source>
         </mc-clip>
      </spine>
   </sequence>
</project>
```

As of FCPXML 1.2, `mc-source` elements no longer support audio filters. Instead, you apply audio filters to an `mc-clip` element, which applies the effect to all active audio source angles, or to an `audio-source` element, which only applies the effect to the individual audio source, if active. Existing FCPXML 1.1 projects with audio angles on an `mc-clip` element are converted to 1.2 and later format on import.

In FCPXML 1.6, use the `audio-role-source` element  to apply audible adjustments and audio filters to an audio component identified by its role.

## See Also

### Multicam Media
- [Multicam Media](./multicam-media.md)
  Assemble angles from a multi-camera shooting as a unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/audio-components-and-multicam)*