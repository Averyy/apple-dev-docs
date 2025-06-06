# init(_:windowStyle:traits:body:cameras:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a preview of a SwiftUI view in a window with custom viewpoints.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(_ name: String? = nil, windowStyle: some WindowStyle, traits: PreviewTrait<Preview.ViewTraits>..., @ViewBuilder body: @escaping @MainActor () -> any View, @PreviewCameraBuilder cameras: () -> [PreviewCamera] = { return [] })
```

#### Discussion

Preview macros expand into a declaration that calls this initializer. Don’t use this initializer directly. Instead use one of the macros, like [`Preview(_:windowStyle:traits:body:cameras:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:windowStyle:traits:body:cameras:)).

## Parameters

- `name`: An optional display name for the preview.
- `windowStyle`: The window style to use for the preview.
- `traits`: An optional list of     instances that customize the appearance of the preview.
- `body`: A view builder that produces a SwiftUI view to preview.
- `cameras`: One or more preview cameras that indicate the custom, fixed   viewpoints that you want to be able to view the preview from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:windowstyle:traits:body:cameras:))*