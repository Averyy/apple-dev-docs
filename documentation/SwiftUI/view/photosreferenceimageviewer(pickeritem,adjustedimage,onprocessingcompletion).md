# photosReferenceImageViewer(pickerItem:adjustedImage:onProcessingCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an image viewer for an image containing Apple Reference Image data selected from the Photos picker when `pickerItem` is set.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+

## Declaration

```swift
@MainActor
@preconcurrency func photosReferenceImageViewer(pickerItem: Binding<PhotosPickerItem?>, adjustedImage: CGImage?, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View
```

## Discussion

- Parameters

  - pickerItem: The `PhotosPickerItem` returned from a SwiftUI Photos picker.
  - adjustedImage: An adjusted rendition of the picked image to display in place of it. Pass `nil` to show the picked image itself. If the image can’t be read, the viewer shows the unadjusted picked image instead, without reporting an error. Don’t modify the image’s underlying pixel data while it’s displayed. The reference image is still read from the picked image, not from this image.
  - onProcessingCompletion: An optional closure called when processing completes. The closure contains a result with either the newly created asset that contains the processed reference image, or an error detailing why the processing failed. The original asset is deleted, so you should use the returned asset as the new representation of the originally provided picker item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photosreferenceimageviewer(pickeritem:adjustedimage:onprocessingcompletion:))*