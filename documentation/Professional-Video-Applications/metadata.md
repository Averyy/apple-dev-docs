# Metadata

**Framework**: Professional-Video-Applications  
**Role**: Article

Describe metadata about media that is of interest to other applications.

#### Overview

Final Cut Pro maintains various metadata item values, such as camera name, reel, copyright. Metadata typically comes from the media and may be of interest to other applications, but is not critical for Final Cut Pro to perform its tasks.

On export, Final Cut Pro includes only the metadata items in the user-selected metadata view. On import, Final Cut Pro uses the user-specified values in the FCPXML for editable metadata items; it ignores the values for non-editable metadata items during import and instead retrieves from the media asset.

Use the metadata elements listed below to describe metadata about a media.

| Metadata Elements | Description |
| --- | --- |
| `metadata` | Contains a collection of `md` elements. |
| `md` | Specifies an individual metadata item. |
| `array` | Contains a collection of `string` elements that define the value(s) for an array of strings. |
| `string` | Defines one metadata value in an array of strings. |

##### md Element Attributes

| Attribute | Description |
| --- | --- |
| `key` | A structured Final Cut Pro key string that identifies the metadata item, for example, `com.apple.proapps.mio.cameraName`. |
| `value` | The value of the metadata item. When the value is an array, specify an `array` element. |
| `editable` | Indicates whether the metadata item is editable (1=Yes, 0=No). The default is 0.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Most metadata items are not editable, and you may omit this attribute. If editable, Final Cut Pro applies the new value for the metadata item on import. |
| `type` | Defines the metadata item value type. |
| `displayName` | The metadata item name that appears in Final Cut Pro. |
| `description` | The metadata item description that appears in Final Cut Pro. |
| `source` | The metadata item origin. |

The following code listing is an example of metadata with primitive data types:

```swift
<metadata>
    <md key="com.apple.proapps.mio.cameraName" value="The Big Camera"/>
    <md key="com.apple.proapps.spotlight.kMDItemCopyright"
            value="© 2009 All Rights Reserved"/>
    <md key="com.apple.proapps.studio.reel" value="R945"/>
    <md key="com.apple.proapps.studio.scene" value="Deep Water"/>
</metadata>
```

The following code listing is an example of metadata with complex data types:

```swift
<metadata>
    <md key="com.apple.proapps.spotlight.kMDItemCodecs" displayName="Codecs">
        <array>
            <string>AAC</string>
            <string>H.264</string>
        </array>
    </md>
</metadata>
```

## See Also

### Media Metadata
- [Associating Ratings, Keywords, Markers, and Metadata with Media](./associating-ratings-keywords-markers-and-metadata-with-media.md)
  Organize and annotate the media and projects your users send to and receive from Final Cut Pro.
- [Metadata Keys and Sources](./metadata-keys-and-sources.md)
  Define metadata keys that identify each metadata item and its sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/metadata)*