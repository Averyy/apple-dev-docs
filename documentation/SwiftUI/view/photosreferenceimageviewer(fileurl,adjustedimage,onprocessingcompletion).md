# photosReferenceImageViewer(fileURL:adjustedImage:onProcessingCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an image viewer for a given image file containing Apple Reference Image data when `fileURL` is set.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+

## Declaration

```swift
@MainActor
@preconcurrency func photosReferenceImageViewer(fileURL: Binding<URL?>, adjustedImage: CGImage?, onProcessingCompletion: ((Result<URL, any Error>) -> Void)?) -> some View
```

## Discussion

- Parameters

  - fileURL: A binding to an optional URL that refers to the file containing the Apple Reference Image. When non-nil, the sheet will be presented. Your app must have read access to this file.
  - adjustedImage: An adjusted rendition of the file’s image to display in place of it. Pass `nil` to show the file’s image itself. If the image can’t be read, the viewer shows the unadjusted file image instead, without reporting an error. Don’t modify the image’s underlying pixel data while it’s displayed. The reference image is still read from the file, not from this image.
  - onProcessingCompletion: An optional closure called when processing completes. The closure contains a file URL to a newly created file with processed reference image, or an error detailing why the processing failed. The new file is based on the input file, not the adjusted image. Your app should treat the returned file as the new representation of the provided reference image and future calls to the viewer should use this file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photosreferenceimageviewer(fileurl:adjustedimage:onprocessingcompletion:))*