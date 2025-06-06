# imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onCancellation:)

**Framework**: SwiftUI  
**Kind**: method

Presents the system sheet to create images from the specified input.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImageURL: URL, onCompletion: @escaping (URL) -> Void, onCancellation: (() -> Void)? = nil) -> some View
```

#### Discussion

Add this modifier to a view to display the system’s image-creation sheet. When the variable in the `isPresented` parameter is `true`, the view presents the sheet. Present the sheet in situations where someone might want to generate a new image for their content. When configuring the sheet, specify an optional starting image and text description to use to create the initial image.

While visible, the sheet allows people to experiment with the contents of an image before returning it to your app. The person viewing the sheet can accept the image they created or cancel the operation. When they make their choice, the system executes the appropriate block.

You can use this modifier only if the device supports creating new images. Check the `ImagePlayground/SwiftUICore/EnvironmentValues/supportsImagePlayground` environment variable to determine the availability of the feature. The following code creates a button to display the sheet only when the feature is available:

```swift
@State private var showSheet = false
@State private var createdImageURL: URL? = nil
@Environment(\.supportsImagePlayground) private var supportsImagePlayground
// ....

if supportsImagePlayground {
  Button("Show Generation Sheet") {
    showSheet = true
  }.imagePlaygroundSheet(
    isPresented: $showSheet,
    concept: "Dog on a surfboard",
    sourceImageURL: sourceImageURL) { url in
    createdImageURL = url
  }
}
```

## Parameters

- `isPresented`: A binding to a Boolean value that determines   whether to display the sheet.
- `concept`: An initial natural language string that describes the expected contents of the image.   The person viewing the creation UI can edit the concepts from inside that UI.    is equivalent to  .
- `sourceImageURL`: A file URL that refers to the image to use as the starting point for creating   the new image. The person viewing the sheet can override the image you provide, and choose   different images and concepts inside the creation UI. If you don’t provide a starting image,   the system creates the new image.
- `onCompletion`: The block to receive the created image. The block   has no return value and receives the following parameter:
- `onCancellation`: The block to execute when the person exits.   the creation UI without choosing an image. After executing this block,   the system automatically dismisses the sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/imageplaygroundsheet(ispresented:concept:sourceimageurl:oncompletion:oncancellation:))*