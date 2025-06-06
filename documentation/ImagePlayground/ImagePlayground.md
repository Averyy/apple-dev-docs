# Image Playground

**Framework**: Image Playground  
**Kind**: module

Present a system interface to generate images based on descriptive information.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

#### Overview

Use the `ImagePlayground` framework to generate custom images using system-supported styles. To generate images, you specify a text description of what you want, an optional image, and the style you want the image to adopt. Use that information to present a system sheet from your SwiftUI view, or present a system view controller from your UIKit or AppKit interface. The system interface manages all interactions with the person, and upon success delivers an image for you to incorporate into your content. You can also use a programmatic interface to generate images without interactions.

## Topics

### SwiftUI presentation
- [@MainActor @preconcurrency func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImage: Image? = nil, onCompletion: @escaping (URL) -> Void, onCancellation: (() -> Void)? = nil) -> some View
](../SwiftUI/View/imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:).md)
  Presents the system sheet to create images from the specified input.
- [@MainActor @preconcurrency func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept] = [], sourceImage: Image? = nil, onCompletion: @escaping (URL) -> Void, onCancellation: (() -> Void)? = nil) -> some View
](../SwiftUI/View/imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:).md)
  Presents the system sheet to create images from the specified input.
- [@MainActor @preconcurrency func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept] = [], sourceImageURL: URL, onCompletion: @escaping (URL) -> Void, onCancellation: (() -> Void)? = nil) -> some View
](../SwiftUI/View/imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:).md)
  Presents the system sheet to create images from the specified input.
### UIKit and AppKit presentation
- [class ImagePlaygroundViewController](imageplaygroundviewcontroller.md)
  Displays a standard system interface to generate images from the provided input.
### Programmatic creation
- [class ImageCreator](imagecreator.md)
  Generates images programmatically from the description and style information you specify.
### Platform support
- [struct ImagePlaygroundConcept](imageplaygroundconcept.md)
  Text elements that specify the content to include in the image.
- [struct ImagePlaygroundStyle](imageplaygroundstyle.md)
  Style options that determine the appearance of generated images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ImagePlayground)*