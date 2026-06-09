# imagePlaygroundGenerationStyle(_:in:)

**Framework**: SwiftUI  
**Kind**: method

Sets the selected and allowed styles to use when displaying the image generation sheet.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
func imagePlaygroundGenerationStyle(_ style: ImagePlaygroundStyle, in allowedStyles: [ImagePlaygroundStyle] = ImagePlaygroundStyle.all) -> some View
```

#### Return Value

An image playground sheet configured with the specified style information.

#### Discussion

Configures the sheet with the specified style information. At presentation time, the sheet selects the style from the `style` parameter initially, but the person can change the selected style to any of the values in the `allowedStyles` parameter.

## Parameters

- `style`: The style to pre-select in the sheet. This style must also be present in the `allowedStyles` parameter.
- `allowedStyles`: The list of styles that the sheet can display to people. Specify `ImagePlaygroundStyle/all` to make all styles available from the sheet.

## See Also

- [func imagePlaygroundOptions(ImagePlaygroundOptions) -> some View](view/imageplaygroundoptions(_:).md)
  Sets the options to use when generating an image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/imageplaygroundgenerationstyle(_:in:))*