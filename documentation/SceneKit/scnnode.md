# SCNNode

**Framework**: SceneKit  
**Kind**: class

A structural element of a scene graph, representing a position and transform in a 3D coordinate space, to which you can attach geometry, lights, cameras, or other displayable content.

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
class SCNNode
```

## Mentions

- [Animating SceneKit Content](animating-scenekit-content.md)

#### Overview

An [`SCNNode`](scnnode.md) object by itself has no visible content when the scene containing it is rendered—it represents only a coordinate space transform (position, orientation, and scale) relative to its parent node. To construct a scene, you use a hierarchy of nodes to create its structure, then add lights, cameras, and geometry to nodes to create visible content.

##### Nodes Determine the Structure of a Scene

The hierarchy of nodes, or , in a scene defines both the organization of its contents and your ability to present and manipulate those contents using SceneKit. You may create a node hierarchy programmatically using SceneKit, load one from a file created using 3D authoring tools, or combine the two approaches. SceneKit provides many utilities for organizing and searching the scene graph—for details, see the methods in Managing the Node Hierarchy and Searching the Node Hierarchy.

The [`rootNode`](scnscene/rootnode.md) object in a scene defines the coordinate system of the world rendered by SceneKit. Each child node you add to this root node creates its own coordinate system, which is in turn inherited by its own children. You determine the transformation between coordinate systems using the node’s [`position`](scnnode/position.md), [`rotation`](scnnode/rotation.md), and [`scale`](scnnode/scale.md) properties properties (or directly using its [`transform`](scnnode/transform.md) property).

You use a hierarchy of nodes and transformations to model the contents of your scene in a way that suits the needs of your app. For example, if your app presents an animated view of a solar system, you can construct a node hierarchy that models celestial bodies relative to one another: Each planet can be a node, with its orbit and its current position in that orbit defined in the coordinate system of the sun. A planet node defines its own coordinate space, useful both for specifying the planet’s rotation and the orbits of its moons (each of which is a child node of its planet). With this scene hierarchy, you can easily add realistic animation to the scene—animating both the revolution of a moon around its planet and the planet around the sun will combine the animations so that the moon follows the planet.

##### A Nodes Attachments Define Visual Content and Behavior

The node hierarchy determines the spatial and logical structure of a scene, but not its visible contents. You add 2D and 3D objects to a scene by attaching [`SCNGeometry`](scngeometry.md) objects to nodes. (Geometries, in turn, have attached [`SCNMaterial`](scnmaterial.md) objects that determine their appearance.) To shade the geometries in a scene with light and shadow effects, add nodes with attached [`SCNLight`](scnlight.md) objects. To control the viewpoint from which the scene appears when rendered, add nodes with attached [`SCNCamera`](scncamera.md) objects.

To add physics-based behaviors and special effects to SceneKit content, use other types of node attachments. For example, an [`SCNPhysicsBody`](scnphysicsbody.md) object defines a node’s characteristics for physics simulation, and an [`SCNPhysicsField`](scnphysicsfield.md) object applies forces to physics bodies in an area around the node. An [`SCNParticleSystem`](scnparticlesystem.md) object attached to a node renders particle effects such as fire, rain, or falling leaves in the space defined by a node.

To improve performance, SceneKit can share attachments between multiple nodes. For example, in a racing game that includes many identical cars, the scene graph would contain many nodes—one to position and animate each car—but all car nodes would reference the same geometry object.

## Topics

### Creating a Node
- [init(geometry: SCNGeometry?)](scnnode/init(geometry:).md)
  Creates and returns a node object with the specified geometry attached.
### Managing the Node’s Transform
- [var simdTransform: simd_float4x4](scnnode/simdtransform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var simdPosition: simd_float3](scnnode/simdposition.md)
  The translation applied to the node. Animatable.
- [var simdRotation: simd_float4](scnnode/simdrotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var simdEulerAngles: simd_float3](scnnode/simdeulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var simdOrientation: simd_quatf](scnnode/simdorientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var simdScale: simd_float3](scnnode/simdscale.md)
  The scale factor applied to the node. Animatable.
- [var simdPivot: simd_float4x4](scnnode/simdpivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.
### Managing Node Content
- [var name: String?](scnnode/name.md)
  A name associated with the node.
- [var light: SCNLight?](scnnode/light.md)
  The light attached to the node.
- [var camera: SCNCamera?](scnnode/camera.md)
  The camera attached to the node.
- [var geometry: SCNGeometry?](scnnode/geometry.md)
  The geometry attached to the node.
- [var morpher: SCNMorpher?](scnnode/morpher.md)
  The morpher object responsible for blending the node’s geometry.
- [var skinner: SCNSkinner?](scnnode/skinner.md)
  The skinner object responsible for skeletal animations of node’s contents.
- [var categoryBitMask: Int](scnnode/categorybitmask.md)
  A mask that defines which categories the node belongs to.
- [protocol SCNBoundingVolume](scnboundingvolume.md)
  Methods common to the [`SCNNode`](scnnode.md) and [`SCNGeometry`](scngeometry.md) classes for measuring location and size.
### Constraining Node Behavior
- [var constraints: [SCNConstraint]?](scnnode/constraints.md)
  A list of constraints affecting the node’s transformation.
### Working with Node Animation
- [var presentation: SCNNode](scnnode/presentation.md)
  A node object representing the state of the node as it currently appears onscreen.
- [var isPaused: Bool](scnnode/ispaused.md)
  A Boolean value that determines whether to run actions and animations attached to the node and its child nodes.
### Modifying the Node Visibility
- [var isHidden: Bool](scnnode/ishidden.md)
  A Boolean value that determines the visibility of the node’s contents. Animatable.
- [var opacity: CGFloat](scnnode/opacity.md)
  The opacity value of the node. Animatable.
- [var renderingOrder: Int](scnnode/renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var castsShadow: Bool](scnnode/castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [var movabilityHint: SCNMovabilityHint](scnnode/movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.
- [enum SCNMovabilityHint](scnmovabilityhint.md)
  Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](scnnode/movabilityhint.md) property.
### Managing the Node Hierarchy
- [var parent: SCNNode?](scnnode/parent.md)
  The node’s parent in the scene graph hierarchy.
- [var childNodes: [SCNNode]](scnnode/childnodes.md)
  An array of the node’s children in the scene graph hierarchy.
- [func addChildNode(SCNNode)](scnnode/addchildnode(_:).md)
  Adds a node to the node’s array of children.
- [func insertChildNode(SCNNode, at: Int)](scnnode/insertchildnode(_:at:).md)
  Adds a node to the node’s array of children at a specified index.
- [func removeFromParentNode()](scnnode/removefromparentnode.md)
  Removes the node from its parent’s array of child nodes.
- [func replaceChildNode(SCNNode, with: SCNNode)](scnnode/replacechildnode(_:with:).md)
  Removes a child from the node’s array of children and inserts another node in its place.
### Searching the Node Hierarchy
- [func childNodes(passingTest: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]](scnnode/childnodes(passingtest:).md)
  Returns all nodes in the node’s child node subtree that satisfy the test applied by a block.
- [func childNode(withName: String, recursively: Bool) -> SCNNode?](scnnode/childnode(withname:recursively:).md)
  Returns the first node in the node’s child node subtree with the specified name.
- [func enumerateChildNodes((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](scnnode/enumeratechildnodes(_:).md)
  Executes the specified block for each of the node’s child and descendant nodes.
- [func enumerateHierarchy((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](scnnode/enumeratehierarchy(_:).md)
  Executes the specified block for each of the node’s child and descendant nodes, as well as for the node itself.
### Customizing Node Rendering
- [var filters: [CIFilter]?](scnnode/filters.md)
  An array of Core Image filters to be applied to the rendered contents of the node.
- [var rendererDelegate: (any SCNNodeRendererDelegate)?](scnnode/rendererdelegate.md)
  An object responsible for rendering custom contents for the node using Metal or OpenGL.
### Adding Physics to a Node
- [var physicsBody: SCNPhysicsBody?](scnnode/physicsbody.md)
  The physics body associated with the node.
- [var physicsField: SCNPhysicsField?](scnnode/physicsfield.md)
  The physics field associated with the node.
### Working with Particle Systems
- [func addParticleSystem(SCNParticleSystem)](scnnode/addparticlesystem(_:).md)
  Attaches a particle system to the node.
- [var particleSystems: [SCNParticleSystem]?](scnnode/particlesystems.md)
  The particle systems attached to the node.
- [func removeParticleSystem(SCNParticleSystem)](scnnode/removeparticlesystem(_:).md)
  Removes a particle system attached to the node.
- [func removeAllParticleSystems()](scnnode/removeallparticlesystems.md)
  Removes any particle systems directly attached to the node.
### Working with Positional Audio
- [func addAudioPlayer(SCNAudioPlayer)](scnnode/addaudioplayer(_:).md)
  Adds the specified auto player to the node and begins playback.
- [var audioPlayers: [SCNAudioPlayer]](scnnode/audioplayers.md)
  The audio players currently attached to the node.
- [func removeAudioPlayer(SCNAudioPlayer)](scnnode/removeaudioplayer(_:).md)
  Removes the specified audio player from the node, stopping playback.
- [func removeAllAudioPlayers()](scnnode/removeallaudioplayers.md)
  Removes all audio players attached to the node, stopping playback.
### Copying a Node
- [func clone() -> Self](scnnode/clone.md)
  Creates a copy of the node and its children.
- [func flattenedClone() -> Self](scnnode/flattenedclone.md)
  Creates an optimized copy of the node and its children.
### Hit-Testing
- [func hitTestWithSegment(from: SCNVector3, to: SCNVector3, options: [String : Any]?) -> [SCNHitTestResult]](scnnode/hittestwithsegment(from:to:options:).md)
  Searches the node’s child node subtree for objects intersecting a line segment between two specified points.
- [struct SCNHitTestOption](scnhittestoption.md)
  Options affecting the behavior of SceneKit hit-testing methods.
### Performing Node-Relative Operations
- [func simdRotate(by: simd_quatf, aroundTarget: simd_float3)](scnnode/simdrotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func simdLocalTranslate(by: simd_float3)](scnnode/simdlocaltranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func simdLocalRotate(by: simd_quatf)](scnnode/simdlocalrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func simdLook(at: simd_float3)](scnnode/simdlook(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func simdLook(at: simd_float3, up: simd_float3, localFront: simd_float3)](scnnode/simdlook(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.
### Calculating Node-Relative Transforms
- [class var simdLocalRight: simd_float3](scnnode/simdlocalright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var simdLocalUp: simd_float3](scnnode/simdlocalup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [class var simdLocalFront: simd_float3](scnnode/simdlocalfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var simdWorldRight: simd_float3](scnnode/simdworldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [var simdWorldUp: simd_float3](scnnode/simdworldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var simdWorldFront: simd_float3](scnnode/simdworldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.
### Managing Transforms in World Space
- [var simdWorldTransform: simd_float4x4](scnnode/simdworldtransform.md)
  The world transform applied to the node.
- [var simdWorldOrientation: simd_quatf](scnnode/simdworldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
- [var simdWorldPosition: simd_float3](scnnode/simdworldposition.md)
  The node’s position relative to the scene’s world coordinate space.
### Converting Between Coordinate Spaces
- [func simdConvertPosition(simd_float3, from: SCNNode?) -> simd_float3](scnnode/simdconvertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func simdConvertPosition(simd_float3, to: SCNNode?) -> simd_float3](scnnode/simdconvertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func simdConvertTransform(simd_float4x4, from: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func simdConvertTransform(simd_float4x4, to: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func simdConvertVector(simd_float3, from: SCNNode?) -> simd_float3](scnnode/simdconvertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func simdConvertVector(simd_float3, to: SCNNode?) -> simd_float3](scnnode/simdconvertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.
### Handling UI Focus
- [var focusBehavior: SCNNodeFocusBehavior](scnnode/focusbehavior.md)
  The focus behavior for a node.
- [enum SCNNodeFocusBehavior](scnnodefocusbehavior.md)
  Options for the focusable states of a SceneKit node.
### Working with GameplayKit
- [var entity: GKEntity?](scnnode/entity.md)
  The GameplayKit entity this node represents.
### Managing the Node’s Transform (SceneKit Types)
- [var transform: SCNMatrix4](scnnode/transform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var position: SCNVector3](scnnode/position.md)
  The translation applied to the node. Animatable.
- [var rotation: SCNVector4](scnnode/rotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var eulerAngles: SCNVector3](scnnode/eulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var orientation: SCNQuaternion](scnnode/orientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var scale: SCNVector3](scnnode/scale.md)
  The scale factor applied to the node. Animatable.
- [var pivot: SCNMatrix4](scnnode/pivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.
### Performing Node-Relative Operations (SceneKit Types)
- [func rotate(by: SCNQuaternion, aroundTarget: SCNVector3)](scnnode/rotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func localTranslate(by: SCNVector3)](scnnode/localtranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func localRotate(by: SCNQuaternion)](scnnode/localrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func look(at: SCNVector3)](scnnode/look(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func look(at: SCNVector3, up: SCNVector3, localFront: SCNVector3)](scnnode/look(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.
### Calculating Node-Relative Transforms (SceneKit Types)
- [class var localRight: SCNVector3](scnnode/localright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var localUp: SCNVector3](scnnode/localup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [class var localFront: SCNVector3](scnnode/localfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var worldRight: SCNVector3](scnnode/worldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [var worldUp: SCNVector3](scnnode/worldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var worldFront: SCNVector3](scnnode/worldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.
### Managing Transforms in World Space (SceneKit Types)
- [var worldTransform: SCNMatrix4](scnnode/worldtransform.md)
  The world transform applied to the node.
- [func setWorldTransform(SCNMatrix4)](scnnode/setworldtransform(_:).md)
  Sets the world transform applied to the node.
- [var worldOrientation: SCNQuaternion](scnnode/worldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
- [var worldPosition: SCNVector3](scnnode/worldposition.md)
  The node’s position relative to the scene’s world coordinate space.
### Converting Between Coordinate Spaces (SceneKit Types)
- [func convertPosition(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func convertPosition(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func convertTransform(SCNMatrix4, from: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func convertTransform(SCNMatrix4, to: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func convertVector(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func convertVector(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SCNReferenceNode](scnreferencenode.md)
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
- [SCNActionable](scnactionable.md)
- [SCNAnimatable](scnanimatable.md)
- [SCNBoundingVolume](scnboundingvolume.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)

## See Also

- [Organizing a Scene with Nodes](organizing-a-scene-with-nodes.md)
  Use nodes to define the structure of a scene.
- [class SCNReferenceNode](scnreferencenode.md)
  A scene graph node that serves as a placeholder for content to be loaded from a separate scene file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode)*