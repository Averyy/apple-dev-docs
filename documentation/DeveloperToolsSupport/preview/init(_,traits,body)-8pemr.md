# init(_:traits:body:)

**Framework**: DeveloperToolsSupport  
**Kind**: init  
**Role**: Initializer

Creates a preview of a SwiftUI view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
init(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., body: @escaping @MainActor () -> any View)
```

#### Discussion

Preview macros expand into a declaration that calls this initializer. Don’t use this initializer directly. Instead use one of the macros, like [`Preview(_:body:)`](../../SwiftUI/preview%28_,body%29.md).

## Parameters

- `name`: An optional display name for the preview.
- `traits`: An optional list of [`PreviewTrait`](../previewtrait.md) instances that customize the appearance of the preview.
- `body`: A content builder that produces a SwiftUI view to preview.

## See Also

### Creating a SwiftUI preview
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./init%28_,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.
- [init(String?, immersionStyle: some ImmersionStyle, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./init%28_,immersionstyle,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.
- [init(String?, windowStyle: some WindowStyle, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./init%28_,windowstyle,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view in a window with custom viewpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:traits:body:)-8pemr)*