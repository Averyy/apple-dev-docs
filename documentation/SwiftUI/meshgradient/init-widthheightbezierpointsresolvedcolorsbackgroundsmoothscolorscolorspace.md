# init(width:height:bezierPoints:resolvedColors:background:smoothsColors:colorSpace:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new gradient mesh specified as a 2D grid of colored points, specifying the Bezier control points explicitly, with already-resolved sRGB colors.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(width: Int, height: Int, bezierPoints: [MeshGradient.BezierPoint], resolvedColors: [Color.Resolved], background: Color = .clear, smoothsColors: Bool = true, colorSpace: Gradient.ColorSpace = .device)
```

## Parameters

- `width`: The width of the mesh, i.e. the number of vertices   per row.
- `height`: The height of the mesh, i.e. the number of vertices   per column.
- `bezierPoints`: The array of points and control points,   containing   elements.
- `resolvedColors`: The array of colors, containing   elements.
- `background`: The background color, this fills any points   outside the defined vertex mesh.
- `smoothsColors`: Whether cubic (smooth) interpolation should   be used for the colors in the mesh (rather than only for the   shape of the mesh).
- `colorSpace`: The color space in which to interpolate vertex   colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/meshgradient/init(width:height:bezierpoints:resolvedcolors:background:smoothscolors:colorspace:))*