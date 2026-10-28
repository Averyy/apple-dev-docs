# Describing Final Cut Pro Items in FCPXML

**Framework**: Professional-Video-Applications  
**Role**: Article

Describe clips, projects, and other items in FCPXML to exchange data with Final Cut Pro.

## Overview

Your app uses FCPXML to describe media, projects, and other information when it sends data to or receives data from Final Cut Pro. Whether the FCPXML is created by your app for Final Cut Pro or by Final Cut Pro for your app, the descriptions in FCPXML are essentially the same.

The following examples show two FCPXML documents that describe media assets and Final Cut Pro objects. An explanation of what Final Cut Pro does when it receives the document follows each example. These examples, along with the tips in the following section, help you understand what your app needs to do when it receives FCPXML documents from Final Cut Pro.

> **Note**:  FCPXML describes various aspects of a Final Cut Pro library and the items it contains in a way that is useful to other apps. FCPXML doesn’t describe all possible data, and it’s not a substitute for the native Final Cut Pro project and event data organized in a library bundle.

- For more information on resources that represents media assets, possibly with custom metadata, see  [Describe Ratings, Keywords, Collections, and Custom Metadata](./describing-final-cut-pro-items-in-fcpxml.md#Describe-Ratings-Keywords-Collections-and-Custom-Metadata).
- For more information on Final Cut Pro clips that contain ratings and keywords, see [Describe Ratings, Keywords, Collections, and Custom Metadata](./describing-final-cut-pro-items-in-fcpxml.md#Describe-Ratings-Keywords-Collections-and-Custom-Metadata).
- For more information on Final Cut Pro projects that each represent a sequence of clips, possibly with project markers, see [Describe a Project, Markers, and Assets](./describing-final-cut-pro-items-in-fcpxml.md#Describe-a-Project-Markers-and-Assets).
- For more information on Final Cut Pro events that contain clips and projects, possibly with keyword collections or smart collections. see [Describe Ratings, Keywords, Collections, and Custom Metadata](./describing-final-cut-pro-items-in-fcpxml.md#Describe-Ratings-Keywords-Collections-and-Custom-Metadata).

### Receive FCPXML in Your App

The purpose and goals of your app determine how it uses data from Final Cut Pro. Use these tips to get the most from the FCPXML documents that your app receives.

- Organize the clips in a way that makes sense for your app and your users. For example, put clips in folders that correspond to Final Cut Pro events or based on when you created the clips; use metadata to sort clips into folders by scene, take, camera name, and so on; group projects, clips, and related resources into a single folder.
- Preserve the editing decisions in a project, along with any project markers. Use that information to identify which special effects you used on which clips, to track assets for rights management, and so on.
- To preserve how your users have organized their data in Final Cut Pro, use the keywords and ratings that they associated with clips to categorize data in your app. Consider creating equivalents for keyword collections and smart collections.

### Describe a Project, Markers, and Assets

The following example FCPXML document describes a project with three different clips in its timeline sequence. One of the clips, `MyMovie1`, appears three times. The order of the clips in the project `spine` determines their order in the project. The document also describes the three media assets used in the project, along with URLs to the location of the files on a local file system. The example includes the three clips again at the end of the document, so they can appear in the Final Cut Pro browser in addition to the project to use in further editing. The explanation following this example describes how Final Cut Pro interprets this FCPXML.

```swift
<fcpxml version="1.10">
    <import-options>
        <option key="library location" value="file:///Volumes/FCPXLibraries/MyLibrary.fcpbundle"/>
    </import-options>
    <!-- Resources -->
    <resources>
        <format id="r1" name="FFVideoFormat1080p30"/>
        <asset id="r2" start="0s" duration="10s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
            <media-rep kind="original-media" src="file:///Volumes/Media/MyMovie1.mov"/>
        </asset>
        <asset id="r3" start="0s" duration="20s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
            <media-rep kind="original-media" src="file:///Volumes/Media/MyMovie2.mov"/>
        </asset>
        <asset id="r4" start="10s" duration="40s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
            <media-rep kind="original-media"  src="file:///Volumes/Media/MyMovie3.mov"/>
        </asset>
    </resources>
    <project name="MyProjectWithMarkers">
        <!-- Project Story Elements -->
        <sequence format="r1">
            <spine>
                <asset-clip name="MyMovie1" ref="r2" start="0s" duration="5s" audioRole="dialogue">
                    <marker start="2s" duration="1000/30000s" value="My Marker 1"/>
                </asset-clip>
                <asset-clip name="MyMovie3" ref="r4" offset="5s" start="15s" duration="5s" audioRole="dialogue">
                    <chapter-marker start="18s" duration="1000/30000s" value="Chapter 2" posterOffset="19s"/>
                </asset-clip>
                <asset-clip name="MyMovie1" ref="r2" offset="10s" start="5s" duration="5s" audioRole="dialogue">
                    <marker start="8s" duration="1000/30000s" value="My Marker 2"/>
                </asset-clip>
                <asset-clip name="MyMovie2" ref="r3" offset="15s" start="5s" duration="5s" audioRole="dialogue">
                    <marker start="6s" duration="1000/30000s" value="My To Do 1" completed="0"/>
                    <marker start="8s" duration="1000/30000s" value="My To Do 2" completed="1"/>
                </asset-clip>
                <asset-clip name="MyMovie1" ref="r2" offset="20s" start="0s" duration="5s" audioRole="dialogue">
                    <marker start="4s" duration="1000/30000s" value="My Marker 3"/>
                </asset-clip>
            </spine>
        </sequence>
    </project>
    <!-- Clips -->
    <asset-clip name="MyMovie1" ref="r2" format="r1" start="0s" duration="10s" audioRole="dialogue"/>
    <asset-clip name="MyMovie2" ref="r3" format="r1" start="0s" duration="20s" audioRole="dialogue"/>
    <asset-clip name="MyMovie3" ref="r4" format="r1" start="10s" duration="40s" audioRole="dialogue"/>
</fcpxml>
```

This example tells Final Cut Pro to:

- Create a new event in the library specified by the import option: `file://Volumes/FCPXLibraries/MyLibrary.fcpbundle`. Name the new event with today’s date, as in 11`-14-20`. (If an event with that name already exists, add a numeric suffix to the event name to create a unique name, as in 11`-14-20 1`).
- Import and copy (or link to) the media files (`MyMovie1.mov`, `MyMovie2.mov`, and `MyMovie3.mov`) on the local file system at `/Volumes/Media/`. Users set the preference for copying or linking files in the Import pane of the Final Cut Pro Preferences window. For more information on prefrences for importing media, see [Import preferences](https://support.apple.com/guide/final-cut-pro/import-preferences-verb8e6085b/10.4.7/mac/10.14) in Final Cut Pro User Guide.
- For each media asset, create a clip, for example, `MyMovie1`, `MyMovie2`, and `MyMovie3` in the new event using the first video format (`FFVideoFormat1080p30`) specified in the FCPXML document. If a clip with the same name already exists in the event, ask the user whether to replace the existing clip or keep both clips. If the user decides to keep both, add a numerical suffix to keep the names unique, as in `MyMovie1 1`. The choice your user makes — to replace an item or to keep both — applies to all naming conflicts involving clips and projects during that same operation.
- Create a project called `MyProjectWithMarkers` that contains five clips in this order: the first 5 seconds of `MyMovie1`; starting 15 seconds in, the next 5 seconds of `MyMovie3`; the last 5 seconds of `MyMovie1`; the last 5 seconds of `MyMovie2`; and the first 5 seconds of `MyMovie1` again. (If a project with the same name already exists, ask the user whether to replace the existing project or keep both. If the user decides to keep both, add a numerical suffix, as in `MyProjectWithMarkers` `1`.)
- In `MyProjectWithMarkers`, add a marker (`MyMarker1`) to the first clip (`MyMovie1`) at 2 seconds into the clip. Add a chapter marker (`Chapter` `2`) at 3 seconds into `MyMovie3`. Add another marker (`MyMarker2`) to the third clip (`MyMovie1`) at 3 seconds into the clip. Add two “to do” markers (`MyToDo1` and `MyToDo2`) at 1 second and 3 seconds into `MyMovie2`; notice that `MyToDo2` is marked as complete. Add yet another marker (`MyMarker3`) to the last clip (`MyMovie1`) at 4 seconds into the clip.

> 💡 **Tip**:  You can choose to make the clips used in a project available to users for future editing. In addition to describing clips in the project timeline, add them to the FCPXML document at the same level as the project, as shown in the previous example. When Final Cut Pro processes the document, your users see the clips in the project as well as in the Final Cut Pro browser (inside an event named with today’s date).

### Describe Ratings, Keywords, Collections, and Custom Metadata

The following example FCPXML document describes two clips for the media assets (`Evening.mov` and `Morning.mov).` The clips (`Evening` and `Morning`) are organized into an event named `MyBigEvent`. The `Evening` clip contains a keyword (`Ocean`) and the `Morning` clip contains two Final Cut Pro ratings. The document also describes the media assets used in the event, along with URLs to the location of the files; the `Evening.mov` asset contains two pieces of custom metadata. The explanation following this example describes how Final Cut Pro interprets this FCPXML.

```swift
<fcpxml version="1.10">
    <!-- Resources -->
    <resources>
        <format id="r1" name="FFVideoFormat1080p30"/>
        <asset id="r2" start="0s" duration="10s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
            <media-rep kind="original-media" src="file:///Volumes/Media/Evening.mov"/>
            <metadata>
                <md key="com.myCompany.myApp.myCustomMetadata" value="This media belongs to me." type="string" editable="1" displayName="My custom metadata" source="custom"/>
                <md key="com.myCompany.myApp.anotherCustomMetadata" value="Another piece of metadata that is read only." type="string" displayName="Another custom metadata" source="custom"/>
            </metadata>
        </asset>
        <asset id="r3" start="0s" duration="10s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000">
            <media-rep kind="original-media" src="file:///Volumes/Media/Morning.mov"/>
        </asset>
    </resources>
    <!-- Events -->
    <event name="MyBigEvent">
        <!-- Clips -->
        <asset-clip name="Evening" ref="r2" format="r1" start="0s" duration="10s" audioRole="dialogue">
            <keyword start="2s" duration="2s" value="Ocean"/>
        </asset-clip>
        <asset-clip name="Morning" ref="r3" format="r1" start="0s" duration="10s" audioRole="dialogue">
            <rating start="2s" duration="1s" value="favorite"/>
            <rating start="4s" duration="1s" value="reject"/>
        </asset-clip>
        <keyword-collection name="Ocean"/>
    </event>
</fcpxml>
```

This example tells Final Cut Pro to:

- Import and copy (or link to) two media assets (`Evening.mov` and `Morning.mov`).
- Attach two pieces of custom metadata to the `Evening.mov` asset: The first piece of metadata (`MyCustomMetadata`) is editable and has the value “`This media belongs to me.`” The second piece of custom metadata is read-only (not editable), so Final Cut Pro ignores its value. Note that to make custom metadata visible to your users in Final Cut Pro, you must provide a definition of the custom metadata and a metadata view in your app’s `.plist` bundle. For more information on providing custom metadata and metadata view, see [Add Custom Metadata](./associating-ratings-keywords-markers-and-metadata-with-media.md#Add-Custom-Metadata).
- Create a clip for each of the media assets imported (`Evening` and `Morning`) and put them in the event called `MyBigEvent`. (If an event named `MyBigEvent` doesn’t exist, create it and put the clips in it. Events must contain at least one clip or project; they cannot be empty.)
- Add a keyword (`Ocean`) to the `Evening` clip starting 2 seconds into the clip and lasting 1 second.
- Add a Favorite rating for a duration of 1-second to the the `Morning` clip at 2 seconds into the clip, and add a `Reject` rating for a duratiom of 1-second at 4 seconds in.
- Create a keyword collection called `Ocean` to organize clips that contain the `Ocean` keyword.

## See Also

### Clips and Project Collections
- [keyword-collection](./keyword-collection.md)
  Group clips and projects based on matching keywords.
- [smart-collection](./smart-collection.md)
  Describe smart collection filters that group clips and projects that match the criteria.
- [collection-folder](./collection-folder.md)
  Contain keyword and smart collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/describing-final-cut-pro-items-in-fcpxml)*