# SceneKit

**Framework**: Scenekit  
**Kind**: module

Create 3D games and add 3D content to apps using high-level scene descriptions, and easily add animations, physics simulation, particle effects, and realistic physically based rendering.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

#### Overview

SceneKit combines a high-performance rendering engine with a descriptive API for import, manipulation, and rendering of 3D assets. Unlike lower-level APIs such as Metal and OpenGL that require you to implement in precise detail the rendering algorithms that display a scene, SceneKit requires only descriptions of your scene’s contents and the actions or animations you want it to perform.

> **Note**:  In visionOS, you can display SceneKit content only in 2D views and textures. For information about how to create immersive 3D content, see [`Creating fully immersive experiences in your app`](https://developer.apple.com/documentation/visionOS/creating-fully-immersive-experiences).

## Topics

### Essentials
- [class SCNScene](scnscene.md)
  A container for the node hierarchy and global properties that together form a displayable 3D scene.
- [class SCNView](scnview.md)
  A view for displaying 3D SceneKit content.
### Scene Structure
- [Organizing a Scene with Nodes](organizing-a-scene-with-nodes.md)
  Use nodes to define the structure of a scene.
- [class SCNNode](scnnode.md)
  A structural element of a scene graph, representing a position and transform in a 3D coordinate space, to which you can attach geometry, lights, cameras, or other displayable content.
- [class SCNReferenceNode](scnreferencenode.md)
  A scene graph node that serves as a placeholder for content to be loaded from a separate scene file.
### Display and Interactivity
- [protocol SCNSceneRenderer](scnscenerenderer.md)
  Methods and properties common to the [`SCNView`](scnview.md), [`SCNLayer`](scnlayer.md), and [`SCNRenderer`](scnrenderer.md) classes.
- [protocol SCNSceneRendererDelegate](scnscenerendererdelegate.md)
  Methods your app can implement to participate in SceneKit’s animation loop or perform additional rendering.
- [class SCNLayer](scnlayer.md)
  A Core Animation layer that renders a SceneKit scene as its content.
- [class SCNRenderer](scnrenderer.md)
  A renderer for displaying a SceneKit scene in an existing Metal workflow or OpenGL context.
- [class SCNHitTestResult](scnhittestresult.md)
  Information about the result of a scene-space or view-space search for scene elements.
### Lighting, Cameras, and Shading
- [class SCNLight](scnlight.md)
  A light source that can be attached to a node to illuminate the scene.
- [class SCNCamera](scncamera.md)
  A set of camera attributes that can be attached to a node to provide a point of view for displaying the scene.
- [class SCNMaterial](scnmaterial.md)
  A set of shading attributes that define the appearance of a geometry’s surface when rendered.
- [class SCNMaterialProperty](scnmaterialproperty.md)
  A container for the color or texture of one of a material’s visual properties.
### Geometry
- [class SCNGeometry](scngeometry.md)
  A three-dimensional shape (also called a model or mesh) that can be displayed in a scene, with attached materials that define its appearance.
- [class SCNGeometrySource](scngeometrysource.md)
  A container for vertex data forming part of the definition for a three-dimensional object, or geometry.
- [class SCNGeometryElement](scngeometryelement.md)
  A container for index data describing how vertices connect to define a three-dimensional object, or geometry.
- [Built-in Geometry Types](built-in-geometry-types.md)
  Basic shapes—such as spheres, boxes, and planes—and features for generating 3D objects from 2D text and Bézier curves.
### Animation and Constraints
- [Animation](animation.md)
  Create declarative animations that move elements of a scene in predetermined ways, or manage animations imported with external authoring tools.
- [Constraints](constraints.md)
  Automatically adjust the position or orientation of a node based on specified rules.
- [class SCNSkinner](scnskinner.md)
  An object that manages the relationship between skeletal animations and the nodes and geometries they animate.
- [class SCNMorpher](scnmorpher.md)
  An object that manages smooth transitions between a node’s base geometry and one or more target geometries.
### Physics
- [Physics Simulation](physics-simulation.md)
  Add dynamic behaviors to scene elements; detect contacts and collisions; simulate realistic effects like gravity, springs, and vehicles.
### Particle Systems
- [class SCNParticleSystem](scnparticlesystem.md)
  An object that animates and renders a system of small image sprites using a high-level simulation whose general behavior you specify.
- [class SCNParticlePropertyController](scnparticlepropertycontroller.md)
  An animation for a single property of the individual particles rendered by a particle system.
### Audio
- [class SCNAudioSource](scnaudiosource.md)
  A simple, reusable audio source—music or sound effects loaded from a file—for use in positional audio playback.
- [class SCNAudioPlayer](scnaudioplayer.md)
  A controller for playback of a positional audio source in a SceneKit scene.
### Renderer Customization
- [protocol SCNShadable](scnshadable.md)
  Methods for customizing SceneKit’s rendering of geometry and materials using Metal or OpenGL shader programs.
- [class SCNProgram](scnprogram.md)
  A complete Metal or OpenGL shader program that replaces SceneKit’s rendering of a geometry or material.
- [protocol SCNBufferStream](scnbufferstream.md)
  An object that manages a Metal buffer used by a custom shader program.
- [class SCNTechnique](scntechnique.md)
  A specification for augmenting or postprocessing SceneKit’s rendering of a scene using additional drawing passes with custom Metal or OpenGL shaders.
- [protocol SCNTechniqueSupport](scntechniquesupport.md)
  The common interface for SceneKit objects that support multipass rendering using [`SCNTechnique`](scntechnique.md) objects.
- [protocol SCNNodeRendererDelegate](scnnoderendererdelegate.md)
  Methods you can implement to use your own custom Metal or OpenGL drawing code to render content for a node.
- [Postprocessing a Scene With Custom Symbols](postprocessing-a-scene-with-custom-symbols.md)
  Create visual effects in a scene by defining a rendering technique with custom symbols.
### Scene Asset Import
- [class SCNSceneSource](scnscenesource.md)
  An object that manages the data-reading tasks associated with loading scene contents from a file or data.
### JavaScript
- [func SCNExportJavaScriptModule(JSContext)](scnexportjavascriptmodule(_:).md)
  Makes SceneKit classes and global constants available to the specified JavaScript context.
### SceneKit Data Types
- [SceneKit 3D Data Types](scenekit-3d-data-types.md)
  SceneKit-specific vectors, matrices, and related functions and operations.
### Macros
- [Macros](scenekit-macros.md)
### Reference
- [SceneKit Enumerations](scenekit-enumerations.md)
- [SceneKit Constants](scenekit-constants.md)
  Constants used throughout the SceneKit framework.
### Structures
- [struct SceneView](sceneview.md)
  A SwiftUI view for displaying 3D SceneKit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SceneKit)*