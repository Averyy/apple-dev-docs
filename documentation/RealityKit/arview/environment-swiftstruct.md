# ARView.Environment

**Framework**: RealityKit  
**Kind**: struct

A description of background, lighting, and acoustic properties for a view’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
struct Environment
```

## Topics

### Creating an environment
- [init(background: ARView.Environment.Background, lighting: ARView.Environment.ImageBasedLight, reverb: ARView.Environment.Reverb)](arview/environment-swift.struct/init(background:lighting:reverb:).md)
  Creates a new environment description with the given elements.
### Setting a background
- [var background: ARView.Environment.Background](arview/environment-swift.struct/background-swift.property.md)
  The background for the environment.
- [ARView.Environment.Background](arview/environment-swift.struct/background-swift.struct.md)
  Content that appears as the background of the scene.
### Lighting the environment
- [var lighting: ARView.Environment.ImageBasedLight](arview/environment-swift.struct/lighting.md)
  The lighting used in the environment of a particular scene.
- [ARView.Environment.ImageBasedLight](arview/environment-swift.struct/imagebasedlight.md)
  Lighting properties of an environment.
### Defining acoustic properties
- [var reverb: ARView.Environment.Reverb](arview/environment-swift.struct/reverb-swift.property.md)
  The amount of reverb in the scene.
- [ARView.Environment.Reverb](arview/environment-swift.struct/reverb-swift.enum.md)
  Reverb characteristics of an environment.
### Structures
- [ARView.Environment.SceneUnderstanding](arview/environment-swift.struct/sceneunderstanding-swift.struct.md)
  An object that holds scene-understanding options for the view.
### Instance Properties
- [var sceneUnderstanding: ARView.Environment.SceneUnderstanding](arview/environment-swift.struct/sceneunderstanding-swift.property.md)
  The scene-understanding options for the view.
### Type Aliases
- [ARView.Environment.Color](arview/environment-swift.struct/color.md)
  An alias for the color type that’s appropriate for the current platform.

## See Also

- [struct RealityViewEnvironment](realityviewenvironment.md)
  A struct that determines the background and default lighting properties for a reality view.
- [struct RealityViewRenderingEffects](realityviewrenderingeffects.md)
  A struct for enabling and disabling rendering effects for RealityKit content.
- [struct RealityViewRenderingEffectMode](realityviewrenderingeffectmode.md)
  A mode that determines whether a rendering effect is enabled or disabled.
- [struct RealityViewDynamicRange](realityviewdynamicrange.md)
  Options that determine the state of high dynamic range rendering for virtual content.
- [enum AntialiasingMode](antialiasingmode.md)
  The rendering technique used to smooth edges of virtual content.
- [struct RealityViewPostProcessEffect](realityviewpostprocesseffect.md)
  A struct for enabling or disabling post processing effects for all content a reality view contains.
- [struct PostProcessEffectContext](postprocesseffectcontext.md)
  An object RealityKit passes data to a post process effect method.
- [ARView.RenderOptions](arview/renderoptions-swift.struct.md)
  The available rendering options that you use to selectively disable certain rendering effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/environment-swift.struct)*