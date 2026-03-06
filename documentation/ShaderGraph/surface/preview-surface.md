# Preview Surface

**Framework**: ShaderGraph  
**Kind**: subscript

A MaterialX version of USD Preview Surface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Description

- **`Diffuse Color`**: The base display color of the surface. The color of an object under pure white light.
- **`Roughness`**: The level of roughness of the surface. This value ranges between `0` and `1.0`, with `0` outputting a perfectly specular surface and `1.0` indicating maximum roughness. The default is `0.5`.
- **`Metallic`**: The indicator if a surface is metallic or not. Set this value to `1` for metallic surfaces and `0` for nonmetallic surfaces. The default is `0.0`.
- **`Opacity`**: The level of opaqueness of the surface. If the value of this parameter is `1.0`, the surface is fully opaque. If the value is less than `1.0`, the surface appears translucent. If the value is `0`, the surface is completely transparent. The default is `1.0`.
- **`Normal`**: The normal vector in tangent space; the default is `(0,0,1)`.
- **`Clearcoat`**: A second clear reflective layer on the surface. This property produces a glossy finish. The default is `0.0`.
- **`Clearcoat Roughness`**: The level of roughness of the surfaces clearcoat layer; the default is `0.01`.
- **`Emissive Color`**: The self-illumination color of the surface. The color the surface displays as if it is self-lit.
- **`Index of Refraction`**: The index of refraction the node uses if the surface is translucent or specular. The `Index of Refraction` defines how light bends or refracts when it passes through a material. The default is `1.5`.
- **`Ambient Occlusion`**: The degree of ambient lighting that the surface receives. This value simulates soft shadows and subtle shading. A value of `0.0` indicates a fully occluded area, while a value of `1.0` indicates an unoccluded area. The default is `1.0`.
- **`Opacity Threshold`**: The threshold for whether the node renders a portion of the surface based on its opacity level. A value of `0.0` means that no additional masking occurs. If the value is greater than `0.0`, the node renders only areas of the surface with an `Opacity` value greater than the value of this parameter. The default is `0.0`.

#### Discussion

The `Preview Surface` node produces a custom surface based on its input parameters. Connect the output of the `Preview Surface` node to the `Custom Surface` output of your material. Below is an example material that uses only the `Preview Surface` node to produce a gold-like texture and apply it to a sphere:


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/surface/preview-surface)*