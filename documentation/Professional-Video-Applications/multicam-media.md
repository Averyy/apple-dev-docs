# Multicam Media

**Framework**: Professional-Video-Applications  
**Role**: Article

Assemble angles from a multi-camera shooting as a unit.

## Overview

A multicam media describes a collection of angles shot at the same time from multiple angles. Assemble footages synchronized in time from multiple cameras, or angles, using the `multicam` element. The `mc-angle` element describes the construction of each angle.

| Multicam Media Elements | Attributes |
| --- | --- |
| `multicam` | A root container for angles of related media, organized as `mc-angle` elements. |
| `mc-angle` | A container of story elements organized sequentially in time. |

> **Note**:  FCPXML 1.1 added support for multicam editing to manage media from multiple cameras or other synchronized footage.

The `multicam` element appears as a child element under a `media` element (as a resource reference). A `multicam` element contains one or more `mc-angle` elements that each manage a series of other story elements.

The code listing below shows a multicam definition with two angle definitions, `a1` and `a2`:

```swift
<resources>
   <media id="r1" name="MyMulticamClip">
      <multicam format="r2">
         <mc-angle name="MyMovie1" angleID="a1">
            <asset-clip name="MyMovie1" offset="0s" ref="r3" duration="10s" audioRole="dialogue" />
         </mc-angle>
         <mc-angle name="MyMovie2" angleID="a2">
            <asset-clip name="MyMovie2" offset="0s" ref="r4" duration="20s" audioRole="dialogue" />
         </mc-angle>
      </multicam>
   </media>
   <format id="r2" name="FFVideoFormat1080p30" />
   <asset id="r3" name="MyMovie1" src="file:///Volumes/Media/MyMovie1.mov" start="0s" duration="10s" hasVideo="1" format="r2" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000" />
   <asset id="r4" name="MyMovie2" src="file:///Volumes/Media/MyMovie2.mov" start="0s" duration="20s" hasVideo="1" format="r2" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000" />
</resources> 
```

> **Note**:  Starting in FCPXML 1.4, specify visual adjustments on a multicam clip on individual angles instead of the entire clip.

### Using Multicam Media

To use the multicam media as a clip, add an `mc-clip` element that references the media in the timeline.

Each `mc-clip` element can use audio and video from the same angle, or combine the audio and video from separate angles from the same `multicam` container. Use `mc-source` elements to specify the angle from which the audio, video, or both come from.

The `mc-source` element has the following attributes:

| Attribute | Description |
| --- | --- |
| `angleID` | Specifies the angle. |
| `srcEnable` | Indicates which source to use, if any, from the angle; use one of the following: `audio`, `video`, `all`, or `none`. |

The code listing below refers to the multicam media defined in the earlier code listing on this page.

```swift
<mc-clip ref="r4" name="MC Clip" duration="10s">
   <mc-source angleID="a1" srcEnable="all" />
</mc-clip>
```

> **Note**:   In FCPXML 1.1, you specified the angle using the `videoAngleID` and `audioAngleID` attributes of the `mc-clip` element. In FCPXML 1.2, you used the `mc-source` element’s `angleID` attribute.

## See Also

### Multicam Media
- [Audio Components and Multicam](./audio-components-and-multicam.md)
  Specify configuration of audio components using the `mc-clip` element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/multicam-media)*