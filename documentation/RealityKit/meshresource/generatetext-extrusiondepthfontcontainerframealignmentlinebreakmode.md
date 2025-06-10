# generateText(_:extrusionDepth:font:containerFrame:alignment:lineBreakMode:)

**Framework**: RealityKit  
**Kind**: method

Generates a 3D mesh for rendering static text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency static func generateText(_ string: String, extrusionDepth: Float = 0.25, font: MeshResource.Font = .systemFont(ofSize: 16), containerFrame: CGRect = CGRect.zero, alignment: CTTextAlignment = .left, lineBreakMode: CTLineBreakMode = .byTruncatingTail) -> MeshResource
```

#### Return Value

The text mesh.

## Parameters

- `string`: The text to render.
- `extrusionDepth`: The extent, in meters, of the extruded text in the   z-axis direction.
- `font`: The font to use. The font size is in meters.
- `containerFrame`: Use a frame size of   to tell the method to create a frame large enough to   contain the generated text.
- `alignment`: How the text should be aligned in the text frame.
- `lineBreakMode`: How the text should wrap when reaching a frame   boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generatetext(_:extrusiondepth:font:containerframe:alignment:linebreakmode:))*