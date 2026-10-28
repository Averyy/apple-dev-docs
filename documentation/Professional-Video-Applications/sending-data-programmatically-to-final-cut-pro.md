# Sending Data Programmatically to Final Cut Pro

**Framework**: Professional-Video-Applications  
**Role**: Article

Manage and streamline the sending of batches of media assets and timeline sequences from your app using Apple events.

## Overview

Consider using Apple events to help your users manage their workflow if they have many assets to send to Final Cut Pro and generally send all of those assets before starting their work in Final Cut Pro. With Apple event support in your app, your users need fewer clicks to send their media assets, projects, and metadata to Final Cut Pro for editing.

To provide a more streamlined process, use the `Open` `Document` Apple event to send an FCPXML document to Final Cut Pro and trigger the process with a button or menu item in your app.

![Illustration showing movement of Final Cut Pro X M L document from your app through an Apple event to Final Cut Pro.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3878514@2x.png)

### Create and Save an FCPXML File

Before your app can use Apple events to send a file to Final Cut Pro, it must create the FCPXML document, and save it as a file with an `.fcpxml` extension. See [Creating FCPXML Documents](./creating-fcpxml-documents.md).

Consider saving the `.fcpxml` file to a temporary location that your app clears periodically. Once Final Cut Pro processes the FCPXML, it no longer needs the actual `.fcpxml` file.

### Send an FCPXML File Using an Apple Event

To communicate your app’s request, create an AppleScript that sends an `Open` `Document` Apple event to Final Cut Pro. This Apple event contains a URL that points to an `.fcpxml` file your app created, and it tells Final Cut Pro to open and process that file.

Use the following AppleScript to send an `Open` `Document` Apple event containing the URL to an FCPXML file called `MyEvents.fcpxml`:

```swift
tell application "Final Cut Pro"
    activate
    open POSIX file "/Users/JohnDoe/Documents/UberMAM/MyEvents.fcpxml"
end tell
```

Use the following code to execute the AppleScript script created in the previous example:

**Swift**:

```swift
// the scriptSourceToSend property contains the AppleScript source above
let script = NSAppleScript(source: scriptSourceToSend)
var errorInfo: NSDictionary? = nil
let result = script?.executeAndReturnError(&errorInfo)
if result == nil { /* handle error */ }
```

**Objective-C**:

```objc
// the scriptSourceToSend property contains the AppleScript source above
NSAppleScript *script = [[NSAppleScript alloc] initWithSource:self.scriptSourceToSend];
NSDictionary *errorInfo = nil;
NSAppleEventDescriptor *result = [script executeAndReturnError:&errorInfo];
if (result == nil) { /* handle error */ }
```

AppleScript is the preferred way to send an FCPXML document to Final Cut Pro using the `Open` `Document` Apple event. AppleScript lets Final Cut Pro identify the app that’s sending the request, which means Final Cut Pro can provide that information when it reports an error or prompts for user action. The result is a better experience for your users. If you prefer, however, you can use `NSWorkspace` instead of AppleScript. (See the [NSWorkspace](https://developer.apple.com/library/archive/technotes/tn2050/_index.html#//apple_ref/doc/uid/DTS10003081-CH1-SUBSECTION8) developer documentation for details.)

### Specify a Library for the FCPXML File

When your app sends an FCPXML file to Final Cut Pro using an Apple event, Final Cut Pro displays the Open Library dialog so your user can choose where the content should go. Users can choose an existing library (or event) or create a new one.

You can also specify the location of the library as a URL by adding the `import` option to your FCPXML document. You can even have your app prompt users for the location of the library and add that information as the `import` option when it creates your FCPXML document. If no library exists at the location specified in the FCPXML file, Final Cut Pro creates a new one and gives it the default library name. For more information, see [import-options](./import-options.md).

Once Final Cut Pro determines a library for the data, it processes the FCPXML document and populates the content according to the following rules.

| If an FCPXML document contains | Final Cut Pro does the following |
| --- | --- |
| One or more clips or projects | Final Cut Pro creates a new event in the specified library named with today’s date, as in 06-29-19. Final Cut Pro then imports all items into the new event by copying or linking to the source data. (If an event with the same name already exists, Final Cut Pro adds a numerical suffix to the new event name to keep names unique, as in 06-29-19 1.) |
| Events | Final Cut Pro puts the events into the specified library, merging events with the same name. (If items within the merged events have the same name, Final Cut Pro asks the user whether to replace the existing item with the new item or keep both. If a user keeps both, Final Cut Pro adds a numerical suffix to the new item name to keep names unique. |
| A library | Final Cut Pro merges all the content into the specified library. Any naming conflicts between new and existing items are handled using the previous rules. |

## See Also

### Data Sent from Your App to Final Cut Pro
- [Sending Media and Metadata to Final Cut Pro](./sending-media-and-metadata-to-final-cut-pro.md)
  Send media assets, timeline sequences, and metadata from your app to Final Cut Pro.
- [Supporting Drag and Drop for Data Sent to Final Cut Pro](./supporting-drag-and-drop-for-data-sent-to-final-cut-pro.md)
  Add drag and drop support so your users can drag media assets and timeline sequences from your app directly into Final Cut Pro.
- [Sending media to Final Cut Pro as it’s recorded](./sending-media-to-final-cut-pro-as-it-s-recorded.md)
  Designate media as a growing file to make it available to users while it’s still being recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/sending-data-programmatically-to-final-cut-pro)*