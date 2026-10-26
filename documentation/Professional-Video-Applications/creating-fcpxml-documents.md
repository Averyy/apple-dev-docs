# Creating FCPXML Documents

**Framework**: Professional-Video-Applications  
**Role**: Article

Describe media assets, editing decisions, metadata, and other items in FCPXML so users can send and receive data between your app and Final Cut Pro.

#### Overview

FCPXML describes Final Cut Pro items in a way your app understands. Your app uses FCPXML to send data to Final Cut Pro, and Final Cut Pro uses it to describe the data your app receives.

FCPXML describes data from your app in terms that correlate to Final Cut Pro objects — clips and project sequences, along with their media assets, often organized in events. FCPXML captures editing decisions, including the order of clips, as well as audio or video effects and transitions. It also captures metadata associated with the media assets, as well as ratings, keywords, and markers that Final Cut Pro uses to organize and annotate data. For more information on how you describe Final Cut Pro objects, see  [Describing Final Cut Pro Items in FCPXML](./describing-final-cut-pro-items-in-fcpxml.md).

An FCPXML document represents one of the following Final Cut Pro objects:

- A library
- One or more events
- One or more clips, which may have associated ratings or keywords; or projects, which may contain markers.

##### Prepare Media Assets

Final Cut Pro must have access to all media assets you reference in your FCPXML document. FCPXML describes media assets in terms of URLs that point to the location of the files that contain the media assets. The location can be on a local file volume or a shared network volume. Either way, the user must have read access to the media-asset files. Final Cut Pro can also import media from a remote location and download the media asset files, if the URLs contain proper authentication. For more information on how to describe a media file location, see [Location of Media Files](./media-rep.md#Location-of-Media-Files).

##### Structure Your FCPXML Document

The example FCPXML document below describes multiple media resources and an event that contains a project (with markers) and clips (with keywords).

```swift
<fcpxml version="1.10">

<!-- Resources -->
    <resources>
        <format id="r1" name="FFVideoFormat1080p30"/>
        <asset id="r2" start="0s" duration="10s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
            <media-rep kind="original-media" src="file:///Volumes/media/MyMovie1.mov"/>
        </asset>
        <asset id="r3" start="0s" duration="20s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
            <media-rep kind="original-media" src="file:///Volumes/media/MyMovie2.mov"/>
        </asset>
        <asset id="r4" start="10s" duration="40s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
            <media-rep kind="original-media" src="file:///Volumes/media/MyMovie3.mov"/>
        </asset>
    </resources>
    
<!-- Events -->
    <event name="MyBigEvent">
        <project name="MyProject">
            <!-- Project Story Elements -->
            <sequence format="r1">
                <spine>
                    <asset-clip name="MyMovie1" ref="r2" start="0s" duration="5s" audioRole="dialogue">
                        <marker start="2s" duration="1000/30000s" value="My Marker 1"/>
                    </asset-clip>
                    <asset-clip name="MyMovie3" ref="r4" offset="5s" start="15s" duration="5s" audioRole="dialogue"/>
                    <asset-clip name="MyMovie2" ref="r3" offset="15s" start="5s" duration="5s" audioRole="dialogue">
                        <marker start="6s" duration="1000/30000s" value="My Marker 2"/>
                    </asset-clip>
                </spine>
            </sequence>
        </project>

<!-- Clips -->
        <asset-clip name="MyMovie1" ref="r2" format="r1" start="0s" duration="10s" audioRole="dialogue">
            <keyword start="2s" duration="2s" value="Ocean"/>
        </asset-clip>
        <asset-clip name="MyMovie2" ref="r3" format="r1" start="0s" duration="20s" audioRole="dialogue"/>
        <asset-clip name="MyMovie3" ref="r4" format="r1" start="10s" duration="40s" audioRole="dialogue">
            <keyword start="24s" duration="8s" value="Ocean"/>
        </asset-clip>
        <keyword-collection name="Ocean"/>
    </event>

</fcpxml>
```

In an FCPXML document, one section describes the media assets and metadata you send to Final Cut Pro, and another section describes how to organize and use those media assets in an edited timeline. A valid FCPXML document must conform to the document type definition (DTD) and you must encode it in Unicode.

For information on examples of FCPXML documents, see [Describing Final Cut Pro Items in FCPXML](./describing-final-cut-pro-items-in-fcpxml.md).

## See Also

### Document Structure and Root Elements
- [FCPXML Bundle Reference](./fcpxml-bundle-reference.md)
  Keep an FCPXML document and any files it references together in a bundle.
- [Importing FCPXML Data](./importing-fcpxml-data.md)
  Import data from Final Cut Pro to your app by using FCPXML.
- [fcpxml](./fcpxml.md)
  Contain top-level elements in a document.
- [resources](./resources.md)
  Contain shared resources on which events and projects depend.
- [library](./library.md)
  Contain events, clips, projects, and smart collections.
- [event](./event.md)
  Represent a single event in a library.
- [project](./project.md)
  Represent a project timeline.
- [import-options](./import-options.md)
  Contain options that describe how to import events and projects into Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/creating-fcpxml-documents)*