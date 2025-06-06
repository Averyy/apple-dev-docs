# SCNMaterial

**Framework**: SceneKit  
**Kind**: class

A set of shading attributes that define the appearance of a geometry’s surface when rendered.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNMaterial
```

#### Overview

When you create a material, you define a collection of visual attributes and their options, which you can then reuse for multiple geometries in a scene.

A material has several visual properties, each of which defines a different part of SceneKit’s lighting and shading process. Each visual property is an instance of the [`SCNMaterialProperty`](scnmaterialproperty.md) class that provides a solid color, texture, or other 2D content for that aspect of SceneKit’s rendering. The material’s [`lightingModel`](scnmaterial/lightingmodel-swift.property.md) property then determines the formula SceneKit uses to combine the visual properties with the lights in the scene to produce the final color for each pixel in the rendered scene. For more details on the rendering process, see [`SCNMaterial.LightingModel`](scnmaterial/lightingmodel-swift.struct.md).

You attach one or more materials to an instance of the [`SCNGeometry`](scngeometry.md) class using its [`firstMaterial`](scngeometry/firstmaterial.md) or [`materials`](scngeometry/materials.md) property. Multiple geometries can reference the same material. In this case, changing the attributes of the material changes the appearance of every geometry that uses it.

## Topics

### Creating a Material
- [var name: String?](scnmaterial/name.md)
  A name associated with the material.
### Choosing a Shading Model
- [var lightingModel: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.property.md)
  The lighting formula that SceneKit uses to render the material.
- [SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct.md)
  Constants specifying the lighting and shading algorithm to use for rendering a material.
### Visual Properties for Physically Based Shading
- [var diffuse: SCNMaterialProperty](scnmaterial/diffuse.md)
  An object that manages the material’s diffuse response to lighting.
- [var metalness: SCNMaterialProperty](scnmaterial/metalness.md)
  An object that provides color values to determine how metallic the material’s surface appears.
- [var roughness: SCNMaterialProperty](scnmaterial/roughness.md)
  An object that provides color values to determine the apparent smoothness of the surface.
### Visual Properties for Special Effects
- [var normal: SCNMaterialProperty](scnmaterial/normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var displacement: SCNMaterialProperty](scnmaterial/displacement.md)
- [var emission: SCNMaterialProperty](scnmaterial/emission.md)
  An object that defines the color emitted by each point on a surface.
- [var selfIllumination: SCNMaterialProperty](scnmaterial/selfillumination.md)
  An object that provides color values representing the global illumination of the surface.
- [var ambientOcclusion: SCNMaterialProperty](scnmaterial/ambientocclusion.md)
  An object that provides color values to be multiplied with the ambient light affecting the material.
### Visual Properties for Basic Shading
- [var diffuse: SCNMaterialProperty](scnmaterial/diffuse.md)
  An object that manages the material’s diffuse response to lighting.
- [var ambient: SCNMaterialProperty](scnmaterial/ambient.md)
  An object that manages the material’s response to ambient lighting.
- [var specular: SCNMaterialProperty](scnmaterial/specular.md)
  An object that manages the material’s specular response to lighting.
- [var reflective: SCNMaterialProperty](scnmaterial/reflective.md)
  An object that defines the reflected color for each point on a surface.
- [var multiply: SCNMaterialProperty](scnmaterial/multiply.md)
  An object that provides color values that are multiplied with pixels in a material after all other shading is complete.
- [var transparent: SCNMaterialProperty](scnmaterial/transparent.md)
  An object that determines the opacity of each point in a material.
- [var shininess: CGFloat](scnmaterial/shininess.md)
  The sharpness of specular highlights. Animatable.
- [var fresnelExponent: CGFloat](scnmaterial/fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.
- [var locksAmbientWithDiffuse: Bool](scnmaterial/locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.
### Managing Opacity and Blending
- [var transparency: CGFloat](scnmaterial/transparency.md)
  The uniform transparency of the material. Animatable.
- [var transparencyMode: SCNTransparencyMode](scnmaterial/transparencymode.md)
  The mode SceneKit uses to calculate transparency for the material.
- [enum SCNTransparencyMode](scntransparencymode.md)
  The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](scnmaterial/transparencymode.md) property.
- [var blendMode: SCNBlendMode](scnmaterial/blendmode.md)
  The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.
- [enum SCNBlendMode](scnblendmode.md)
  Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](scnmaterial/blendmode.md) property.
### Customizing Rendered Appearance
- [var isLitPerPixel: Bool](scnmaterial/islitperpixel.md)
  A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.
- [var isDoubleSided: Bool](scnmaterial/isdoublesided.md)
  A Boolean value that determines whether SceneKit renders both front and back faces of a surface.
- [var cullMode: SCNCullMode](scnmaterial/cullmode.md)
  The mode determining which faces of a surface SceneKit renders. Animatable.
- [enum SCNCullMode](scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](scnmaterial/cullmode.md) property.
- [var fillMode: SCNFillMode](scnmaterial/fillmode.md)
- [enum SCNFillMode](scnfillmode.md)
### Managing Render Targets
- [var writesToDepthBuffer: Bool](scnmaterial/writestodepthbuffer.md)
  A Boolean value that determines whether SceneKit produces depth information when rendering the material.
- [var readsFromDepthBuffer: Bool](scnmaterial/readsfromdepthbuffer.md)
  A Boolean value that determines whether SceneKit uses depth information when rendering the material.
- [var colorBufferWriteMask: SCNColorMask](scnmaterial/colorbufferwritemask.md)
- [struct SCNColorMask](scncolormask.md)
### Instance Properties
- [var clearCoat: SCNMaterialProperty](scnmaterial/clearcoat.md)
- [var clearCoatNormal: SCNMaterialProperty](scnmaterial/clearcoatnormal.md)
- [var clearCoatRoughness: SCNMaterialProperty](scnmaterial/clearcoatroughness.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNAnimatable](scnanimatable.md)
- [SCNShadable](scnshadable.md)

## See Also

- [class SCNLight](scnlight.md)
  A light source that can be attached to a node to illuminate the scene.
- [class SCNCamera](scncamera.md)
  A set of camera attributes that can be attached to a node to provide a point of view for displaying the scene.
- [class SCNMaterialProperty](scnmaterialproperty.md)
  A container for the color or texture of one of a material’s visual properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial)*