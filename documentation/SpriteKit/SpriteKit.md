# SpriteKit

**Framework**: SpriteKit  
**Kind**: module

Add high-performance 2D content with smooth animations to your app, or create a game with a high-level set of 2D game-based tools.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 10.0+

#### Overview

SpriteKit is a general-purpose framework for drawing shapes, particles, text, images, and video in two dimensions. It leverages Metal to achieve high-performance rendering, while offering a simple programming interface to make it easy to create games and other graphics-intensive apps. Using a rich set of animations and physics behaviors, you can quickly add life to your visual elements and gracefully transition between screens.

SpriteKit is supported in iOS, macOS, tvOS, and watchOS, and it integrates well with frameworks such as GameplayKit and SceneKit. You can use SpriteKit in a compatible iPhone or iPad app running in visionOS, but don’t use it in apps you create specifically for visionOS.

## Topics

### Essentials
- [Drawing SpriteKit Content in a View](drawing-spritekit-content-in-a-view.md)
  Display visual content using SpriteKit.
- [class SKScene](skscene.md)
  An object that organizes all of the active SpriteKit content.
- [Nodes for Scene Building](nodes-for-scene-building.md)
  Define the appearance or layout of scene content.
### Scene Renderers
- [Choosing a SpriteKit Scene Renderer](choosing-a-spritekit-scene-renderer.md)
  Compare the different ways to display a SpriteKit scene.
- [class SKView](skview.md)
  A view subclass that renders a SpriteKit scene.
- [class SKRenderer](skrenderer.md)
  An object that renders a scene into a custom Metal rendering pipeline and drives the scene update cycle.
- [class WKInterfaceSKScene](../WatchKit/WKInterfaceSKScene.md)
  A visual WatchKit element that displays a SpriteKit scene.
### Textures
- [Maximizing Texture Performance](maximizing-texture-performance.md)
  Speed up image display and enable more images to be displayed at one time.
- [class SKTexture](sktexture.md)
  An image, decoded on the GPU, that can be used to render various SpriteKit objects.
- [class SKTextureAtlas](sktextureatlas.md)
  A collection of textures optimized for storage and drawing performance.
- [class SKMutableTexture](skmutabletexture.md)
  A texture whose contents can be dynamically updated.
### Animation
- [Getting Started with Actions](getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [class SKAction](skaction.md)
  An object that is run by a node to change its structure or content.
### Constraints
- [class SKConstraint](skconstraint.md)
  A specification for constraining a node’s position or rotation.
- [class SKReachConstraints](skreachconstraints.md)
  A specification of the degree of freedom when solving inverse kinematics.
### Mathematical Tools
- [class SKKeyframeSequence](skkeyframesequence.md)
  An object that performs interpolation between values specified at different times (keyframes).
- [class SKRange](skrange.md)
  A definition of a range of floating-point values.
- [class SKRegion](skregion.md)
  The definition of an arbitrary area.
### Physics Simulation
- [Getting Started with Physics](getting-started-with-physics.md)
  Simulate gravity, acceleration, collision detection, or joints.
- [class SKPhysicsWorld](skphysicsworld.md)
  The driver of the physics engine in a scene; it exposes the ability for you to configure and query the physics system.
- [class SKPhysicsBody](skphysicsbody.md)
  An object that adds physics simulation to a node.
- [class SKPhysicsContact](skphysicscontact.md)
  A description of the contact between two physics bodies.
- [protocol SKPhysicsContactDelegate](skphysicscontactdelegate.md)
  Methods your app can implement to respond when physics bodies come into contact.
- [class SKFieldNode](skfieldnode.md)
  A node that applies physics effects to nearby nodes.
### Physics Joints
- [Working with Inverse Kinematics](working-with-inverse-kinematics.md)
  Gain fine-tuned control of objects that are connected by joints.
- [class SKPhysicsJoint](skphysicsjoint.md)
  The abstract superclass for objects that connect physics bodies.
- [class SKPhysicsJointFixed](skphysicsjointfixed.md)
  A joint that fuses two physics bodies together at a reference point.
- [class SKPhysicsJointLimit](skphysicsjointlimit.md)
  A joint that imposes a maximum distance between two physics bodies, as if they were connected by a rope.
- [class SKPhysicsJointPin](skphysicsjointpin.md)
  A joint that pins together two physics bodies, allowing independent rotation.
- [class SKPhysicsJointSliding](skphysicsjointsliding.md)
  A joint that allows two physics bodies to slide along an axis.
- [class SKPhysicsJointSpring](skphysicsjointspring.md)
  A joint that simulates a spring connecting two physics bodies.
### Tiling
- [class SKTileMapNode](sktilemapnode.md)
  A two-dimensional array of images.
- [class SKTileDefinition](sktiledefinition.md)
  A single tile that can be repeated in a tile map.
- [class SKTileGroup](sktilegroup.md)
  A set of tiles that collectively define one type of terrain.
- [class SKTileGroupRule](sktilegrouprule.md)
  Rules that describe how various tiles should be placed in a map.
- [class SKTileSet](sktileset.md)
  A container for related tile groups.
### Shaders
- [class SKShader](skshader.md)
  An object that allows you to apply a custom fragment shader.
- [class SKAttribute](skattribute.md)
  A specification for dynamic per-node data used with a custom shader.
- [class SKAttributeValue](skattributevalue.md)
  A container for dynamic shader data associated with a node.
- [class SKUniform](skuniform.md)
  A container for uniform shader data.
### Warping
- [class SKWarpGeometry](skwarpgeometry.md)
  A definition for a deformation of nodes that conform to [`SKWarpable`](skwarpable.md).
- [class SKWarpGeometryGrid](skwarpgeometrygrid.md)
  A definition for a grid-based deformation of nodes that conform to [`SKWarpable`](skwarpable.md).
- [protocol SKWarpable](skwarpable.md)
  A protocol for objects that can be warped and animated by an [`SKWarpGeometry`](skwarpgeometry.md).
### Reference
- [SpriteKit Enumerations](spritekit-enumerations.md)
  Enumerations used across SpriteKit.
- [SpriteKit Data Types](spritekit-data-types.md)
  Data types used across SpriteKit.
- [SpriteKit Constants](spritekit-constants.md)
  Constants used across SpriteKit.
- [SpriteKit Type Aliases](spritekit-type-aliases.md)
  Type aliases used across SpriteKit.
- [SpriteKit Variables](spritekit-variables.md)
  Global variables and macros used across SpriteKit.
### Structures
- [struct SpriteView](spriteview.md)
  A SwiftUI view that renders a SpriteKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SpriteKit)*