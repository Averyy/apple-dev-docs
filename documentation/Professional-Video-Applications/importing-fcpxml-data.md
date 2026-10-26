# Importing FCPXML Data

**Framework**: Professional-Video-Applications  
**Role**: Article

Import data from Final Cut Pro to your app by using FCPXML.

#### Overview

FCPXML is a specialized format that uses XML elements to describe data that users send from Final Cut Pro to your app. Using FCPXML documents, your app can receive data from Final Cut Pro and then further process that data.

When your users choose to export XML from Final Cut Pro, they can select the XML version, either Current or Previous, for the export. When a user selects the Current version (FCPXML 1.10), Final Cut Pro exports a `.fcpxmld` bundle and an `Info.fcpxml` document located at the root of the bundle directory. Your app must support the `.fcpxmld` and `.fcpxml` document types. When a user selects the Previous version (FCPXML 1.9), Final Cut Pro exports a single `.fcpxml` document.

##### Add support for FCPXML documents and bundles

To add support for FCPXML documents and bundles to your app, update your project’s `Info.plist` file to include the `.fcpxml` and `.fcpxmld` document types. For information on modifying the document type, see the [Developing a Document-Based App](../AppKit/developing-a-document-based-app.md) section of the sample code, Developing a Document-Based App.

![The Xcode Information Property List table that shows the Key, Type, and Value columns. The Key column shows the  Information Property List first with nested Document Types. Update the Document Type Definitions to include the F C P X M L and F C P X M L D document types.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3875711@2x.png)

##### Check the extension when your app opens a file URL

When your app opens a file URL, your app must check the extension to determine whether the URL points to a `.fcpxml` document or a `.fcpxmld` bundle.

When your app receives a bundle, open and parse the `Info.fcpxml` file at the root of the bundle directory.

**Swift**:

```swift
@main
class AppDelegate: NSObject, NSApplicationDelegate {

    func application(_ application: NSApplication, open urls: [URL]) {
        let fcpxmlFileExtension = "fcpxml"
        let fcpxmlBundleExtension = "fcpxmld"
        for url in urls {
            switch url.pathExtension {
            case fcpxmlFileExtension:
                openFCPXMLDocument(at: url)
            case fcpxmlBundleExtension:
                let fcpxmlFileName = "Info.fcpxml"
                let fcpxmlFileURL = url.appendingPathComponent(fcpxmlFileName)
                openFCPXMLDocument(at: fcpxmlFileURL)
            default:
                continue
            }
        }
    }

    func openFCPXMLDocument(at url: URL) {}

}
```

**Objective-C**:

```objc
@implementation AppDelegate

- (void)application:(NSApplication *)application openURLs:(NSArray<NSURL *> *)urls {
    NSString *fcpxmlFileExtension = @"fcpxml";
    NSString *fcpxmlBundleExtension = @"fcpxmld";
    for (NSURL *url in urls) {
        NSString *pathExtension = [url pathExtension];
        if ([pathExtension isEqualToString:fcpxmlFileExtension]) {
            [self openFCPXMLDocumentAtURL:url];
        } else if ([pathExtension isEqualToString:fcpxmlBundleExtension]) {
            NSString *fcpxmlFileName = @"Info.fcpxml";
            NSURL *fcpxmlFileURL = [url URLByAppendingPathComponent:fcpxmlFileName];
            [self openFCPXMLDocumentAtURL:fcpxmlFileURL];
        } else {
            continue;
        }
    }
}

- (void)openFCPXMLDocumentAtURL:(NSURL *)url {}

@end
```

For information on examples of FCPXML documents, see [Describing Final Cut Pro Items in FCPXML](./describing-final-cut-pro-items-in-fcpxml.md).

## See Also

### Document Structure and Root Elements
- [Creating FCPXML Documents](./creating-fcpxml-documents.md)
  Describe media assets, editing decisions, metadata, and other items in FCPXML so users can send and receive data between your app and Final Cut Pro.
- [FCPXML Bundle Reference](./fcpxml-bundle-reference.md)
  Keep an FCPXML document and any files it references together in a bundle.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/importing-fcpxml-data)*