# photosReferenceImageViewer(asset:adjustedImage:onProcessingCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an image viewer for an asset in a photo library that contains Apple Reference Image data when `asset` is set.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+

## Declaration

```swift
@MainActor
@preconcurrency func photosReferenceImageViewer(asset: Binding<PHAsset?>, adjustedImage: CGImage?, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View
```

## Discussion

- Parameters

  - asset: A `PHAsset` that is an image that contains Apple Reference Image data.
  - adjustedImage: An adjusted rendition of the asset to display in place of it. Pass `nil` to show the asset itself. If the image can’t be read, the viewer shows the unadjusted asset instead, without reporting an error. Don’t modify the image’s underlying pixel data while it’s displayed. The reference image is still read from the asset, not from this image.
  - onProcessingCompletion: An optional closure called when processing completes. The closure contains a result with either the newly created asset that contains the processed reference image, or an error detailing why the processing failed. The original asset is deleted, so you should use the returned asset as the new representation of the originally provided asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photosreferenceimageviewer(asset:adjustedimage:onprocessingcompletion:))*