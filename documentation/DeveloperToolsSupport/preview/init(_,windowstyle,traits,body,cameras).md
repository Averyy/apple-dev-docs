# init(_:windowStyle:traits:body:cameras:)

**Framework**: DeveloperToolsSupport  
**Kind**: init  
**Role**: Initializer

Creates a preview of a SwiftUI view in a window with custom viewpoints.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(_ name: String? = nil, windowStyle: some WindowStyle, traits: PreviewTrait<Preview.ViewTraits>..., @ContentBuilder body: @escaping @MainActor () -> any View, @PreviewCameraBuilder cameras: () -> [PreviewCamera] = { return [] })
```

## Discussion

Preview macros expand into a declaration that calls this initializer. Don’t use this initializer directly. Instead use one of the macros, like [`Preview(_:windowStyle:traits:body:cameras:)`](../../SwiftUI/preview%28_,windowstyle,traits,body,cameras%29.md).

## Parameters

- `name`: An optional display name for the preview.
- `windowStyle`: The window style to use for the preview.
- `traits`: An optional list of [`PreviewTrait`](../previewtrait.md) instances that customize the appearance of the preview.
- `body`: A content builder that produces a SwiftUI view to preview.
- `cameras`: One or more preview cameras that indicate the custom, fixed viewpoints that you want to be able to view the preview from.

## See Also

### Creating a SwiftUI preview
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](./init%28_,traits,body%29-8pemr.md)
  Creates a preview of a SwiftUI view.
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./init%28_,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.
- [init(String?, immersionStyle: some ImmersionStyle, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./init%28_,immersionstyle,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:windowstyle:traits:body:cameras:))*