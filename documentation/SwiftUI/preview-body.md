# Preview(_:body:)

**Framework**: SwiftUI  
**Kind**: macro

Creates a preview of a SwiftUI view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview(_ name: String? = nil, @ViewBuilder body: @escaping @MainActor () -> any View)
```

#### Overview

Use this macro to display a SwiftUI preview in the canvas. You typically specify at least one preview macro for every [`View`](view.md) that your app defines to help you develop, test, and debug the view:

```swift
struct ContentView: View {
    var body: some View {
        // ...
    }
}

#Preview {
    ContentView()
}
```

If you include more than one preview in a source file, the canvas provides controls that enable you to select which to display when that source file is active. The canvas labels the different previews with the line number where the preview appears in source. To better identify the previews in the canvas, you can give them names. For example if your `ContentView` takes a Boolean input, you can create named previews for each input state:

```swift
#Preview("Input true") {
    ContentView(someInput: true)
}

#Preview("Input false") {
    ContentView(someInput: false)
}
```

Inside the preview, you can provide different inputs, model data, and other infrastructure that the view needs for normal operation. For example, you can present a custom view as the sidebar inside a [`NavigationSplitView`](navigationsplitview.md) if that’s how your app uses the view.

Other preview macros provide different customization options. For example, if you need to modify the appearance of a preview using one or more [`PreviewTrait`](https://developer.apple.com/documentation/DeveloperToolsSupport/PreviewTrait), instances, use the [`Preview(_:traits:_:body:)`](preview(_:traits:_:body:).md) macro.

## Parameters

- `name`: An optional display name for the preview. If you don’t specify a   name, the canvas labels the preview using the line number where the   preview appears in source.
- `body`: A   that produces a SwiftUI view to preview. You   typically specify one of your app’s custom views and optionally any   inputs, model data, modifiers, and enclosing views that the custom   view needs for normal operation.

## See Also

- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>, PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview(_:traits:_:body:).md)
  Creates a preview of a SwiftUI view using the specified traits.
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview(_:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/preview(_:body:))*