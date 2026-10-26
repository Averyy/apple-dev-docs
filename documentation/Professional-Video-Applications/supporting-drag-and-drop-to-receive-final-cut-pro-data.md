# Supporting Drag and Drop to Receive Final Cut Pro Data

**Framework**: Professional-Video-Applications  
**Role**: Article

Add drag and drop support in your app to give users an intuitive way to receive clips, projects, and other items from Final Cut Pro.

#### Overview

Drag and drop is a good choice for receiving data when your users need to transfer a relatively small number of items from Final Cut Pro to your app. If your users often go back and forth between Final Cut Pro and your app as they receive data from Final Cut Pro, supporting drag and drop in your app could streamline that workflow by letting them drag items directly from the Final Cut Pro sidebar or browser to your app.

> 💡 **Tip**: If you want your users to be able to send rendered media (movies) to your app, set up a custom share destination. (See [Receiving Media and Data Through a Custom Share Destination](./receiving-media-and-data-through-a-custom-share-destination.md).)

Drag and drop operations use a `pasteboard` as the standardized mechanism for exchanging data between apps.

![Illustration showing an F C P X M L document moving from Final Cut Pro to your app using the pasteboard. ](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3878515@2x.png)

Once your user selects objects in the Final Cut Pro sidebar or browser and starts dragging them, Final Cut Pro creates a *promise*—a commitment to provide a data representation—in the dragging pasteboard. When your user drops the dragged objects into your app, your app requests the content of the promise. Final Cut Pro fulfills the request by putting the FCPXML for the dragged objects into the pasteboard. Your app retrieves the FCPXML and creates the objects in your app.

For information on versioned pasteboard types, see [Pasteboard Types and Versions](./supporting-drag-and-drop-for-data-sent-to-final-cut-pro.md#Pasteboard-Types-and-Versions).

> **Note**:  When your users drag an object from Final Cut Pro to your app, only the metadata in the currently selected metadata view is included in the FCPXML. Users can change the metadata view in Final Cut Pro before they drag data to your app. For more information, see [Intro to metadata in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/intro-to-metadata-verc392f8885/mac).

##### Receive Pasteboard Data

When receiving XML, your app can begin checking the available types on the pasteboard to request the most appropriate type; typically the highest versioned pasteboard type your app supports. Requesting a versioned pasteboard type ensures that your app continues to function as expected if a user updates to a new version of Final Cut Pro, with a newer DTD version, before updating your app. Order the pasteboard types your app supports by priority. Then you can iterate through your app’s sorted pasteboard types and select the first type available on the pasteboard. The following code snippet shows how you can do this in your app.

**Swift**:

```swift
let sortedPasteboardTypes = ["com.apple.finalcutpro.xml.v1-10", "com.apple.finalcutpro.xml.v1-9", "com.apple.finalcutpro.xml"]
    .map { NSPasteboard.PasteboardType($0) }
for pasteboardType in sortedPasteboardTypes {
    guard let availableTypes = pasteboard.types, availableTypes.contains(pasteboardType),
          let data = pasteboard.data(forType: pasteboardType) else { continue }
    do {
        let document = try XMLDocument(data: data, options: [])
        parseXMLDocument(document)
    } catch let error {
        print(error)
    }
    break
}
```

**Objective-C**:

```objc
NSArray *sortedPasteboardTypes = @[@"com.apple.finalcutpro.xml.v1-10", @"com.apple.finalcutpro.xml.v1-9", @"com.apple.finalcutpro.xml"];
for (NSPasteboardType pasteboardType in sortedPasteboardTypes) {
    if ([pasteboard.types containsObject:pasteboardType]) {
        NSData *xmlData = [pasteboard dataForType:pasteboardType];
        NSError *error = nil;
        NSXMLDocument *xmlDoc = [[NSXMLDocument alloc] initWithData:xmlData options:NSXMLNodeOptionsNone error:&error];
        if (error != nil) {
            [self parseXMLDocument:xmlDoc];
        }
        break;
    }
}
```

The organization of the FCPXML document depends on what your users drag out of Final Cut Pro:

| When users drag | The FCPXML from Final Cut Pro includes |
| --- | --- |
| One or more events from the Final Cut Pro sidebar | The contents of the dragged events. Each event can contain multiple projects and clips; each project contains editing decisions and can include markers; and each clip can include keywords and ratings. (Information about the library that contains the events is not included.) |
| One or more items (projects and clips) in the Final Cut Pro browser | The contents of the dragged projects and clips. Each project contains editing decisions, along with any markers. Each clip can include keywords and ratings. (Information about the events that contain those items is not included.) |
| A single library from the Final Cut Pro sidebar | The contents of the entire library. The library can contain multiple events, which could contain multiple projects (with editing decisions and possibly with markers) and clips (possibly with keywords and ratings). |

In each case, metadata associated with the media assets (and in the selected metadata view) are available in the Resource section of the FCPXML document (See [Structure Your FCPXML Document](./creating-fcpxml-documents.md#Structure-Your-FCPXML-Document) for more details.)

You may decide to design your app so that it accepts only certain types of Final Cut Pro objects in specific areas. For example, one part of your app might accept events, while another part might accept only clips.

## See Also

### Data Received in Your App from Final Cut Pro
- [Receiving Media and Data Through a Custom Share Destination](./receiving-media-and-data-through-a-custom-share-destination.md)
  Receive rendered media (movies), editing descriptions for project timelines, library archives, and FCPXML for other Final Cut Pro items in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/supporting-drag-and-drop-to-receive-final-cut-pro-data)*