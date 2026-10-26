# Receiving Media and Data Through a Custom Share Destination

**Framework**: Professional-Video-Applications  
**Role**: Article

Receive rendered media (movies), editing descriptions for project timelines, library archives, and FCPXML for other Final Cut Pro items in your app.

#### Overview

After your users have finished working on their project in Final Cut Pro, they’re ready to bring it over to your app for final processing. Maybe your users plan to upload their project to an asset management server, or perhaps they need to archive or catalog the entire Final Cut Pro library.

With a Final Cut Pro *custom share destination* (and support from your app), your users can receive rendered output from a Final Cut Pro project, along with FCPXML descriptions for the project’s editing decisions and other items, such as keywords, ratings, and markers. Your app can also request a copy of the library containing these items to use for archiving.

![Illustration showing a Final Cut Pro custom share destination sending both FCPXML and QuickTime Movies to your app.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3878516@2x.png)

In Final Cut Pro, a *share destination* provides a set of preconfigured export settings. When a user shares one or more projects or clips, these settings determine the format and other characteristics of the exported media. A *custom share destination* serves a similar purpose, but it specifies an app that knows how to interact with Final Cut Pro as the *target application* in the Final Cut Pro export settings.

Once you set up a custom share destination for your users, they see the custom share destination you created as one of the choices for sharing a project in Final Cut Pro.

![Screenshot showing File > Share menus with the custom share destination called MyAppCustomDestination selected.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3234183.png)

Setting up your app is the first step in providing a custom share destination for your users. Edit your app’s `Info.plist` file to indicate that your app is capable of interacting with Final Cut Pro to configure the share operation (see [Signal Your App’s Capabilities](./receiving-media-and-data-through-a-custom-share-destination.md#Signal-Your-Apps-Capabilities)). Supply the scripting definitions required by Final Cut Pro to interact with your app through Apple events (see [Describe Your Scripting Terminology](./receiving-media-and-data-through-a-custom-share-destination.md#Describe-Your-Scripting-Terminology)) and add support so your app can respond to the series of Apple events sent by Final Cut Pro (see [Provide Responses to Apple Events](./receiving-media-and-data-through-a-custom-share-destination.md#Provide-Responses-to-Apple-Events)).

Once you’ve configured your app, create a custom share destination in Final Cut Pro. This is the destination that lets your users share their projects with your app (see [Create a Custom Share Destination in Final Cut Pro](./receiving-media-and-data-through-a-custom-share-destination.md#Create-a-Custom-Share-Destination-in-Final-Cut-Pro)). You distribute this custom share destination along with your app so users can add it to their own Final Cut Pro installation (see [Distribute a Custom Share Destination to Your Users](./receiving-media-and-data-through-a-custom-share-destination.md#Distribute-a-Custom-Share-Destination-to-Your-Users)).

When your users have finished editing their projects in Final Cut Pro and want to continue their work in your app, they just select the project in Final Cut Pro, choose File > Share, and select your app’s custom share destination from the list of destinations. (See [Intro to sharing projects in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/intro-to-sharing-projects-ver9d10063a/mac) for more information.) Final Cut Pro conveys the request to your app, and your app responds with the information Final Cut Pro needs to perform the export operation.

> 💡 **Tip**:  When you create the custom share destination for your app in Final Cut Pro, use that opportunity to test the communications between Final Cut Pro and your app. As your own first user, you can identify and fix any bugs before you distribute the custom share destination file to your users.

##### Signal Your App’s Capabilities

Your app must advertise its ability to interact with Final Cut Pro and provide the information necessary for sharing a project. Add the following entry to the `Info.plist` file in your app’s bundle:

```swift
<key>com.apple.proapps.MediaAssetProtocol</key>
<dict>
</dict>
```

The value for this entry is an empty dictionary; the content is reserved for future use by Final Cut Pro.

##### Describe Your Scripting Terminology

Your app must supply scripting definitions for the events, object classes, and associated properties that Final Cut Pro uses to interact with your app. Specifically, your app must:

- Create scripting definitions for events, object classes, and record types. This includes definitions for the `asset` class as a representation of the media in your app. It also includes the `make` event that Final Cut Pro sends to tell your app to create an `asset` object as a placeholder. (See [Creating Scripting Definitions for Custom Share Destinations](./creating-scripting-definitions-for-custom-share-destinations.md) for the scripting definitions you need to provide.)
- Implement the command-handler classes that are referenced from the scripting definitions. Specifically, implement the command handler for the `make` event using the Cocoa class name specified in your scripting definition. (See [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164) for more information.)
- Implement the object classes and associated properties according to key-value coding (KVC) and other conventions. Specifically, implement the object class for the `asset` object class, using the Cocoa class name specified in the scripting definition. (See [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164) for details.) Cocoa Scripting support gets the properties’ values when Final Cut Pro asks for those properties through `Get` `Property` `Apple` events.

##### Provide Responses to Apple Events

Once Final Cut Pro confirms that your app can interact with it through Apple events, it sends your app a series of Apple events. Your app responds by telling Final Cut Pro what kind of data your users want to receive and by providing a location for the data. Specifically, Final Cut Pro uses Apple events to find out:

- Whether your user wants to receive rendered media, editing decisions in FCPXML, or both
- Whether your user wants a library archive
- Which share metadata keys and values your user wants in the exported media files
- Which DTD version to use for the exported media files
- What Final Cut Pro metadata view to use to filter the metadata keys included in the exported media files

For information about responding to each of these Apple events, see [Responding to Apple Events from Final Cut Pro](./responding-to-apple-events-from-final-cut-pro.md).

##### Create a Custom Share Destination in Final Cut Pro

Once your app is set up to interact with Final Cut Pro, it’s time to create the actual share destination that your users will select in Final Cut Pro. (For more information, see [Create share destinations in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/create-share-destinations-ver9fd008a21/mac).)

1. Create a new custom share destination. In Final Cut Pro, choose File > Share > Add Destination. Drag the Export File destination from the right side of the Destinations list to the left side.
2. Give the new destination a name and specify the format and other settings. Choose the format your app requires and then specify the related settings, such as Video codec and Resolution. (For details about each option, see [Export File destination in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/export-file-destination-ver13664388c/10.4.7/mac/10.14).)
3. Designate your app as the target application. From the “Open with” pop-up menu, choose Other. In the Applications folder, select your app and click Open.

![Screenshot of the Destinations pane in Final Cut Pro Preferences. In the Destinations list on the left, MyAppCustomDestination is selected as the custom share destination for your app. The “Open with” field on the right shows MyApp as the target application. ](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3234547.png)

##### Distribute a Custom Share Destination to Your Users

Your users need the custom share destination you created for your app installed on their own systems so that it’s available in the list of share destinations in Final Cut Pro. (See [Create share destinations in Final Cut Pro: Share destinations between Final Cut Pro users](https://support.apple.com/guide/final-cut-pro/create-share-destinations-ver9fd008a21/10.4.7/mac/10.14) for more information.)

1. Select your custom share destination. In Final Cut Pro, choose Final Cut Pro > Preferences, select the Destinations pane, and then select the custom share destination for your app.
2. Drag your custom share destination to a location in the Finder. Final Cut Pro creates an `.fcpxdest` file for your custom share destination in that location.

When you’re ready to deliver the `.fcpxdest` file to your users (perhaps along with your app), instruct them to install the `.fcpxdest` file in Final Cut Pro in any of these ways:

- Double-click the `.fcpxdest` file in the Finder.
- Drag the `.fcpxdest` file to the Destinations pane in Final Cut Pro > Preferences.
- Place the `.fcpxdest` file in either of the following locations:

`/Library/Application Support/ProApps/Share Destinations/ ~/Library/Application Support/ProApps/Share Destinations/`

> 💡 **Tip**: You can use the `Open` `Document` Apple event to send your `.fcpxdest` file programmatically and have Final Cut Pro open it. Final Cut Pro will then install your custom share destination, making it available to your users. Use the steps in [Send an FCPXML File Using an Apple Event](./sending-data-programmatically-to-final-cut-pro.md#Send-an-FCPXML-File-Using-an-Apple-Event), but substitute `.fcpxdest` file for the `.fcpxml` file.

## Topics

### Handling Apple Events
- [Responding to Apple Events from Final Cut Pro](./responding-to-apple-events-from-final-cut-pro.md)
  Tell Final Cut Pro about the kind of data your users want to receive in your app through a custom share destination.
- [Supporting Conversions with Scripting Class Extensions](./supporting-conversions-with-scripting-class-extensions.md)
  Support conversions between the Apple event descriptor types and Foundation object classes.
- [Creating Scripting Definitions for Custom Share Destinations](./creating-scripting-definitions-for-custom-share-destinations.md)
  Define the record types, object classes, and event types that let your app interact with Final Cut Pro.

## See Also

### Data Received in Your App from Final Cut Pro
- [Supporting Drag and Drop to Receive Final Cut Pro Data](./supporting-drag-and-drop-to-receive-final-cut-pro-data.md)
  Add drag and drop support in your app to give users an intuitive way to receive clips, projects, and other items from Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/receiving-media-and-data-through-a-custom-share-destination)*