# GLKEffectPropertyLight

**Framework**: GLKit  
**Kind**: class

Lighting information for use in GLKit rendering effects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class GLKEffectPropertyLight
```

#### Overview

The lighting model implemented by [`GLKEffectPropertyLight`](glkeffectpropertylight.md) is identical to the lighting model implemented in OpenGL ES 1.1; each light interacts with any material properties on the effect to determine the intensity and color that particular light contributes to the scene at a fragment.

There are three basic kinds of lights: directional, point and spotlights.

- A directional light is considered to be infinitely far away, and always directs light in the same direction. To create a directional light, set the [`position`](glkeffectpropertylight/position.md) property to a vector whose `x`, `y`, and `z` components specify the direction to the light (that is, the negation of the direction the light is travelling in), and whose `w` component is set to `0.0`.
- A point light is placed at a position within the scene, and emits light in all directions. To create a directional light, set the [`position`](glkeffectpropertylight/position.md) property to a vector whose `x`, `y`, `z` and `w` components specify the homogenous coordinates for the position of the light in the scene. The `w` component is typically set to `1.0` and must not be set to `0.0`.

The intensity of a point light is adjusted using an distance attenuation function. This function is controlled by adjusting the [`constantAttenuation`](glkeffectpropertylight/constantattenuation.md), [`linearAttenuation`](glkeffectpropertylight/linearattenuation.md) or [`quadraticAttenuation`](glkeffectpropertylight/quadraticattenuation.md) properties. The default values for these properties create a light whose intensity is constant over distance.

- A spotlight is placed at a position within the scene, and emits light in a specific direction in a cone. To create a spotlight, set the [`position`](glkeffectpropertylight/position.md) property to a vector whose `x`, `y`, `z` and `w` components specify the homogenous coordinates for the position of the light in the scene. The `w` component must not be set to `0.0`. Then, set the [`spotDirection`](glkeffectpropertylight/spotdirection.md) property to a vector that specifies the direction of the light and the [`spotCutoff`](glkeffectpropertylight/spotcutoff.md) to a value less than `180.0`.

Like a point light, a spotlight’s intensity can be adjusted using the distance attenuation properties. A spotlight’s intensity can also be changed as a function of the spotlight angle by setting the [`spotExponent`](glkeffectpropertylight/spotexponent.md) property. The default value for a spotlight creates a spotlight whose intensity is not affected by the angle. That is, the spotlight radiates the same amount of light at the center and at the edge of the cone.

Lighting calculations are performed in eye-space coordinates.  The eye-space coordinates for the position and the spot direction are calculated at the precise moment that new position values are specified and may be affected by other properties of the effect. For more information, see [`GLKBaseEffect`](glkbaseeffect.md).

## Topics

### Configuring Common Lighting Properties
- [var enabled: GLboolean](glkeffectpropertylight/enabled.md)
  A Boolean value that indicates whether calculations should be performed on this light.
- [var position: GLKVector4](glkeffectpropertylight/position.md)
  The position of the light in world coordinates.
- [var transform: GLKEffectPropertyTransform](glkeffectpropertylight/transform.md)
  A transform applied to the light’s position and direction before calculating the contribution of the light.
### Configuring Light Colors
- [var ambientColor: GLKVector4](glkeffectpropertylight/ambientcolor.md)
  The ambient portion of the light.
- [var diffuseColor: GLKVector4](glkeffectpropertylight/diffusecolor.md)
  The diffuse portion of the light.
- [var specularColor: GLKVector4](glkeffectpropertylight/specularcolor.md)
  The specular portion of the light.
### Configuring Lighting Attenuation
- [var constantAttenuation: GLfloat](glkeffectpropertylight/constantattenuation.md)
  A constant factor applied to the attenuation of a point light or spotlight.
- [var linearAttenuation: GLfloat](glkeffectpropertylight/linearattenuation.md)
  A linear factor applied to the attenuation of a point light or spotlight.
- [var quadraticAttenuation: GLfloat](glkeffectpropertylight/quadraticattenuation.md)
  A quadratic factor applied to the attenuation of a point light or spotlight.
### Configuring Spotlight Properties
- [var spotCutoff: GLfloat](glkeffectpropertylight/spotcutoff.md)
  The angle in degrees where the spotlight is cut off.
- [var spotDirection: GLKVector3](glkeffectpropertylight/spotdirection.md)
  A vector indicating the direction the spotlight is projecting.
- [var spotExponent: GLfloat](glkeffectpropertylight/spotexponent.md)
  A value indicating how focused the spotlight is.
### Constants
- [enum GLKLightingType](glklightingtype.md)
  A constant that describes how lighting is calculated by an effect.

## Relationships

### Inherits From
- [GLKEffectProperty](glkeffectproperty.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GLKEffectProperty](glkeffectproperty.md)
  The abstract superclass for configuration information used in GLKit rendering effects.
- [class GLKEffectPropertyFog](glkeffectpropertyfog.md)
  Fog drawing information for use in GLKit rendering effects.
- [class GLKEffectPropertyTexture](glkeffectpropertytexture.md)
  Texture drawing parameters for use in GLKit rendering effects.
- [class GLKEffectPropertyMaterial](glkeffectpropertymaterial.md)
  Surface appearance properties for use in GLKit rendering effects.
- [class GLKEffectPropertyTransform](glkeffectpropertytransform.md)
  Coordinate transform information for use in GLKit rendering effects.
- [GLKit Effects Constants](glkit-effects-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight)*