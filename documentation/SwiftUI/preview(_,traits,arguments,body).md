# Preview(_:traits:arguments:body:)

**Framework**: SwiftUI  
**Kind**: macro  
**Role**: Macro

Creates a group of previews of a parameterized SwiftUI view, varying its inputs over the provided arguments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 27.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @ContentBuilder body: @escaping @MainActor (T) -> any View)
```

## Parameters

- `name`: An optional display name for the preview. If you don’t specify a name, the canvas labels the preview using the line number where the preview appears in source.
- `traits`: Optional [`PreviewTrait`](../DeveloperToolsSupport/previewtrait.md) instances that customizes the appearance of the preview.
- `arguments`: An array of inputs to pass into the preview’s `body`.
- `body`: A [`ContentBuilder`](./contentbuilder.md) mapping an argument to a SwiftUI view to preview.

## See Also

### Creating a preview
- [macro Preview(String?, body: () -> any View)](./preview%28_,body%29.md)
  Creates a preview of a SwiftUI view.
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>, PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](./preview%28_,traits,_,body%29.md)
  Creates a preview of a SwiftUI view using the specified traits.
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./preview%28_,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/preview(_:traits:arguments:body:))*