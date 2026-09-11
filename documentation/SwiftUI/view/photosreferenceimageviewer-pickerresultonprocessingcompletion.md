# photosReferenceImageViewer(pickerResult:onProcessingCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents an image viewer for the resulting image containing Apple Reference Image data from `PHPickerViewController` when `isPresented` is set to true.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func photosReferenceImageViewer(pickerResult: Binding<PHPickerResult?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View
```

#### Discussion

- Parameters - isPresented: A binding that determines when this view is presented.
- pickerResult: The result from a `PHPickerViewController`
- onProcessingCompletion: An optional closure called when processing completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photosreferenceimageviewer(pickerresult:onprocessingcompletion:))*