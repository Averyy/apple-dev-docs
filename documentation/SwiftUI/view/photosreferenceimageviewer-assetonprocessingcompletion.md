# photosReferenceImageViewer(asset:onProcessingCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents an image viewer for an asset in a photo library that contains Apple Reference Image data when `isPresented` is set to true.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func photosReferenceImageViewer(asset: Binding<PHAsset?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View
```

#### Discussion

- Parameters - isPresented: A binding that determines when this view is presented.
- asset: A `PHAsset` that is an image that contains Apple Reference Image data.
- onProcessingCompletion: An optional closure called when processing completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photosreferenceimageviewer(asset:onprocessingcompletion:))*