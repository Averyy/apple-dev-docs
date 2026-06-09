# imagePlaygroundOptions(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the options to use when generating an image.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
nonisolated
func imagePlaygroundOptions(_ options: ImagePlaygroundOptions = ImagePlaygroundOptions()) -> some View
```

#### Return Value

An image playground sheet that generates images using the specified `options`.

#### Discussion

If you don’t provide any custom options, the sheet applies the default options to image generation.

## Parameters

- `options`: The options to apply when generating an image.

## See Also

- [func imagePlaygroundGenerationStyle(ImagePlaygroundStyle, in: [ImagePlaygroundStyle]) -> some View](view/imageplaygroundgenerationstyle(_:in:).md)
  Sets the selected and allowed styles to use when displaying the image generation sheet.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImage: Image?, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concept:sourceimage:oncompletion:oncancellation:).md)
  Presents the system sheet to create an image using the specified string and optional starting image.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImage: Image?, onCompletion: (URL) -> Void, onAdaptiveImageGlyphCreation: (NSAdaptiveImageGlyph) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concept:sourceimage:oncompletion:onadaptiveimageglyphcreation:oncancellation:).md)
  Presents the system sheet to create images from the specified input.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImageURL: URL, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concept:sourceimageurl:oncompletion:oncancellation:).md)
  Presents the system sheet to create an image using the specified string and image URL.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImageURL: URL, onCompletion: (URL) -> Void, onAdaptiveImageGlyphCreation: (NSAdaptiveImageGlyph) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concept:sourceimageurl:oncompletion:onadaptiveimageglyphcreation:oncancellation:).md)
  Presents the system sheet to create an image or Genmoji using the specified string and image URL.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImage: Image?, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concepts:sourceimage:oncompletion:oncancellation:).md)
  Presents the system sheet to create an image using one or more concepts and an optional starting image.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImage: Image?, onCompletion: (URL) -> Void, onAdaptiveImageGlyphCreation: (NSAdaptiveImageGlyph) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concepts:sourceimage:oncompletion:onadaptiveimageglyphcreation:oncancellation:).md)
  Presents the system sheet to create an image or Genmoji using one or more concepts and an optional starting image.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImageURL: URL, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concepts:sourceimageurl:oncompletion:oncancellation:).md)
  Presents the system sheet to create an image using one or more concepts and an image URL.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImageURL: URL, onCompletion: (URL) -> Void, onAdaptiveImageGlyphCreation: (NSAdaptiveImageGlyph) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concepts:sourceimageurl:oncompletion:onadaptiveimageglyphcreation:oncancellation:).md)
  Presents the system sheet to create an image or Genmoji using one or more concepts and an image URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/imageplaygroundoptions(_:))*