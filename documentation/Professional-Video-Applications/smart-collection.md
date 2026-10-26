# smart-collection

**Framework**: Professional-Video-Applications  
**Role**: Article

Describe smart collection filters that group clips and projects that match the criteria.

#### Overview

A `smart-collection` element can have one or more smart collection match elements listed in the table below. Each of the smart collection match elements describes a smart collection filter that gathers items matching the criteria.

##### Smart Collection Match Elements

| Element | Description |
| --- | --- |
| `match-clip` | Match clips based on one of the following types:  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `audition` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `synchronized` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `compound`  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `multicam` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `layeredGraphic` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `project` |
| `match-keywords` | Match clips based on assigned keywords. |
| `match-markers` | Match clips based on one of the following marker types: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `all` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `standard` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `allTodo` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `complete` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `incomplete` |
| `match-media` | Match clips or projects based on one of the media types: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `audioOnly` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `stills` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `videoOnly` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `videoWithAudio` |
| `match-property` | Match clips based on the following property keys against property values: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |
| `reel` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `scene` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `take` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `audioOutputChannels` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `frameSize` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `videoFrameRate` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `audioSampleRate` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `cameraName` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `cameraAngle` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `projection` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `stereoscopic` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `cinematic` |  |
| ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For the projection and the stereoscopic property keys, the values can be: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `projection`: none, equirectangular, fisheye, back-to-back fisheye, or cubic ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `stereoscopic`: mono, side by side, or over under |  |
| `match-ratings` | Match clips based on assigned ratings. |
| `match-representation` | Match clips based on the availability of one of the following representation types: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `original` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `optimized` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `proxy` |
| `match-roles` | Match clips based on assigned roles. |
| `match-shot` | Match clips based on the assigned shot type |
| `match-stabilization` | Match clips based on the stabilization type. |
| `match-text` | Match clips or projects based on a specified text. The text search can be scoped to one of the following types: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `all` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `notes` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `name` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `markers` |
| `match-time` | Match clips or projects created or imported based on a specific date. |
| `match-timeRange` | Match clips or projects created or imported based on a range of time. |
| `match-usage` | Match clips based on whether they are used. |

##### Rule Attribute

Most smart collection match elements have a `rule` attribute to describe the criteria of the filter that the element describes.

For example, the following `match-clip` element defines a filter that gathers multicam clips:

```swift
<match-clip type="multicam" rule="is"/>
```

The following `match-property` element defines a filter that gathers clips with their camera name set:

```swift
<match-property type="cameraName" rule="isSet"/>
```

The possible values for the `rule` attribute are listed below. Depending on the smart collection match element, the possible values may be different. Consult the FCPXML Document Type Definition for the exact details.

| Attribute | Possible Values |
| --- | --- |
| `rule` | `includes` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `doesNotInclude` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |
| `includesAny` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `includesAll` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `doesNotIncludeAny` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `doesNotIncludeAll` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `is` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `isNot` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `isSet` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `isNotSet` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `isBefore` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `isAfter` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `isInLast` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `isNotInLast` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `used` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) |  |
| `unused` |  |

The following example shows three smart collections. The first one collects video clips, either video only or video and audio. The second one collects audio-only clips. The third one is for still-image clips.

```swift
<smart-collection name="Video" match="any">
    <match-media rule="is" type="videoOnly"/>
    <match-media rule="is" type="videoWithAudio"/>
</smart-collection>
<smart-collection name="Audio Only" match="all">
    <match-media rule="is" type="audioOnly"/>
</smart-collection>
<smart-collection name="Stills" match="all">
    <match-media rule="is" type="stills"/>
</smart-collection>
```

## See Also

### Clips and Project Collections
- [Describing Final Cut Pro Items in FCPXML](./describing-final-cut-pro-items-in-fcpxml.md)
  Describe clips, projects, and other items in FCPXML to exchange data with Final Cut Pro.
- [keyword-collection](./keyword-collection.md)
  Group clips and projects based on matching keywords.
- [collection-folder](./collection-folder.md)
  Contain keyword and smart collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/smart-collection)*