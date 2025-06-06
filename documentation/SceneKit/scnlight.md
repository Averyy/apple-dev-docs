# SCNLight

**Framework**: SceneKit  
**Kind**: class

A light source that can be attached to a node to illuminate the scene.

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
class SCNLight
```

#### Overview

You illuminate your scene by attaching lights to [`SCNNode`](scnnode.md) objects using their [`light`](scnnode/light.md) property.

You set a light’s type using its [`type`](scnlight/type.md) property. Depending on a light’s type, its position and direction may affect its behavior—you control the light’s position and direction through the node that the light is attached to. The direction of a light, if applicable to its type, is along the negative z-axis of its node’s local coordinate system.

A light’s other properties affect how it illuminates a scene. All lights have a [`color`](scnlight/color.md) property, which interacts with [`SCNMaterial`](scnmaterial.md) objects to produce the pixel colors in a rendered scene. Other properties, such as attenuation, shadowing, and spot angle, can affect the behavior of certain types of lights.

The number and type of lights in a scene is a key factor in SceneKit’s rendering performance. For efficient rendering, follow these tips:

- Use SceneKit lights only for dynamic light sources or lights that affect moving objects. For statically lit portions of your scene, create a light map texture in an external 3D authoring tool (also known as ) and apply it to objects in the scene using the [`multiply`](scnmaterial/multiply.md) material property.
- Minimize the number of lights on each element of the scene. You can achieve most common lighting effects using no more than three lights, and you only need a single ambient light source. SceneKit only uses up to eight light sources per node when rendering, ignoring any additional lights. If you set the [`attenuationEndDistance`](scnlight/attenuationenddistance.md) property on a spotlight or omnidirectional light to limit its area of effect, SceneKit ignores the light (and its performance cost) when rendering objects outside that area. You can also use the [`categoryBitMask`](scnlight/categorybitmask.md) property to choose which nodes are illuminated by a light.

## Topics

### Modifying a Light’s Appearance
- [var type: SCNLight.LightType](scnlight/type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](scnlight/lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](scnlight/type.md) property.
- [var color: Any](scnlight/color.md)
  The color of the light. Animatable.
- [var temperature: CGFloat](scnlight/temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var intensity: CGFloat](scnlight/intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.
- [var sphericalHarmonicsCoefficients: Data](scnlight/sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.
### Managing Light Attributes
- [var name: String?](scnlight/name.md)
  A name associated with the light.
- [func attribute(forKey: String) -> Any?](scnlight/attribute(forkey:).md)
  Returns the value of a lighting attribute.
- [func setAttribute(Any?, forKey: String)](scnlight/setattribute(_:forkey:).md)
  Sets the value for a lighting attribute.
- [Lighting Attribute Keys](lighting-attribute-keys.md)
  Keys for specifying the behavior of a light using the [`attribute(forKey:)`](scnlight/attribute(forkey:).md) and [`setAttribute(_:forKey:)`](scnlight/setattribute(_:forkey:).md) methods.
### Managing Light Attenuation
- [var attenuationStartDistance: CGFloat](scnlight/attenuationstartdistance.md)
  The distance from the light at which its intensity begins to diminish. Animatable.
- [var attenuationEndDistance: CGFloat](scnlight/attenuationenddistance.md)
  The distance from the light at which its intensity is completely diminished. Animatable.
- [var attenuationFalloffExponent: CGFloat](scnlight/attenuationfalloffexponent.md)
  The transition curve for the light’s intensity between its attenuation start and end distances. Animatable.
### Managing Spotlight Extent
- [var spotInnerAngle: CGFloat](scnlight/spotinnerangle.md)
  The angle, in degrees, of the area fully lit by a spotlight. Animatable.
- [var spotOuterAngle: CGFloat](scnlight/spotouterangle.md)
  The angle, in degrees, of the area partially lit by a spotlight. Animatable.
- [var gobo: SCNMaterialProperty?](scnlight/gobo.md)
  An image or other visual content affecting the shape and color of a light’s illuminated area.
### Managing Shadows Cast by the Light
- [var castsShadow: Bool](scnlight/castsshadow.md)
  A Boolean value that determines whether the light casts shadows.
- [var shadowRadius: CGFloat](scnlight/shadowradius.md)
  A number that specifies the amount of blurring around the edges of shadows cast by the light. Animatable.
- [var shadowColor: Any](scnlight/shadowcolor.md)
  The color of shadows cast by the light. Animatable.
- [var shadowMapSize: CGSize](scnlight/shadowmapsize.md)
  The size of the shadow map image that SceneKit renders when creating shadows.
- [var shadowSampleCount: Int](scnlight/shadowsamplecount.md)
  The number of samples from the shadow map that SceneKit uses to render each pixel.
- [var shadowMode: SCNShadowMode](scnlight/shadowmode.md)
  The mode SceneKit uses to render shadows.
- [enum SCNShadowMode](scnshadowmode.md)
  Options for SceneKit’s rendering of shadows cast by a light, used by the [`shadowMode`](scnlight/shadowmode.md) property.
- [var shadowBias: CGFloat](scnlight/shadowbias.md)
  The amount of correction to apply to the shadow to prevent rendering artifacts.
- [var orthographicScale: CGFloat](scnlight/orthographicscale.md)
  The orthographic scale SceneKit uses when rendering the shadow map for a directional light.
- [var zFar: CGFloat](scnlight/zfar.md)
  The maximum distance between the light and a visible surface for casting shadows.
- [var zNear: CGFloat](scnlight/znear.md)
  The minimum distance between the light and a visible surface for casting shadows. Animatable.
### Choosing Nodes to be Illuminated by the Light
- [var categoryBitMask: Int](scnlight/categorybitmask.md)
  A mask that defines which categories this light belongs to.
### Managing Photometric Lights
- [var iesProfileURL: URL?](scnlight/iesprofileurl.md)
  The URL for a file that contains photometry data describing the intended appearance of the light.
### Instance Properties
- [var areaExtents: simd_float3](scnlight/areaextents.md)
- [var areaPolygonVertices: [NSValue]?](scnlight/areapolygonvertices.md)
- [var areaType: SCNLightAreaType](scnlight/areatype.md)
- [var automaticallyAdjustsShadowProjection: Bool](scnlight/automaticallyadjustsshadowprojection.md)
- [var doubleSided: Bool](scnlight/doublesided.md)
- [var drawsArea: Bool](scnlight/drawsarea.md)
- [var forcesBackFaceCasters: Bool](scnlight/forcesbackfacecasters.md)
- [var maximumShadowDistance: CGFloat](scnlight/maximumshadowdistance.md)
- [var parallaxCenterOffset: simd_float3](scnlight/parallaxcenteroffset.md)
- [var parallaxCorrectionEnabled: Bool](scnlight/parallaxcorrectionenabled.md)
- [var parallaxExtentsFactor: simd_float3](scnlight/parallaxextentsfactor.md)
- [var probeEnvironment: SCNMaterialProperty?](scnlight/probeenvironment.md)
- [var probeExtents: simd_float3](scnlight/probeextents.md)
- [var probeOffset: simd_float3](scnlight/probeoffset.md)
- [var probeType: SCNLightProbeType](scnlight/probetype.md)
- [var probeUpdateType: SCNLightProbeUpdateType](scnlight/probeupdatetype.md)
- [var sampleDistributedShadowMaps: Bool](scnlight/sampledistributedshadowmaps.md)
- [var shadowCascadeCount: Int](scnlight/shadowcascadecount.md)
- [var shadowCascadeSplittingFactor: CGFloat](scnlight/shadowcascadesplittingfactor.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNAnimatable](scnanimatable.md)
- [SCNTechniqueSupport](scntechniquesupport.md)

## See Also

- [class SCNCamera](scncamera.md)
  A set of camera attributes that can be attached to a node to provide a point of view for displaying the scene.
- [class SCNMaterial](scnmaterial.md)
  A set of shading attributes that define the appearance of a geometry’s surface when rendered.
- [class SCNMaterialProperty](scnmaterialproperty.md)
  A container for the color or texture of one of a material’s visual properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight)*