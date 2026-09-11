# photosReferenceImageViewer(pickerItem:onProcessingCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents an image viewer for an image containing Apple Reference Image data selected from the Photos picker when `isPresented` is set to true.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func photosReferenceImageViewer(pickerItem: Binding<PhotosPickerItem?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View
```

#### Discussion

- Parameters - isPresented: A binding that determines when this view is presented.
- pickerItem: The `PhotosPickerItem` returned from a SwiftUI Photos picker.
- onProcessingCompletion: An optional closure called when processing completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photosreferenceimageviewer(pickeritem:onprocessingcompletion:))*