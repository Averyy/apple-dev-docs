# Associating Ratings, Keywords, Markers, and Metadata with Media

**Framework**: Professional-Video-Applications  
**Role**: Article

Organize and annotate the media and projects your users send to and receive from Final Cut Pro.

#### Overview

Metadata, markers, and annotations, such as ratings and keywords, help your users sort, organize, and find their media. Include any of the following items in the FCPXML documents that your app sends to Final Cut Pro. If these items are in the FCPXML that your app receives from Final Cut Pro, you can use them to organize the incoming media.

| Metadata, Markers, and Annotations | Description |
| --- | --- |
| Common metadata | Information about the media that Final Cut Pro knows how to collect. Common metadata is typically ingested by Final Cut Pro from source media files. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For more information on including common metadata, see [Include Common Metadata](./associating-ratings-keywords-markers-and-metadata-with-media.md#Include-Common-Metadata). |
| Custom metadata | Information about the media that’s specific to your app’s workflow. Custom metadata is typically included in an FCPXML document sent to Final Cut Pro from your app.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For more information on adding custom metadata, see [Add Custom Metadata](./associating-ratings-keywords-markers-and-metadata-with-media.md#Add-Custom-Metadata). |
| Share metadata | Information, such as Copyright and Episode ID, that identifies media distributed to consumers.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For more information on share metadata, see [Review Share Metadata](./associating-ratings-keywords-markers-and-metadata-with-media.md#Review-Share-Metadata); also see [Change metadata for shared items in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/change-metadata-for-shared-items-ver8e9a81d37/10.4.7/mac/10.14). |
| Ratings | Sections of a clip that has ratings, such as accepted or rejected. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For more information on ratings, see [Add Ratings, Keywords, and Markers](./associating-ratings-keywords-markers-and-metadata-with-media.md#Add-Ratings-Keywords-and-Markers); also see [Rate clips in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/rate-clips-ver30ccd91f/mac) |
| Keywords | Labeled sections of a clip used to categorize clips into keyword collections. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For more information on adding keywords to clips, see [Add Ratings, Keywords, and Markers](./associating-ratings-keywords-markers-and-metadata-with-media.md#Add-Ratings-Keywords-and-Markers); also see [Add keywords to clips in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/add-keywords-ver68416335/mac). |
| Markers | Labeled locations that let video editors jump to a specific point in time in a project sequence. A marker has no duration.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For more information on adding markers, see [Add Ratings, Keywords, and Markers](./associating-ratings-keywords-markers-and-metadata-with-media.md#Add-Ratings-Keywords-and-Markers); also see [Intro to markers in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/intro-to-markers-ver397279dd/mac).) |

##### Include Common Metadata

*Common metadata* includes information about how a user created a piece of media, notes about the editing or production process, or additional information about the item’s origin. Final Cut Pro provides an extensive list of both basic and specialized metadata; users can review and modify items in that list using the Info inspector. For more information on viewing and editing common metadata, see [View and change clip metadata in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/view-and-change-clip-metadata-ver397298cc/mac).

> **Note**:  Common metadata is typically stored in the media file. To read and write common metadata in a QuickTime Movie file, use the AVFoundation APIs. For more information on AVFoundation APIs, see [AVFoundation Programming Guide](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188).

Final Cut Pro also provides *metadata views* to review and manage various groups of metadata. The currently selected metadata view determines which metadata Final Cut Pro includes in the FCPXML files that your app receives. For more information on using metadata views, see [Modify metadata views in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/modify-metadata-views-ver397297af/mac).

The following table shows a small subset of common metadata keys recognized by Final Cut Pro. To get the key for a particular metadata item, modify that item’s value in the Final Cut Pro Info inspector, select a metadata view that includes the item, and then, in Final Cut Pro, choose File > Export to XML. The metadata keys are identified in the resulting FCPXML document.

| Display Name | Key | Type |
| --- | --- | --- |
| Reel | `com.apple.proapps.reel` | String |
| Scene | `com.apple.proapps.scene` | String |
| Take | `com.apple.proapps.take` | String |
| Camera Angle | `com.apple.proapps.angle` | String |
| Date Imported | `com.apple.proapps.ingestDate` | Date |

> **Note**:  If the purpose of your app includes *writing* media files (for example, if your app is a recording app or a transcoding utility), then you may decide to include some of that metadata when your app writes the new media file—even though the metadata was read-only when the source file was consumed. When read-only metadata is included in the FCPXML, it doesn’t overwrite what’s already in the media file. However, where possible, your app should ingest the metadata directly from the media file.

##### Add Custom Metadata

While Final Cut Pro already recognizes a comprehensive set of metadata, there are times when a particular workflow requires custom metadata.

Attach custom metadata to media assets by adding metadata tags in the FCPXML file. The following example shows two pieces of custom metadata attached to a media asset. The second piece of metadata is read-only. For more information about defining custom metadata in FCPXML, see [Define and Register Custom Metadata Keys](./associating-ratings-keywords-markers-and-metadata-with-media.md#Define-and-Register-Custom-Metadata-Keys).

```swift
<asset id="r2" start="0s" duration="10s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
    <media-rep kind="original-media" src="file://Volumes/Media/Evening.mov"/>
    <metadata>
        <md key="com.myCompany.myApp.myCustomMetadata" value="This is my media" type="string" editable="1" displayName="My custom metadata" source="custom"/>
        <md key="com.myCompany.myApp.anotherCustomMetadata" value="Another piece of metadata that is read only" type="string" displayName="Another custom metadata" source="custom"/>
    </metadata>
</asset>
```

To make custom metadata visible and available to Final Cut Pro users, provide a property list file (a `.plist` file) with your app that specifies a definition and one or more metadata views for each piece of custom metadata. When Final Cut Pro users select the media or item annotated by the custom metadata, they see the custom metadata in the Info inspector window, and can manage it just as they do common metadata. For more information on managing custom metadata, see [View and change clip metadata in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/view-and-change-clip-metadata-ver397298cc/mac).

If you don’t include a metadata view in the `.plist` file, the custom metadata won’t be visible to users in Final Cut Pro until they add it manually to an existing or new metadata view. For more information about defining custom metadata in FCPXML, see [Define and Register Custom Metadata Keys](./associating-ratings-keywords-markers-and-metadata-with-media.md#Define-and-Register-Custom-Metadata-Keys).

> **Note**:  If the FCPXML document your app sends to Final Cut Pro includes custom metadata values, Final Cut Pro uses the values for any editable metadata items and ignores the values for any noneditable (read-only) metadata.

##### Review Share Metadata

When your app receives a project or clip as a rendered media file through a Final Cut Pro custom share destination, the file may include predetermined metadata keys called share metadata. *Share metadata* represents administrative information about a piece of media, such as its copyright information or an episode number, that helps identify media when it’s distributed to consumers. Final Cut Pro users decide which share metadata to include with the media, but the default items — Title, Description, Creator, and Tags — are included automatically.

> 💡 **Tip**:  Final Cut Pro users can review and manage the share metadata for a selected project in the Share inspector. For information on managing share metadata, see [Change metadata for shared items in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/change-metadata-for-shared-items-ver8e9a81d37/mac).

When your users share a project or a clip through a custom share destination, Final Cut Pro queries your app about which share metadata to include with the media. Your app returns a key-value pair for each piece of share metadata it includes in the FCPXML file. For more information, see [Provide Responses to Apple Events](./receiving-media-and-data-through-a-custom-share-destination.md#Provide-Responses-to-Apple-Events).

The following table shows the share metadata and keys that may be included with the movies or rendered media files your app receives from Final Cut Pro through a custom share destination:

| Display Name | Key | Type |
| --- | --- | --- |
| Actors | `com.apple.quicktime.artist` | String |
| Category | `com.apple.proapps.share.category` | String |
| Copyright | `com.apple.quicktime.copyright` | String |
| Creator | `com.apple.quicktime.author` | String ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) (Default share metadata key) |
| Date | `com.apple.quicktime.creationdate` | String |
| Description | `com.apple.quicktime.description` | String ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) (Default share metadata key) |
| Directors | `com.apple.quicktime.director` | String |
| Episode ID | `com.apple.proapps.share.episodeID` | String |
| Episode Number | `com.apple.proapps.share.episodeNumber` | String |
| Genre | `com.apple.quicktime.genre` | String |
| Media Kind | `com.apple.proapps.share.mediaKind` | String |
| Producers | `com.apple.quicktime.producer` | String |
| Screenwriters | `com.apple.proapps.share.screenWriter` | String |
| Season Number | `com.apple.proapps.share.seasonNumber` | String |
| Share ID | `com.apple.proapps.share.id` | String |
| Show | `com.apple.quicktime.album` | String |
| Tags | `com.apple.quicktime.keywords` | String ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) (Default share metadata key) |
| Title | `com.apple.quicktime.title` | String ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) (Default share metadata key) |
| TV Network | `com.apple.proapps.share.tvNetwork` | String |
| US Rating | `com.apple.quicktime.rating.user` | String |

##### Add Ratings, Keywords, and Markers

Final Cut Pro ratings, keywords, and markers, along with keyword collections_,_ help users annotate, sort, and organize their media. Your app can make use of this information when Final Cut Pro includes it in the FCPXML your app receives. (For more information about using ratings, keywords, and markers, see [Rate Clips in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/rate-clips-ver30ccd91f/mac), [Add keywords to clips in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/add-keywords-ver68416335/mac), and [Intro to markers in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/intro-to-markers-ver397279dd/mac). For information about sample FCPXML code, see [Describing Final Cut Pro Items in FCPXML](./describing-final-cut-pro-items-in-fcpxml.md).)

The code example below attaches rating to a clip and includes a value of either `favorite` or `reject`, along with the starting point and the duration of the rating.

```swift
<asset-clip name="Morning" ref="r5" format="r1" duration="5s" audioRole="dialogue">
     <rating start="2s" duration="1s" value="favorite"/>
     <rating start="4s" duration="1s" value="reject"/>
</asset-clip>
```

Users can group and sort clips into keyword collections with user-defined keywords. The next code listing attaches a keyword to a clip and has the keyword itself, along with its starting point and duration.

```swift
<asset-clip name="Morning" ref="r5" format="r1" duration="5s" audioRole="dialogue">
     <keyword start="2s" duration="2s" value="Ocean"/>
</asset-clip>
```

In a project, markers represent a point in time with no duration. In FCPXML, markers have a duration equal to a single video frame in the format used by the clip.

```swift
<asset-clip name="MyMovie1" ref="r2" start="0s"  duration="5s" audioRole="dialogue">
     <marker start="3s" duration="1000/30000s" value="MyMarker1"/>
</asset-clip>
<asset-clip name="MyMovie2" ref="r3" offset="5s" start="5s" duration="5s" audioRole="dialogue">
     <marker start="6s" duration="1000/30000s" value="MyToDo1" completed="0"/>
     <marker start="8s" duration="1000/30000s" value="MyToDo2" completed="1"/>
</asset-clip>
<asset-clip name="MyMovie3" ref="r4" offset="10s" start="15s" duration="5s" audioRole="dialogue">
     <chapter-marker start="18s" duration="1000/30000s" value="Chapter 2" posterOffset="19s"/>
</asset-clip>
```

##### Define and Register Custom Metadata Keys

If the FCPXML document your app is sending to Final Cut Pro contains custom metadata and you want that metadata to be visible and available to users in Final Cut Pro, create a `.plist` file to define the custom metadata keys and the metadata views to display them in the Final Cut Pro Info inspector window.

When Final Cut Pro launches, it reads the `.plist` file and creates and populates the custom metadata view. Your users can then review the metadata in the Final Cut Pro Info inspector window, and modify and rearrange it just as they would with common metadata. For more information on modifying metadata view, see [Modify metadata views in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/modify-metadata-views-ver397297af/mac). Without this `.plist` file, users won’t be able to see custom metadata in Final Cut Pro unless they add it manually to a metadata view.

To add definitions for custom metadata keys and the associated metadata views, use any text editor to create a `.plist` file. One `.plist` file can contain information for both the metadata definitions and metadata views. Distribute the `.plist` file along with your app and have your users install it in one of the following locations so Final Cut Pro can find it:

- `/Library/Application Support/ProApps/Metadata Definitions/`
- `~/Library/Application Support/ProApps/Metadata Definitions/`

The `.plist` file has two components: *custom metadata definitions* and *metadata view definitions*. The custom metadata definitions make up a dictionary that’s identified by the `com.apple.proapps.MetadataDefinitions` key under the root level dictionary in the `.plist` file. The metadata view definitions make up an array that’s identified by the `com.apple.proapps.MetadataViewSets` key under the root level dictionary in the `.plist` file.

Each entry in the custom metadata definitions dictionary defines one piece of custom metadata. Each entry is also a dictionary and is associated with a metadata key, for example, `com.yourCompany.yourApp.yourCustomMetadata`.

The following table shows the structure of the dictionary that defines one piece of custom metadata:

| Name | Type | Description |
| --- | --- | --- |
| `displayName` | `String` | The name to display in the `Name` field of the Final Cut Pro inspector. |
| `displayDescription` | `String` | The description to display in the `Description` field of the Final Cut Pro Metadata View Set editor. |
| `type` | `String` | The data type of this metadata; for example, `string`, `boolean`, `integer`, `float`. These are the same data types used in FCPXML. |
| `source` | `String` | The source of the metadata to display in the `Origin` field of the Final Cut Pro Metadata View Set editor; for example, `‘EXIF’`, `‘Apple’`, `‘BBC’`, `‘<your company name>’`. |
| `editable` | `Boolean` | Whether the user can modify this metadata. |

Each element in the metadata view definitions array defines one metadata view and is a dictionary. The following table shows the structure of the dictionary that defines one metadata view:

| Name | Type | Description |
| --- | --- | --- |
| `displayName` | `String` | The name to display in the `Name` field of the Final Cut Pro Metadata View Set editor. |
| `displayDescription` | `String` | The description to  display in the `Description` field of the Final Cut Pro Metadata View Set editor. |
| `keys` | `String` `Array` | An array of metadata identifiers, in reverse DNS style. |

The following code shows an example `.plist` file with a custom metadata key definition and a definition for a custom metadata view.

```swift
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>com.apple.proapps.MetadataDefinitions</key>
        <dict>
            <key>com.myCompany.myApp.myCustomMetadata</key>
            <dict>
                <key>displayDescription</key>
                <string>Description of my custom metadata</string>
                <key>displayName</key>
                <string>My custom metadata</string>
                <key>source</key>
                <string>custom</string>
                <key>type</key>
                <string>string</string>
                <key>editable</key>
                <true/>
            </dict>
            <key>com.myCompany.myApp.anotherCustomMetadata</key>
            <dict>
                <key>displayDescription</key>
                <string>Description of another custom metadata</string>
                <key>displayName</key>
                <string>Another custom metadata</string>
                <key>source</key>
                <string>custom</string>
                <key>type</key>
                <string>string</string>
            </dict>
        </dict>
        <key>com.apple.proapps.MetadataViewSets</key>
        <array>
            <dict>
                <key>displayName</key>
                <string>My Application&apos;s Set</string>
                <key>keys</key>
                <array>
                    <string>com.myCompany.myApp.myCustomMetadata</string>
                    <string>com.myCompany.myApp.anotherCustomMetadata</string>
                </array>
            </dict>
        </array>
    </dict>
</plist>


```

## See Also

### Media Metadata
- [Metadata](./metadata.md)
  Describe metadata about media that is of interest to other applications.
- [Metadata Keys and Sources](./metadata-keys-and-sources.md)
  Define metadata keys that identify each metadata item and its sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/associating-ratings-keywords-markers-and-metadata-with-media)*