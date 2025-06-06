# Quick Look

**Framework**: Quick Look  
**Kind**: module

Create previews of files to use inside your app, or perform simple edits on previews.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- visionOS 1.0+

#### Overview

When showing files in your app, including the ability to quickly preview a file and its content can be helpful to your users. For example, you may want to allow users to zoom into a photo, play back an audio file, and so on. Use the Quick Look framework to show a preview of common file types in your app that allows basic interactions. Quick Look can generate previews for common file types, including:

- iWork and Microsoft Office documents
- Images
- Live Photos
- Text files
- PDFs
- Audio and video files
- Augmented reality objects that use the USDZ file format (iOS and iPadOS only)

On iOS devices, the Quick Look framework provides functionality for performing simple edits on previews of common file types; for example, users can add markup to an image. To perform more advanced edits on files, provide advanced playback features, display a file’s content next to text, or add views on top of the preview, use lower-level APIs. For example, use [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) to provide advanced video playback features.

You can provide previews for your own data types by either rendering a view with your own view controller or by returning a supported preview format, such as PDF or HTML.

> **Note**:  The list of supported common file types may change between operating system releases.

 The list of supported common file types may change between operating system releases.

##### Providing Quick Look Previews for Your Data Types

To provide Quick Look previews for your own file types, create a Quick Look preview extension with either a view controller or data-based preview. In either case, add your supported content types to the `QLSupportedContentTypes` array in the `Info.plist` file of the extension.

To provide a view controller-based preview extension, set up a [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) that conforms to [`QLPreviewingController`](https://developer.apple.com/documentation/QuickLookUI/QLPreviewingController). Prepare and display the view within the [`preparePreviewOfFile(at:completionHandler:)`](https://developer.apple.com/documentation/QuickLookUI/QLPreviewingController/preparePreviewOfFile(at:completionHandler:)) method. To learn about creating a view controller preview extension, see [`Quick Look Previews from the Ground Up`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2018/237/).

To provide a data-based preview extension, implement a subclass of [`QLPreviewProvider`](https://developer.apple.com/documentation/QuickLookUI/QLPreviewProvider) to provide a [`QLPreviewReply`](https://developer.apple.com/documentation/QuickLookUI/QLPreviewReply) based on the [`QLFilePreviewRequest`](https://developer.apple.com/documentation/QuickLookUI/QLFilePreviewRequest) that the system provides.

## Topics

### Previews
- [class QLPreviewController](qlpreviewcontroller.md)
  A specialized view controller for previewing an item.
- [protocol QLPreviewItem : NSObjectProtocol](../QuickLookUI/QLPreviewItem.md)
  A protocol that defines a set of properties you implement to make a preview of your application’s content.
- [class QLPreviewSceneActivationConfiguration](qlpreviewsceneactivationconfiguration.md)
  A scene configuration to preview items at the specified URLs.
- [Previews or thumbnail images for macOS 10.14 or earlier](previews-or-thumbnail-images-for-macos-10-14-or-earlier.md)
  Create thumbnail images or previews of common files and custom file types in earlier versions of macOS.
### Preview extensions
- [protocol QLPreviewingController : NSObjectProtocol](../QuickLookUI/QLPreviewingController.md)
  A protocol for implementing a custom controller to create previews of files.
### Data-based preview extensions
- [class QLPreviewProvider](../QuickLookUI/QLPreviewProvider.md)
  A class that you subclass to provide a data-based Quick Look preview extension.
- [class QLFilePreviewRequest](../QuickLookUI/QLFilePreviewRequest.md)
  A Quick Look preview request that indicates the content to preview.
- [class QLPreviewReply](../QuickLookUI/QLPreviewReply.md)
  The class you create when providing a data-based Quick Look preview extension.
- [class QLPreviewReplyAttachment](../QuickLookUI/QLPreviewReplyAttachment.md)
  An attachment for a Quick Look preview reply that provides additional content for the system to display a preview.
### Classes
- [class PreviewApplication](previewapplication.md)
  A class you use to configure and launch the platform Quick Look application.
### Structures
- [struct PreviewItem](previewitem.md)
  An item to preview in the preview application.
- [struct PreviewSession](previewsession.md)
  A structure with which you can control an existing session and receive events for the current preview application.
### Type Aliases
- [typealias EditingMode](editingmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/QuickLook)*