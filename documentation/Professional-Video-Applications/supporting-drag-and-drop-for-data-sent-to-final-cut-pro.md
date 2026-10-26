# Supporting Drag and Drop for Data Sent to Final Cut Pro

**Framework**: Professional-Video-Applications  
**Role**: Article

Add drag and drop support so your users can drag media assets and timeline sequences from your app directly into Final Cut Pro.

#### Overview

Enable drag and drop in your app so your users can drag media assets (or media assets as clips) directly to the Final Cut Pro sidebar, browser, or timeline. For example, if your users frequently send small batches of individual clips to different areas in Final Cut Pro, and often go back and forth between your app and Final Cut Pro, supporting drag and drop can make that process more intuitive.

Drag and drop operations use a pasteboard as the standardized mechanism for exchanging data between apps.

![Illustration showing the drag and drop movement of an F C P X M L file from your app through a pasteboard to Final Cut Pro.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3878513@2x.png)

When your users start dragging items from your app, it creates a *promise* — a commitment to provide a data representation — in the drag pasteboard. When users drop the assets into Final Cut Pro, Final Cut Pro retrieves the content of the promise, and the operating system requests the FCPXML document from your app. Your app returns the FCPXML document that represents the dragged asset.

> 💡 **Tip**: For information about creating an FCPXML document, see [Creating FCPXML Documents](./creating-fcpxml-documents.md); for examples of FCPXML that describe Final Cut Pro objects, see [Describing Final Cut Pro Items in FCPXML](./describing-final-cut-pro-items-in-fcpxml.md).

##### Pasteboard Types and Versions

Final Cut Pro supports a generic XML pasteboard type identified by the string `com.apple.finalcutpro.xml`. Starting in Final Cut Pro 10.5, DTD version 1.8 and later supports version-specific pasteboard types — such as, `com.apple.finalcutpro.xml.v1-8,` `com.apple.finalcutpro.xml.v1-9, or com.apple.finalcutpro.xml.v1-10`. Final Cut Pro looks for the version-specific pasteboard type with the highest version number and requests the XML associated with it. If there is no version-specific pasteboard type, Final Cut Pro finds the generic XML pasteboard type and requests the XML. When sending XML to your app, Final Cut Pro always writes XML for the current DTD version to the generic pasteboard type and the appropriate XML to each versioned pasteboard type.

For maximum compatibility, make sure your app supports the generic XML pasteboard type, that is, XML for the current DTD version as of your app’s release. It is also recommended that your app supports the versioned pasteboard types for the current and previous DTD versions as of your app’s release. Supporting these versions ensure that you take advantage of XML features for the highest DTD version supported by the user’s Final Cut Pro version.

##### Create a Promise in the Pasteboard

The specific steps to enable drag and drop in your app depend on your app’s design and purpose and include tasks such as adding support to the views in your app and implementing delegate methods. For details and more explanation about the steps for enabling drag and drop, see [Drag and Drop](../AppKit/drag-and-drop.md) in the AppKit framework.

When your app is ready to support drag and drop, use the following code snippet to create a promise. In the drag handler, instantiate your custom item-provider class that implements the [`NSPasteboardItemDataProvider`](../AppKit/nspasteboarditemdataprovider.md) protocol. Create a pasteboard item and set your custom item provider to it with the payload types you intend to support. You can then write the pasteboard item to the drag pasteboard. For more information, see [`NSPasteboardItem`](../AppKit/nspasteboarditem.md).

**Swift**:

```swift
let itemProvider = YourItemProvider(data: selection)
let item = NSPasteboardItem()    
//Set supported pasteboard types
let supportedPasteboardTypes = ["com.apple.finalcutpro.xml.v1-10", "com.apple.finalcutpro.xml.v1-9", "com.apple.finalcutpro.xml"]
    .map { NSPasteboard.PasteboardType($0) }
let isOK = item.setDataProvider(itemProvider, forTypes: supportedPasteboardTypes)
if isOK {
    draggingPasteboard.writeObjects([item])
}
```

**Objective-C**:

```objc
YourItemProvider *itemProvider = [[YourItemProvider alloc] initWithYourData:self.selection];
NSPasteboardItem *item = [[NSPasteboardItem alloc] init];

// set the item provider to the pasteboard item for the payload types
NSArray *supportedPasteboardTypes = @[@"com.apple.finalcutpro.xml.v1-10", @"com.apple.finalcutpro.xml.v1-9", @"com.apple.finalcutpro.xml"];
BOOL ok = [item setDataProvider: itemProvider forTypes:supportedPasteboardTypes];
if (ok) {
    [draggingPasteboard writeObjects:[NSArray arrayWithObject:item]];
}
```

##### Respond to Final Cut Pro and Return FCPXML

Once your user drops the dragged items into Final Cut Pro, Final Cut Pro takes over. It retrieves the data from the promise you created in the pasteboard, which invokes the `NSPasteboardItemDataProvider` protocol method in your app. (The method is expected to return FCPXML.)

Use the following code as a guide to implement the `NSPasteboardItemDataProvider` protocol method on your app’s custom pasteboard item provider class and return the FCPXML.

**Swift**:

```swift
func pasteboard(_ pasteboard: NSPasteboard?, item: NSPasteboardItem, provideDataForType type: NSPasteboard.PasteboardType) {
    let supportedPasteboardTypes = ["com.apple.finalcutpro.xml.v1-10", "com.apple.finalcutpro.xml.v1-9", "com.apple.finalcutpro.xml"]
    .map { NSPasteboard.PasteboardType($0) }
    guard supportedPasteboardTypes.contains(type) else { return }
    let document = itemData.newXMLDocument(forPasteboardType: type)
    let options: XMLDocument.Options = [.nodeCompactEmptyElement, .nodePrettyPrint]
    let data = document.xmlData(options: options)
    item.setData(data, forType: type)
}
```

**Objective-C**:

```objc
- (void)pasteboard:(NSPasteboard *)sender
              item:(NSPasteboardItem *)item
provideDataForType:(NSString *)type
{
    // be sure the type matches your expected payload type
NSArray *supportedPasteboardTypes = @[@"com.apple.finalcutpro.xml.v1-10", @"com.apple.finalcutpro.xml.v1-9", @"com.apple.finalcutpro.xml"];
    if ([supportedPasteboardTypes containsObject:type]) {
        // build a new XML document for what the user dragged
        NSXMLDocument* xmlDoc = [self.itemData newXMLDocumentForPasteboardType:type];
        NSUInteger xmlOptions = NSXMLNodeCompactEmptyElement | NSXMLNodePrettyPrint;
        NSData* xmlData = [xmlDoc XMLDataWithOptions:xmlOptions];
        
        if (xmlData != nil)
            [item setData:xmlData forType:type];
    }
}
```

Final Cut Pro validates the document type and the DTD version in the returned FCPXML, and then creates the objects it describes. If there are naming conflicts between new and existing objects, Final Cut Pro handles those conflicts according to the rules described in the following table.

| When users drag a file containing | Final Cut Pro does the following |
| --- | --- |
| One or more events to a library in the Final Cut Pro sidebar | Adds the events to the library. If the library already contains an event with the same name, Final Cut Pro merges the content of the new event with the content in the existing event. |
| One or more clips to a Final Cut Pro timeline | Adds the clips to the event containing the project that’s open in the timeline. Final Cut Pro then inserts the clips onto the timeline at the point where the user dropped them. |
| One or more event items, consisting of any combination of clips and projects with their associated metadata, into an event in the Final Cut Pro sidebar or browser | Adds the items to the event. If the event already contains an item of the same type with the same name, Final Cut Pro prompts the user to either replace the existing item or keep both. (If the user chooses to keep both, Final Cut Pro creates a unique name for the incoming item by adding a numerical suffix to the item’s name.) |
| One or more event items to a library in the Final Cut Pro sidebar | Final Cut Pro creates an event with the name of today’s date, as in `06-25-19`. If an event with that name already exists, Final Cut Pro adds a numeric suffix to create a unique name, as in `06-25-19 1`, and adds the items to the event. |

The type of object being dragged determines where it can be dropped. Final Cut Pro won’t accept a dragged item unless that item is allowed in the drop destination. For example, your users can drag clips into an event, but they can’t drag an event into a smart collection.

## See Also

### Data Sent from Your App to Final Cut Pro
- [Sending Media and Metadata to Final Cut Pro](./sending-media-and-metadata-to-final-cut-pro.md)
  Send media assets, timeline sequences, and metadata from your app to Final Cut Pro.
- [Sending Data Programmatically to Final Cut Pro](./sending-data-programmatically-to-final-cut-pro.md)
  Manage and streamline the sending of batches of media assets and timeline sequences from your app using Apple events.
- [Sending media to Final Cut Pro as it’s recorded](./sending-media-to-final-cut-pro-as-it-s-recorded.md)
  Designate media as a growing file to make it available to users while it’s still being recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/supporting-drag-and-drop-for-data-sent-to-final-cut-pro)*