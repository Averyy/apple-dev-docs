# Metadata Keys and Sources

**Framework**: Professional-Video-Applications  
**Role**: Article

Define metadata keys that identify each metadata item and its sources.

## Overview

The [Metadata Keys](./metadata-keys-and-sources.md#Metadata-Keys) section lists the metadata items that are editable through Final Cut Pro. The key string identifies each supported metadata item.

### Metadata Keys

| Key | Display Name | Type | Source |
| --- | --- | --- | --- |
| `com.apple.proapps.mio.cameraName` | Camera Name | String | Camera |
| `com.apple.proapps.studio.alphaHandling` | Alpha Handling | Integer | Studio |
| `com.apple.proapps.studio.angle` | Camera Angle | String | Studio |
| `com.apple.proapps.studio.metadataAnamorphicType` | Anamorphic Override | Integer | Studio |
| `com.apple.proapps.studio.metadataDeinterlaceType` | Deinterlace | Boolean | Studio |
| `com.apple.proapps.studio.metadataFieldDominanceOverride` | Field Dominance Override | Integer | Studio |
| `com.apple.proapps.studio.metadataLocation` | Location | String | Studio |
| `com.apple.proapps.studio.reel` | Reel | String | Studio |
| `com.apple.proapps.studio.scene` | Scene | String | Studio |
| `com.apple.proapps.studio.shot` | Take | String | Studio |

The supported values for Integer types are provided in the following table:

| Integer Type | Value | Description |
| --- | --- | --- |
| Alpha Handling | 0 | Premultiply |
|  | 1 | Straight |
|  | 2 | None/Ignore Alpha |
| Anamorphic Override | 0 | None Set |
|  | 1 | Standard |
|  | 2 | Widescreen |
| Field Dominance Override | 0 | None Set |
|  | 1 | Progressive |
|  | 2 | Upper First |
|  | 3 | Lower First |

### Metadata Sources

Final Cut Pro maintains metadata items by grouping them based on where they come from (their source). Indicate the source by using the `md` element’s source attribute, for example, `studio` or the prefix of the `key` attribute, for example, `com.apple.proapps.studio`.

The sources and key prefixes you can use are:

- **Camera**: Metadata from a camera or capturing device that Final Cut Pro or the device driver/plug-in picks up. These are not editable, except for com.apple.proapps.mio.cameraName.

*Key Prefixes:*

`com.apple.proapps.mio`

`org.smpte.mxf`

*Example:*

`com.apple.proapps.mio.cameraName`

- **Exif**: Metadata from files with Exif information, for example, a JPEG file.

*Key Prefix:*

`com.apple.proapps.exif.{Exif}`

*Example:*

`com.apple.proapps.exif.{Exif}.FocalLength`

- **Image**: Metadata from an image file, for example, TIFF or PNG, or camera-specific metadata saved with the image.

*Key Prefixes:*

`com.apple.proapps.image.{TIFF}`

`com.apple.proapps.image.{CIFF}`

`com.apple.proapps.image.{GIF}`

`com.apple.proapps.image.{PNG}`

`com.apple.proapps.image.{DNG}`

`com.apple.proapps.image.{GPS}`

`A prefix that identifies the camera manufacturer.`

*Examples:*

`com.apple.proapps.image.{TIFF}.WhitePoint`

`com.apple.proapps.image.{CIFF}.FocusMode`

`com.apple.proapps.image.{PNG}.Gamma`

`com.apple.proapps.image.{GPS}.MapDatum`

- **IPTC**: International Press Telecommunication Council defined photo metadata.

*Key Prefix:*

`com.apple.proapps.iptc.{IPTC}`

Example:

`com.apple.proapps.iptc.{IPTC}.Headline`

- **Share**: Metadata added to a share output.

*Key Prefix:*

`com.apple.proapps.share`

`com.apple.quicktime`

*Example:*

`com.apple.proapps.share.id`

`com.apple.quicktime.copyright`

- **Spotlight**: Spotlight metadata.

*Key Prefix:*

`com.apple.proapps.spotlight`

*Example:*

`com.apple.proapps.spotlight.kMDItemCopyright`

- **Studio**: Final Cut Pro-defined metadata. For more information on list of editable Studio keys, see [Metadata Keys](./metadata-keys-and-sources.md#Metadata-Keys).

Additional Studio keys exist that are not editable.

*Key Prefix:*

`com.apple.proapps.studio`

*Examples:*

`com.apple.proapps.studio.reel`

`com.apple.proapps.studio.scene`

- **Custom**: Metadata the user added in Final Cut Pro which has the prefix: com.apple.proapps.custom, or metadata that comes from a third-party application or camera, which has a prefix that’s a reverse DNS string that identifies a third-party application or a camera manufacturer.

*Key Prefixes:*

`com.apple.proapps.custom`

`A prefix that identifies a third-party application or a camera manufacturer.`

*Examples:*

`com.apple.proapps.custom.mycustommetadata`

`com.yourCompany.yourApp.yourCustomMetadata`

## See Also

### Media Metadata
- [Associating Ratings, Keywords, Markers, and Metadata with Media](./associating-ratings-keywords-markers-and-metadata-with-media.md)
  Organize and annotate the media and projects your users send to and receive from Final Cut Pro.
- [Metadata](./metadata.md)
  Describe metadata about media that is of interest to other applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/metadata-keys-and-sources)*