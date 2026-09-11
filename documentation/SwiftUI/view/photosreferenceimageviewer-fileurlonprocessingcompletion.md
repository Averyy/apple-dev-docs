# photosReferenceImageViewer(fileURL:onProcessingCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents an image viewer for a given image file containing Apple Reference Image data when `fileURL` is set.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func photosReferenceImageViewer(fileURL: Binding<URL?>, onProcessingCompletion: ((Result<URL, any Error>) -> Void)?) -> some View
```

#### Discussion

- Parameters - fileURL: A binding to an optional URL that refers to the file containing the Apple Reference Image image. When non-nil, the sheet will be presented.
- onProcessingCompletion: An optional closure called when processing completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photosreferenceimageviewer(fileurl:onprocessingcompletion:))*