# Responding to Apple Events from Final Cut Pro

**Framework**: Professional-Video-Applications  
**Role**: Article

Tell Final Cut Pro about the kind of data your users want to receive in your app through a custom share destination.

## Overview

An Apple event is a type of interprocess message that can specify complex operations and data. Apple events provide a message transport through which an app can send a request to another app and receive an answer. (For more information about Apple events, see [`NSAppleEventManager`](../Foundation/nsappleeventmanager.md).)

> ❗ **Important**:  The information in this article applies only to situations in which your app is receiving projects or clips from Final Cut Pro through a custom share destination.

Your app must tell Final Cut Pro what kind of information your users want to receive and must provide a location for that data. Final Cut Pro uses the following Apple events (in the order shown) to get this information from your app.

1. `Create Asset`. Tells your app to identify a newly created asset object to serve as a placeholder. For more information, see [Respond to the Create Asset Apple Event](./responding-to-apple-events-from-final-cut-pro.md#Respond-to-the-Create-Asset-Apple-Event).
2. `Get Location Info Property`. Your app should return an asset location record that tells Final Cut Pro where to put the exported output files and indicate whether it wants to receive rendered media, project editing decisions (in FCPXML), or both. For more information, see [Respond to the Get Location Info Property Apple Event](./responding-to-apple-events-from-final-cut-pro.md#Respond-to-the-Get-Location-Info-Property-Apple-Event).
3. `Get Library Info Property`. Your app should return a library location record that tells Final Cut Pro where to put the library archive, if your user wants one. For more information, see [Respond to the Get Library Info Property Apple Event](./responding-to-apple-events-from-final-cut-pro.md#Respond-to-the-Get-Library-Info-Property-Apple-Event).
4. `Get Metadata Property`. Your app should return a user record containing the share metadata keys and values for the share metadata your users want to receive. For more information, see [Respond to the Get Metadata Property Apple Event](./responding-to-apple-events-from-final-cut-pro.md#Respond-to-the-Get-Metadata-Property-Apple-Event).
5. `Get Data Options Property` . Your app should return a user record with key-value pairs that specify the DTD version and the metadata view to use for the exported files. For more information, see [Respond to the Get Data Options Property Apple Event](./responding-to-apple-events-from-final-cut-pro.md#Respond-to-the-Get-Data-Options-Property-Apple-Event).
6. `Open Document`. When the export process is complete, Final Cut Pro sends an `Open Document` Apple event to notify your app that the export output files are available, and includes URLs to the files. For more information, see [Respond to the Open Document Apple Event](./responding-to-apple-events-from-final-cut-pro.md#Respond-to-the-Open-Document-Apple-Event).

> **Note**:  The synopsis for each Apple event is represented in AppleScript syntax; for more information, see the [AppleScript Language Guide](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html#//apple_ref/doc/uid/TP40000983). For more information about handling Apple events in your app, see the [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

When responding to Apple events, you should also know how to:

- Avoid conflicts with automated workflows by checking user interaction levels. See [Monitor User Interaction Levels When Using Apple Events](./responding-to-apple-events-from-final-cut-pro.md#Monitor-User-Interaction-Levels-When-Using-Apple-Events).
- Support conversions between the Apple event descriptor types used by Final Cut Pro and the respective Foundation object classes. See [Supporting Conversions with Scripting Class Extensions](./supporting-conversions-with-scripting-class-extensions.md).
- Use an AppleScript script to test your app and its ability to interact with Final Cut Pro. See [Test Your App with AppleScript](./responding-to-apple-events-from-final-cut-pro.md#Test-Your-App-with-AppleScript).

### Respond to the Create Asset Apple Event

When a Final Cut Pro user chooses File > Share and selects your app’s custom share destination, Final Cut Pro inspects your app’s `Info.plist` file to see if your app can respond to Apple events from Final Cut Pro. (See [Signal Your App’s Capabilities](./receiving-media-and-data-through-a-custom-share-destination.md#Signal-Your-Apps-Capabilities).) Once it confirms your app’s capability, Final Cut Pro sends your app a `Create Asset` Apple event containing the name of the asset, the set of share metadata, and a list of metadata views.

```swift
make new asset with properties { name: <asset name>, metadata: <metadata record>, data options: <options record> }
```

In response to a `Create Asset` event, your app should:

- Create a placeholder asset object with which to associate the exported data.
- Return an object specifier that identifies the newly created placeholder asset. Final Cut Pro uses the object specifier to reference this asset object in subsequent events.

The properties for the `Create Asset` Apple event include:

| Property | Description |
| --- | --- |
| `name` | The asset name. Final Cut Pro derives this information from the project name. |
| `metadata` | A record representing the set of share metadata, where the keys are reverse DNS-style metadata keys and the values are the associated metadata values. (For more information, see [Associating Ratings, Keywords, Markers, and Metadata with Media](./associating-ratings-keywords-markers-and-metadata-with-media.md).) |
| `data options` | A record containing the possible options for the exported output. This record holds the available choices for these `data options`: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `availableMetadataSets` (`list`): A list of available metadata views in Final Cut Pro. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `availableDescriptionVersions` (`list`): A list of available document type definition (DTD) versions that Final Cut Pro can export. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Your app indicates its choices in response to the `Get Data Options Property` Apple event (sent later) that asks for the value of the `data options` property. |

While handling the `Create Asset` event, your app can bring up its UI before Final Cut Pro starts a possibly time-consuming transcoding operation. Use this opportunity to request information relevant to the operation your app is about to perform, such as which custom metadata is stored along with the media or the location of the exported output.

To avoid initiating user interactions while your app is handling Apple events as part of an automated workflow, be sure to check the user interaction levels for incoming Apple events. See [Monitor User Interaction Levels When Using Apple Events](./responding-to-apple-events-from-final-cut-pro.md#Monitor-User-Interaction-Levels-When-Using-Apple-Events).

### Respond to the Get Location Info Property Apple Event

Final Cut Pro sends a `Get Location Info Property` Apple event to ask your app for the location of the exported output files.

```swift
get location info of <asset object specifier>
```

Your app should return an asset location record as described in [Creating Scripting Definitions for Custom Share Destinations](./creating-scripting-definitions-for-custom-share-destinations.md).

The record’s `folder` property specifies the location of the folder to contain the exported output files. The `base name` property provides the base name for the exported output files: Exported media files have an extension that reflects their file format, and exported FCPXML files have an `.fcpxml` extension.

If your user wants an FCPXML file, be sure to set the `has description` property in the asset location record to `true`. If your user wants a media file, set the `has media` property in the asset location record to `true`.

### Respond to the Get Library Info Property Apple Event

Final Cut Pro sends a `Get Library Info Property` event asking for the location of the library output files.

```swift
get library info of <asset object specifier>
```

Your app should return a library location record as described in [Creating Scripting Definitions for Custom Share Destinations](./creating-scripting-definitions-for-custom-share-destinations.md).

The record’s `library folder` property should specify the location of the folder for the exported library output files. The `library base name` property provides the base name for the exported library output files: The exported library archive file has an `.fcpbundle` extension, and the exported FCPXML file has an `.fcpxml` extension.

If your user wants library files, be sure to set the `has archive` and `has library description` properties to `true` in the library location record. If you don’t specify the `library folder` property, Final Cut Pro uses the asset location folder. If you don’t specify the `library base name` property, Final Cut Pro uses the asset name with a suffix to show that it is the FCPXML for the library, such as `MyProject-Library`. If your app doesn’t respond to this event, Final Cut Pro assumes your user doesn’t want library files.

### Respond to the Get Metadata Property Apple Event

Final Cut Pro sends a `Get Metadata Property` event to get an updated set of share metadata. Final Cut Pro supplied the original set of metadata through the `Create Asset` event.

```swift
get metadata of <asset object specifier>
```

Your app must return a user record containing the share metadata keys and their values. Final Cut Pro updates the project being shared and includes the returned share metadata in the exported output. If the user record that your app returns contains keys for metadata other than the share metadata, those keys are ignored. (For a list of share metadata keys, see [Review Share Metadata](./associating-ratings-keywords-markers-and-metadata-with-media.md#Review-Share-Metadata).)

Specifically, your app can generate a unique ID using the `com.apple.proapps.share.id` metadata key that represents the unique ID for the media asset your user is sharing (usually a project). Final Cut Pro includes the metadata for that key in the exported media files so your app can track the files associated with the asset.

### Respond to the Get Data Options Property Apple Event

Final Cut Pro sends a `Get Data Options Property` Apple event to request the data options to be used when it generates the exported output.

```swift
get data options of <asset object specifier>
```

Your app should return a user record with the following keys and their associated values:

| Key | Type | Description |
| --- | --- | --- |
| `descriptionVersion` | `text` | The DTD (document type definition) version to use for the FCPXML export. The default is the version used in the last FCPXML export. |
| `metadataSet` | `text` | The name of the metadata view containing the metadata item to be included in the project FCPXML. |

If no metadata view is specified, Final Cut Pro uses the currently selected metadata view to filter the share metadata. (For a list of keys for share metadata, see [Review Share Metadata](./associating-ratings-keywords-markers-and-metadata-with-media.md#Review-Share-Metadata).)

### Respond to the Open Document Apple Event

Once Final Cut Pro completes exporting the files your app requested, it sends an `Open Document` Apple event to notify your app that output files are available.

```swift
open <list of export output files>
```

The `Open Document` Apple event contains URLs to the exported output files. Your app should return the object specifier for the `asset` object and associate the files to the asset object it has created, matching the `base name` of the files with the asset’s location information.

Because Cocoa scripting handles the `Open Document` Apple event, your app doesn’t need a command-handler class specifically for the event. If your `asset` object class is a subclass of `NSDocument`, Cocoa scripting support instantiates the class according to standard conventions. Alternatively, you can intercept the request by implementing an appropriate `NSApplicationDelegate` method that is involved when Final Cut Pro asks your app to open the URLs.

In some cases, Final Cut Pro creates multiple media files (for example, when your custom share destination is configured to export each role as a separate file). In these cases, the export filename is the asset name returned as the `base name` property of the asset location record, followed by a hyphen (-) and a suffix that indicates the role of the data, such as dialogue or effect.

### Monitor User Interaction Levels When Using Apple Events

To avoid initiating user interactions while handling Apple events sent by an automated workflow, make sure your app checks the user interaction level of the Apple events *before* initiating your user interaction. In the scripting command handler for the `make` command (or the `Create Asset` Apple event), get the current Apple event and its `keyInteractLevelAttr` attribute to check the user interaction level.

The value of the `keyInteractLevelAttr` attribute can be one of the following:

```swift
kAENeverInteract    = 0x00000010, /* server should not interact with user */
kAECanInteract      = 0x00000020, /* server may try to interact with user */
kAEAlwaysInteract   = 0x00000030, /* server should always interact with user where appropriate */
kAECanSwitchLayer   = 0x00000040, /* interaction may switch layer */
```

See the [`NSAppleEventManager`](../Foundation/nsappleeventmanager.md) Class Reference for details on getting the current Apple event.

### Test Your App with AppleScript

Use the following AppleScript script to test your app’s ability to interact with Final Cut Pro.

```swift
tell application "SimpleAssetManager"
    make new asset with properties ¬
        {name:"MyNewAsset", metadata:{|com.apple.proapps.share.episodeID|:"MyNewEpisode"}, data options:{|availableMetadataSets|:{"Camera View", "General View"}}} ¬
 
    set newAsset to result
    set theLocation to location info of newAsset
    set theLibraryLocation to library info of newAsset
    set theMetadata to metadata of newAsset
    set theDataOptions to data options of newAsset
end tell

```

The following Apple event trace outlines the events and replies you get from running the previous AppleScript script:

```swift
tell application "SimpleAssetManager"
    make new asset with properties {name:"MyNewAsset", metadata:{|com.apple.proapps.share.episodeid|:"MyNewEpisode"}, data options:{availableMetadataSets:{"Camera View", "General View"}}}
        --> asset id "SSO-29842-2" of document "Untitled"
    get location info of asset id "SSO-29842-2" of document "Untitled"
        --> {has media:true, has description:true, base name:"MyNewAsset", folder:file "Lucca:Users:jane:Movies:"}
    get library info of asset id "SSO-29842-2" of document "Untitled"
        --> {has library description:true, has archive:true, library folder:file "Lucca:Users:jane:Movies:", library base name:"MyNewAssetLibrary"}
    get metadata of asset id "SSO-29842-2" of document "Untitled"
        --> {|com.apple.simpleassetmanager.preparedasset|:"1", |com.apple.simpleassetmanager.managedasset|:"1", |com.apple.quicktime.description|:"", |com.apple.simpleassetmanager.expeirationdate|:"2016-09-30 00:57:09 +0000", |com.apple.proapps.share.episodeid|:"MyNewEpisode", |com.apple.proapps.share.id|:"", |com.apple.proapps.share.episodenumber|:"0"}
    get data options of asset id "SSO-29842-2" of document "Untitled"
        --> {metadataSet:"None", descriptionVersion:"Previous Version"}
end tell
 
Result:
{metadataSet:"None", descriptionVersion:"Previous Version"}
```

## See Also

### Handling Apple Events
- [Supporting Conversions with Scripting Class Extensions](./supporting-conversions-with-scripting-class-extensions.md)
  Support conversions between the Apple event descriptor types and Foundation object classes.
- [Creating Scripting Definitions for Custom Share Destinations](./creating-scripting-definitions-for-custom-share-destinations.md)
  Define the record types, object classes, and event types that let your app interact with Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/responding-to-apple-events-from-final-cut-pro)*