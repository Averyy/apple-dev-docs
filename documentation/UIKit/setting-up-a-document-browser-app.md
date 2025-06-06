# Setting up a document browser app

**Framework**: UIKit

Add a document browser view controller to your app.

#### Overview

Setting up the document browser is a three-step process:

1. Set the browser as your app’s root view controller.
2. Declare document browser support for your app.
3. Define the type of documents that the document browser can open.

The simplest way to do all three is to create a new project using the Document Based App template.

##### Create a New Document Based App

To create a new document-based app, open Xcode and choose File > New > Project. In the template chooser, under Application, choose the Document Based App template, and click Next.

![Xcode’s  project template pane. Both the iOS tab and the Document Based App icon are selected. ](https://docs-assets.developer.apple.com/published/5449c9fe83d4679fb5a76fcab4ee88bd/media-2920797%402x.png)

Continue following the prompts to create a document-based project. The following items appear in your new project:

- `Main.storyboard` contains a document browser view controller as its initial view controller. This storyboard sets the document browser as your app’s root view controller, ensuring that the browser remains in memory throughout your app’s lifetime.
- In your app’s `Info.plist` file, the [`UISupportsDocumentBrowser`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UISupportsDocumentBrowser) key is set to `YES`, declaring document browser support for your app. Specifically, this key lets other apps open and edit the files stored in your app’s Documents directory. It also lets users set the app’s default save location in Settings. For more information, see [`UISupportsDocumentBrowser`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW37).
- The app declares that it supports `public.image` document types. Users can then select image files in the document browser and share image files from other apps.

Use most of these default values as-is; however, unless you’re making an image-based app, you probably need to update the supported document types.

##### Set the Supported Document Types

For each document type your app supports, follow these steps in the project editor’s Info pane:

1. Click the Document Types disclosure triangle, and click the Add button (+) to add a new document type or open an existing document type.
2. Set the document type’s name and its uniform type identifier (UTI).
3. Click the “Additional document type properties” disclosure triangle.
4. Add the [`LSHandlerRank`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes/LSHandlerRank) key, and set its value to `Owner` or `Alternate`.
5. Optionally, set the other document type properties.

For example, for an app that edits text files, use the settings shown in the following image:

![A screenshot showing the document type settings for text files. The file type is set to public-plain.text, and the handler rank is set to Alternate.](https://docs-assets.developer.apple.com/published/c9bce09b41b8d9073d51f5a13fb28402/media-2948338%402x.png)

These entries set the [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes) key in your app’s `Info.plist` file as shown here:

```xml
<key>CFBundleDocumentTypes</key>
<array>
    <dict>
        <key>CFBundleTypeIconFiles</key>
        <array/>
        <key>CFBundleTypeName</key>
        <string>Text</string>
        <key>LSHandlerRank</key>
        <string>Alternate</string>
        <key>LSItemContentTypes</key>
        <array>
            <string>public.plain-text</string>
        </array>
    </dict>
</array>
```

For more information, see [`Set supported document types`](https://developer.apple.comhttp://help.apple.com/xcode/mac/current/#/devddd273fdd).

## See Also

- [Presenting selected documents](presenting-selected-documents.md)
  Display user-selected documents over your browser view controller.
- [Enabling document sharing](enabling-document-sharing.md)
  Give users the ability to import and export documents from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/setting-up-a-document-browser-app)*