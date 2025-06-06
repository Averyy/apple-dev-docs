# Quick Look Thumbnailing

**Framework**: Quick Look Thumbnailing  
**Kind**: module

Generate thumbnails for common file types and add a Thumbnail Extension to your app to enable others to create thumbnails of your custom files.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

#### Overview

You may want to create a miniature representation, or , of a file and its contents to display within your app. The QuickLookThumbnailing framework provides an API to generate thumbnails using the [`QLThumbnailGenerator`](qlthumbnailgenerator.md) object. It can generate thumbnails for common file types, including:

- Images
- Live Photos
- Text files
- PDFs
- Audio and video files
- Augmented reality objects using the usdz file format (iOS and iPadOS only)

Many apps use custom file types to persist their data. Finder and Spotlight on macOS, other features of the operating system, as well as other apps, often display a generic file icon instead of a thumbnail for these files. However, if an installed app implements a Thumbnail Extension that supports the custom file types, the operating system and other apps can leverage the extension to display rich thumbnails of the custom file types through the [`QLThumbnailGenerator`](qlthumbnailgenerator.md) object. Add a Thumbnail Extension to your app to provide rich thumbnails of your custom file types to your users throughout the operating system and third party apps.

## Topics

### Thumbnail Generation
- [Creating Quick Look Thumbnails to Preview Files in Your App](creating-quick-look-thumbnails-to-preview-files-in-your-app.md)
  Generate thumbnails of images, text files, PDFs, audio files, videos, and more.
- [class QLThumbnailGenerator](qlthumbnailgenerator.md)
  An object that generates thumbnail images based on provided requirements.
- [class QLThumbnailRepresentation](qlthumbnailrepresentation.md)
  Information about the thumbnail that the thumbnail generator returns.
### Thumbnails for Custom File Types
- [Providing Thumbnails of Your Custom File Types](providing-thumbnails-of-your-custom-file-types.md)
  Implement a Thumbnail Extension to allow the operating system and other apps to display thumbnails of your custom files.
- [class QLThumbnailProvider](qlthumbnailprovider.md)
  An abstract base class for creating thumbnails of custom file types.
- [class QLFileThumbnailRequest](qlfilethumbnailrequest.md)
  A request to generate a thumbnail for a custom file type.
- [class QLThumbnailReply](qlthumbnailreply.md)
  The object that provides a thumbnail for a custom file type.
### Error Information
- [let QLThumbnailErrorDomain: String](qlthumbnailerrordomain.md)
  The error domain of the QuickLookThumbnailing framework.
- [struct QLThumbnailError](qlthumbnailerror-swift.struct.md)
  Error information that might return when you generate a thumbnail.
- [QLThumbnailError.Code](qlthumbnailerror-swift.struct/code.md)
  Error codes that may be returned when generating a thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/QuickLookThumbnailing)*