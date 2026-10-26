# SCNScene

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A container for the node hierarchy and global properties that together form a displayable 3D scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class SCNScene
```

```objc
@interface SCNScene : NSObject
```

#### Overview

To display 3D content with SceneKit, you create a scene containing a hierarchy of the nodes and attributes that together represent your visual elements. Typically, you build your assets in a 3D visual editor, then assemble them into a scene using Xcode’s SceneKit Scene Editor, ready for SceneKit to render.

![At the left, a diagram showing a simple scene composed of the node hierarchy and presentation attributes. At the right, the resulting rendered scene.](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2994226@2x.png)

To display your scene, you need to load it at runtime, then set it as the scene property of an [`SCNView`](./scnview.md):

```swift
guard let myScene = SCNScene(named: "MyScene") 
    else { fatalError("Unable to load scene file.") }
scnView.scene = myScene // Your app's SCNView
```

##### Creating a Scene

The simplest way to create a scene is through Xcode’s SceneKit Scene Editor. Start by importing one or more assets from a 3D editor, such as Blender. Then you adjust the positions and attributes of the assets, and set global scene properties, such as lighting environment, to compose your scene. The scene editor creates a `.scn` file, which you save to a `.scnassets` folder in the app bundle. When you build your project, Xcode optimizes the scene file for your target platform.

## Topics

### Creating a Scene from a File
- [convenience init?(named: String)](./scnscene/init%28named%29.md)
  Loads a scene from a file with the specified name in the app’s main bundle.
- [convenience init?(named: String, inDirectory: String?, options: [SCNSceneSource.LoadingOption : Any]?)](./scnscene/init%28named,indirectory,options%29.md)
  Loads a scene from a file with the specified name in a specific subdirectory of the app’s main bundle.
- [convenience init(url: URL, options: [SCNSceneSource.LoadingOption : Any]?) throws](./scnscene/init%28url,options%29-7ugvv.md)
  Loads a scene from the specified URL.
- [+ scene](./scnscene/scene.md)
  Creates and returns an empty scene.
### Managing Animated Effects in a Scene
- [var isPaused: Bool](./scnscene/ispaused.md)
  A Boolean value that determines whether to run actions, animations, particle systems, and physics simulations in the scene graph.
### Accessing Scene Contents
- [var rootNode: SCNNode](./scnscene/rootnode.md)
  The root node of the scene graph.
- [var background: SCNMaterialProperty](./scnscene/background.md)
  A background to be rendered before the rest of the scene.
- [var lightingEnvironment: SCNMaterialProperty](./scnscene/lightingenvironment.md)
  A cube map texture that depicts the environment surrounding the scene’s contents, used for advanced lighting effects.
### Managing Scene Attributes
- [func attribute(forKey: String) -> Any?](./scnscene/attribute%28forkey%29.md)
  Returns the scene attribute for the specified key.
- [func setAttribute(Any?, forKey: String)](./scnscene/setattribute%28_,forkey%29.md)
  Sets a scene attribute for the specified key.
- [SCNScene.Attribute](./scnscene/attribute.md)
### Exporting a Scene File
- [func write(to: URL, options: [String : Any]?, delegate: (any SCNSceneExportDelegate)?, progressHandler: SCNSceneExportProgressHandler?) -> Bool](./scnscene/write%28to,options,delegate,progresshandler%29.md)
  Exports the scene and its contents to a file at the specified URL.
- [protocol SCNSceneExportDelegate](./scnsceneexportdelegate.md)
  Methods you can implement to participate in the process of exporting a scene to a file.
### Adding Fog to a Scene
- [var fogStartDistance: CGFloat](./scnscene/fogstartdistance.md)
  The distance from a point of view at which the scene’s contents begin to be obscured by fog. Animatable.
- [var fogEndDistance: CGFloat](./scnscene/fogenddistance.md)
  The distance from a point of view at which the scene’s contents are completely obscured by fog. Animatable.
- [var fogDensityExponent: CGFloat](./scnscene/fogdensityexponent.md)
  The transition curve for the fog’s intensity between its start and end distances. Animatable.
- [var fogColor: Any](./scnscene/fogcolor.md)
  The color of the fog effect to be rendered with the scene. Animatable.
### Working With Physics in the Scene
- [var physicsWorld: SCNPhysicsWorld](./scnscene/physicsworld.md)
  The physics simulation associated with the scene.
### Working with Particle Systems in the Scene
- [func addParticleSystem(SCNParticleSystem, transform: SCNMatrix4)](./scnscene/addparticlesystem%28_,transform%29.md)
  Attaches a particle system to the scene, using the specified transform.
- [var particleSystems: [SCNParticleSystem]?](./scnscene/particlesystems.md)
  The particle systems attached to the scene.
- [func removeParticleSystem(SCNParticleSystem)](./scnscene/removeparticlesystem%28_%29.md)
  Removes a particle system attached to the scene.
- [func removeAllParticleSystems()](./scnscene/removeallparticlesystems%28%29.md)
  Removes any particle systems directly attached to the scene.
### Constants
- [Scene Attributes](./scene-attributes.md)
  Attribute keys available in the options dictionary for the methods  [`attribute(forKey:)`](./scnscene/attribute%28forkey%29.md) and [`setAttribute(_:forKey:)`](./scnscene/setattribute%28_,forkey%29.md)
- [Scene Export Options](./scene-export-options.md)
  Options for the [`write(to:options:delegate:progressHandler:)`](./scnscene/write%28to,options,delegate,progresshandler%29.md) method.
- [typealias SCNSceneExportProgressHandler](./scnsceneexportprogresshandler.md)
  The signature for the block that SceneKit calls during scene export.
### Initializers
- [convenience init(URL: URL, options: [SCNSceneSource.LoadingOption : Any]?) throws](./scnscene/init%28url,options%29-2hc8n.md)
- [init?(coder: NSCoder)](./scnscene/init%28coder%29.md)
### Instance Properties
- [var screenSpaceReflectionMaximumDistance: CGFloat](./scnscene/screenspacereflectionmaximumdistance.md)
- [var screenSpaceReflectionSampleCount: Int](./scnscene/screenspacereflectionsamplecount.md)
- [var screenSpaceReflectionStride: CGFloat](./scnscene/screenspacereflectionstride.md)
- [var wantsScreenSpaceReflection: Bool](./scnscene/wantsscreenspacereflection.md)
### Creating a Scene from a Model I/O Asset
- [+ sceneWithMDLAsset:](./scnscene/scenewithmdlasset_.md)
  Creates a scene from the specified Model I/O asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [GKSceneRootNodeType](../GameplayKit/gkscenerootnodetype.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Essentials
- [class SCNView](./scnview.md)
  A view for displaying 3D SceneKit content.
- [struct SceneView](./sceneview.md)
  A SwiftUI view for displaying 3D SceneKit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene)*