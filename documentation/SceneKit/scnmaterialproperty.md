# SCNMaterialProperty

**Framework**: SceneKit  
**Kind**: class

A container for the color or texture of one of a material’s visual properties.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNMaterialProperty
```

#### Overview

A material has several visual properties that together determine its appearance under lighting and shading. SceneKit renders each pixel in the scene by combining the information from material properties with the locations, intensities, and colors of lights.

A material property’s contents can be either a color, which provides a uniform effect across the surface of a material, or a texture, which SceneKit maps across the surface of a material using texture coordinates provided by the geometry object the material is attached to. A texture, in turn, can come from any of several sources, such as an image object, a URL to an image file, a specially formatted image or set of images for use as a cube map, or even animated content provided by Core Animation, SpriteKit, or AVFoundation—for the full set of options, see the [`contents`](scnmaterialproperty/contents.md) property.

> **Note**:  Typically, you associate texture images with materials when creating 3D assets with third-party authoring tools, and the scene files containing those assets reference external image files. For best results when shipping assets in your app bundle, place scene files in a folder with the `.scnassets` extension, and place image files referenced as textures from those scenes in an Asset Catalog. Xcode then optimizes the scene and texture resources for best performance on each target device, and prepares your texture resources for delivery features such as App Thinning and On-Demand Resources.

SceneKit uses the material property’s [`contents`](scnmaterialproperty/contents.md) object in different ways for each visual property of a material. For example:

- When you provide a color for the [`diffuse`](scnmaterial/diffuse.md) property, it determines the material’s base color—geometries using the material appear shaded in gradations of this color when illuminated by white light. If you instead provide an image, SceneKit maps the image across the geometry’s surface instead of shading with a uniform base color.
- When you provide a color for the [`specular`](scnmaterial/specular.md) property, it affects the color of light reflected directly toward the viewer from the surface of a geometry using the material. If you instead provide a grayscale image, it determines the tendency of the material to reflect light directly toward the viewer—lighter pixels in the image make those areas of the material appear more shiny, and darker pixels make the material appear more matte.
- The [`normal`](scnmaterial/normal.md) property specifies the orientation of a surface at each point. Materials are uniformly smooth by default, so specifying a color for this property has no useful effect. Instead, you can specify an image for this property that describes the contours of the surface. SceneKit uses this image (called a normal map) in lighting, creating the illusion of a complex, bumpy surface without increasing the complexity of the geometry.

For more details on each visual property and the ways their contents affect a material’s appearance, see [`SCNMaterial`](scnmaterial.md).

SceneKit also uses [`SCNMaterialProperty`](scnmaterialproperty.md) objects elsewhere:

- To provide content to be rendered behind a scene, in the [`background`](scnscene/background.md) property of an [`SCNScene`](scnscene.md) object,
- To affect the color and shape of illumination from a light source, in the [`gobo`](scnlight/gobo.md) property of an [`SCNLight`](scnlight.md) object.
- To bind texture samplers to custom GLSL shader source code snippets, in classes conforming to the [`SCNShadable`](scnshadable.md) protocol.

## Topics

### Creating a Material Property
- [convenience init(contents: Any)](scnmaterialproperty/init(contents:).md)
  Creates a new material property object with the specified contents.
### Working with Material Property Contents
- [var contents: Any?](scnmaterialproperty/contents.md)
  The visual contents of the material property—a color, image, or source of animated content. Animatable.
- [var intensity: CGFloat](scnmaterialproperty/intensity.md)
  A number between `0.0` and `1.0` that modulates the effect of the material property. Animatable.
### Configuring Texture Mapping Attributes
- [var contentsTransform: SCNMatrix4](scnmaterialproperty/contentstransform.md)
  The transformation applied to the material property’s visual contents. Animatable.
- [var wrapS: SCNWrapMode](scnmaterialproperty/wraps.md)
  The wrapping behavior for the S texture coordinate.
- [var wrapT: SCNWrapMode](scnmaterialproperty/wrapt.md)
  The wrapping behavior for the T texture coordinate.
- [enum SCNWrapMode](scnwrapmode.md)
  Modes to apply to texture wrapping, used by the [`wrapT`](scnmaterialproperty/wrapt.md) and [`wrapS`](scnmaterialproperty/wraps.md) properties.
- [var minificationFilter: SCNFilterMode](scnmaterialproperty/minificationfilter.md)
  Texture filtering for rendering the material property’s image contents at a size smaller than that of the original image.
- [var magnificationFilter: SCNFilterMode](scnmaterialproperty/magnificationfilter.md)
  Texture filtering for rendering the material property’s image contents at a size larger than that of the original image.
- [var mipFilter: SCNFilterMode](scnmaterialproperty/mipfilter.md)
  Texture filtering for using mipmaps to render the material property’s image contents at a size smaller than that of the original image.
- [enum SCNFilterMode](scnfiltermode.md)
  Texture filtering modes, used by the [`minificationFilter`](scnmaterialproperty/minificationfilter.md), [`magnificationFilter`](scnmaterialproperty/magnificationfilter.md), and [`mipFilter`](scnmaterialproperty/mipfilter.md) properties.
- [var maxAnisotropy: CGFloat](scnmaterialproperty/maxanisotropy.md)
  The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.
- [var mappingChannel: Int](scnmaterialproperty/mappingchannel.md)
  The source of texture coordinates for mapping the material property’s image contents.
- [var borderColor: Any?](scnmaterialproperty/bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.
### Instance Properties
- [var textureComponents: SCNColorMask](scnmaterialproperty/texturecomponents.md)
### Type Methods
- [class func precomputedLightingEnvironmentContents(with: Data) throws -> Any](scnmaterialproperty/precomputedlightingenvironmentcontents(with:)-2cwpt.md)
- [class func precomputedLightingEnvironmentContents(with: URL) throws -> Any](scnmaterialproperty/precomputedlightingenvironmentcontents(with:)-5f6ar.md)
- [class func precomputedLightingEnvironmentData(forContents: Any, device: (any MTLDevice)?) throws -> Data](scnmaterialproperty/precomputedlightingenvironmentdata(forcontents:device:).md)

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNAnimatable](scnanimatable.md)

## See Also

- [class SCNLight](scnlight.md)
  A light source that can be attached to a node to illuminate the scene.
- [class SCNCamera](scncamera.md)
  A set of camera attributes that can be attached to a node to provide a point of view for displaying the scene.
- [class SCNMaterial](scnmaterial.md)
  A set of shading attributes that define the appearance of a geometry’s surface when rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty)*