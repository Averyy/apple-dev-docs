# init(extruding:textOptions:extrusionOptions:)

**Framework**: RealityKit  
**Kind**: init

Synchronously generates a 3D mesh from a string, with options for text layout and custom extrusions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(extruding string: AttributedString, textOptions: MeshResource.GenerateTextOptions = GenerateTextOptions(), extrusionOptions: MeshResource.ShapeExtrusionOptions = ShapeExtrusionOptions()) throws
```

#### Discussion

You can use the method to make a 3D mesh of a string, control the text’s layout, chamfers, materials, and how to extrude the shape into 3D.

The generated text is scaled at a ratio of 72 points per meter.

![A screenshot of a living room scene with 3D text in the center that reads “Hello, World!”, which is primarily a teal color with chamfered, gray edges around the text’s faces that face the camera.](https://docs-assets.developer.apple.com/published/d965f02496a66cf068f71bd65a5243f5/meshResource-generateText-extrusion.jpg)

## Parameters

- `string`: A string that contains text for the 3D mesh geometry.
- `textOptions`: A configuration for rendering the text in 2D, before extrusion.
- `extrusionOptions`: A configuration for extruding the text in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(extruding:textoptions:extrusionoptions:))*