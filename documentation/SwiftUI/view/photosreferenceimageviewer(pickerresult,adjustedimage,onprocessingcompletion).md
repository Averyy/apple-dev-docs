# photosReferenceImageViewer(pickerResult:adjustedImage:onProcessingCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an image viewer for the resulting image containing Apple Reference Image data from `PHPickerViewController` when `pickerResult` is set.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+

## Declaration

```swift
@MainActor
@preconcurrency func photosReferenceImageViewer(pickerResult: Binding<PHPickerResult?>, adjustedImage: CGImage?, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View
```

## Discussion

- Parameters

  - pickerResult: The result from a `PHPickerViewController`
  - adjustedImage: An adjusted rendition of the picked image to display in place of it. Pass `nil` to show the picked image itself. If the image can’t be read, the viewer shows the unadjusted picked image instead, without reporting an error. Don’t modify the image’s underlying pixel data while it’s displayed. The reference image is still read from the picked image, not from this image.
  - onProcessingCompletion: An optional closure called when processing completes. The closure contains a result with either the newly created asset that contains the processed reference image, or an error detailing why the processing failed. The original asset is deleted, so you should use the returned asset as the new representation of the originally provided picker result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photosreferenceimageviewer(pickerresult:adjustedimage:onprocessingcompletion:))*