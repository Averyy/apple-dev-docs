# Providing Thumbnails of Your Custom File Types

**Framework**: Quick Look Thumbnailing

Implement a Thumbnail Extension to allow the operating system and other apps to display thumbnails of your custom files.

#### Overview

Add a Thumbnail Extension to your app to enable other apps to create thumbnails of your custom file types using the [`QLThumbnailGenerator`](qlthumbnailgenerator.md) object. In addition, this allows the operating system to display rich thumbnails for your custom file types instead of a generic file icon. For example, if your app implements a Thumbnail extension, the iOS Files app and Finder on macOS display thumbnails for your custom file types when the user installs your app.

Adding a Thumbnail Extension also enables iCloud to generate a thumbnail alongside your custom file, enabling other devices to display the thumbnail once the file has been synced with iCloud.

##### Add a Thumbnail Extension to Your App

To add a Thumbnail Extension to your app, select your project in Xcode’s Project navigator and make sure the General pane is visible. Select the + button and add a new Thumbnail extension to your app. Make sure to allow Xcode to create and activate a new build scheme for the extension.

In addition to the new scheme for the Thumbnail extension, Xcode adds the following files to your project:

- A new group in the Project navigator for the extension.
- A [`QLThumbnailProvider`](qlthumbnailprovider.md) subclass that contains the code to generate a thumbnail representation of your custom file types.
- The extension’s `Info.plist` with information about the custom file types to associate with your app and the thumbnails’ minimum dimension.

##### Update the Extensions Infoplist

Xcode creates an `Info.plist` for your new Thumbnail Extension that contains two important entries below the `NSExtensionAttributes` key. Update the following entries in the `Info.plist` file:

##### Create Thumbnails for Your Custom File Types

Using Xcode’s Thumbnail Extension template adds a subclass of [`QLThumbnailProvider`](qlthumbnailprovider.md) to your project that contains an empty implementation of the [`provideThumbnail(for:_:)`](qlthumbnailprovider/providethumbnail(for:_:).md) method. Decide which of [`QLThumbnailReply`](qlthumbnailreply.md)’s initializers you want to use and add your implementation to create thumbnails for each [`QLThumbnailRepresentation.RepresentationType`](qlthumbnailrepresentation/representationtype.md). This decision depends on your app and its requirements; make sure to optimize your code that generates the thumbnails and keep any files as small as possible.

```swift
override func provideThumbnail(for request: QLFileThumbnailRequest, _ handler: @escaping (QLThumbnailReply?, Error?) -> Void) {
    
    // There are three ways to provide a thumbnail through a QLThumbnailReply. Only one of them should be used.
    
    // First way: Draw the thumbnail into the current context, set up with UIKit's coordinate system.
    handler(QLThumbnailReply(contextSize: request.maximumSize, currentContextDrawing: { () -> Bool in
        // Draw the thumbnail here.
        
        // Return true if the thumbnail was successfully drawn inside this block.
        return true
    }), nil)
    
    /*
    
    // Second way: Draw the thumbnail into a context passed to your block, set up with Core Graphics's coordinate system.
    handler(QLThumbnailReply(contextSize: request.maximumSize, drawing: { (context) -> Bool in
        // Draw the thumbnail here.
     
        // Return true if the thumbnail was successfully drawn inside this block.
        return true
    }), nil)
     
    // Third way: Set an image file URL.
    handler(QLThumbnailReply(imageFileURL: Bundle.main.url(forResource: "fileThumbnail", withExtension: "jpg")!), nil)
    
    */
}
```

## See Also

- [class QLThumbnailProvider](qlthumbnailprovider.md)
  An abstract base class for creating thumbnails of custom file types.
- [class QLFileThumbnailRequest](qlfilethumbnailrequest.md)
  A request to generate a thumbnail for a custom file type.
- [class QLThumbnailReply](qlthumbnailreply.md)
  The object that provides a thumbnail for a custom file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/providing-thumbnails-of-your-custom-file-types)*