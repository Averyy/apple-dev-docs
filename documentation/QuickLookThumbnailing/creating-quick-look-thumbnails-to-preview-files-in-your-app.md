# Creating Quick Look Thumbnails to Preview Files in Your App

**Framework**: Quick Look Thumbnailing

Generate thumbnails of images, text files, PDFs, audio files, videos, and more.

#### Overview

Apps often need to display a small, high-quality miniature representation, or , of a file or its content. The QuickLookThumbnailing framework provides a fast way to generate thumbnails for file types with the [`QLThumbnailGenerator`](qlthumbnailgenerator.md) object. It can create thumbnails for many common file types, including:

- Images, including raw image file types (the list of supported image formats varies for each platform; use the [`CGImageSourceCopyTypeIdentifiers()`](https://developer.apple.com/documentation/ImageIO/CGImageSourceCopyTypeIdentifiers()) method to retrieve a list of supported image types)
- Live Photos
- Text files
- PDF files
- Audio and video files (use [`AVURLAsset`](https://developer.apple.com/documentation/AVFoundation/AVURLAsset)’s [`audiovisualTypes()`](https://developer.apple.com/documentation/AVFoundation/AVURLAsset/audiovisualTypes()) method to retrieve a list of supported audio and video formats)
- Augmented reality objects using the `USDZ` file format (iOS and iPadOS only)

If an installed app implements a Thumbnail Extension that supports a custom file type, other apps can use [`QLThumbnailGenerator`](qlthumbnailgenerator.md) to create thumbnails of the custom file type. Read [`Providing Thumbnails of Your Custom File Types`](providing-thumbnails-of-your-custom-file-types.md) to learn more about adding a Thumbnail Extension to your app.

##### Generate a Thumbnail

Import the QuickLookThumbnailing framework and use [`QLThumbnailGenerator`](qlthumbnailgenerator.md) to create thumbnails. It provides asynchronous methods for three common use cases:

- To create the best possible thumbnail, use the [`generateBestRepresentation(for:completion:)`](qlthumbnailgenerator/generatebestrepresentation(for:completion:).md) method.
- Use the [`generateRepresentations(for:update:)`](qlthumbnailgenerator/generaterepresentations(for:update:).md) method to create a file icon or low-quality thumbnail quickly, and replace it with a higher quality thumbnail once it’s available. QuickLookThumbnailing calls the `updateHandler` in order of lower quality to higher quality thumbnail types. If a better quality thumbnail becomes available before a lower quality one, the framework may skip the call to the `updateHandler` for the lower quality thumbnail. You can rely on QuickLookThumbnailing to call the `updateHandler` at least once by the time it finishes the creation of thumbnails with either the best requested thumbnail, or an error object.
- Creating high-quality thumbnails often involves compressing a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) as a `PNG` or `JPEG` file in-process. This task requires more resources than are available in resource-constrained environments such as File Provider Extensions. Use the [`saveBestRepresentation(for:to:contentType:completion:)`](qlthumbnailgenerator/savebestrepresentation(for:to:contenttype:completion:).md) method to create and save the thumbnail image outside of your process as it doesn’t impose the same constraints on memory usage.

The following code listing generates all possible thumbnail representations for an image:

```swift
func generateThumbnailRepresentations() {
    
    // Set up the parameters of the request.
    guard let url = Bundle.main.url(forResource: "example", withExtension: "png") else {
        
        // Handle the error case.
        assert(false, "The URL can't be nil")
        return
    }
    let size: CGSize = CGSize(width: 60, height: 90)
    let scale = UIScreen.main.scale
    
    // Create the thumbnail request.
    let request = QLThumbnailGenerator.Request(fileAt: url,
                                               size: size,
                                               scale: scale,
                                               representationTypes: .all)
    
    // Retrieve the singleton instance of the thumbnail generator and generate the thumbnails.
    let generator = QLThumbnailGenerator.shared
    generator.generateRepresentations(for: request) { (thumbnail, type, error) in
        DispatchQueue.main.async {
            if thumbnail == nil || error != nil {
                // Handle the error case gracefully.
            } else {
                // Display the thumbnail that you created.
            }
        }
    }
}
```

You can cancel ongoing requests to generate thumbnails by using the [`cancel(_:)`](qlthumbnailgenerator/cancel(_:).md) method.

##### Request Thumbnails for Files in Icloud

You can create thumbnails for remote files stored in iCloud using [`QLThumbnailGenerator`](qlthumbnailgenerator.md). If you’re using a custom file type in your app, implement a Thumbnail extension as described in [`Providing Thumbnails of Your Custom File Types`](providing-thumbnails-of-your-custom-file-types.md). iCloud automatically calls your app’s extension and uploads a thumbnail image along with the file. QuickLookThumbnailing downloads the thumbnail the next time you request a thumbnail for the file stored in iCloud, ensuring that apps on devices that don’t have your app installed can display thumbnails of your custom files.

If a file is smaller than 1 MB and of a common file type such as an image, a PDF, or a video, iCloud doesn’t upload a thumbnail to save storage. Instead, QuickLookThumbnailing uses the actual file to create a thumbnail for you.

## See Also

- [class QLThumbnailGenerator](qlthumbnailgenerator.md)
  An object that generates thumbnail images based on provided requirements.
- [class QLThumbnailRepresentation](qlthumbnailrepresentation.md)
  Information about the thumbnail that the thumbnail generator returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/creating-quick-look-thumbnails-to-preview-files-in-your-app)*