# generateText(_:extrusionDepth:font:containerFrame:alignment:lineBreakMode:)

**Framework**: RealityKit  
**Kind**: method

Generates a 3D mesh for rendering static text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generateText(_ string: String, extrusionDepth: Float = 0.25, font: MeshResource.Font = .systemFont(ofSize: defaultTextFontSize), containerFrame: CGRect = CGRect.zero, alignment: CTTextAlignment = .left, lineBreakMode: CTLineBreakMode = .byTruncatingTail) -> MeshResource
```

#### Return Value

The text mesh.

## Parameters

- `string`: The text to render.
- `extrusionDepth`: The extent, in meters, of the extruded text in the z-axis direction.
- `font`: The font to use. The font size is in meters. On tvOS the default is a 16-point system font; on other platforms it’s the standard system font size.
- `containerFrame`: The size, in meters, of the text frame in the local coordinate system where the text is laid out. The text frame has the same origin as the local coordinate system. Use a frame size of `(0,0)` to tell the method to create a frame large enough to contain the generated text.
- `alignment`: How the text should be aligned in the text frame.
- `lineBreakMode`: How the text should wrap when reaching a frame boundary.

## See Also

- [convenience init(extruding: AttributedString, textOptions: MeshResource.GenerateTextOptions, extrusionOptions: MeshResource.ShapeExtrusionOptions) throws](meshresource/init(extruding:textoptions:extrusionoptions:)-7xk2s.md)
  Synchronously generates a 3D mesh from a string, with options for text layout and custom extrusions.
- [convenience init(extruding: AttributedString, textOptions: MeshResource.GenerateTextOptions, extrusionOptions: MeshResource.ShapeExtrusionOptions) throws](meshresource/init(extruding:textoptions:extrusionoptions:)-7xk2s.md)
  Synchronously generates a 3D mesh from a string, with options for text layout and custom extrusions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generatetext(_:extrusiondepth:font:containerframe:alignment:linebreakmode:)-3py6y)*