# SKNode

**Framework**: SpriteKit  
**Kind**: class

The base class of all SpriteKit nodes.

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
@MainActor
class SKNode
```

## Mentions

- [Customizing the Behavior of a Node](customizing-the-behavior-of-a-node.md)
- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)
- [Using Base Nodes to Lay Out SpriteKit Content](using-base-nodes-to-lay-out-spritekit-content.md)
- [Detecting Changes at Each Step of an Animation](detecting-changes-at-each-step-of-an-animation.md)
- [Connecting Bodies with Joints](connecting-bodies-with-joints.md)
- [Resizing a Sprite in Nine Parts](resizing-a-sprite-in-nine-parts.md)
- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)
- [Searching the Node Tree](searching-the-node-tree.md)
- [Accessing and Modifying the Node Tree](accessing-and-modifying-the-node-tree.md)

#### Overview

`SKNode` provides base properties for its subclasses and it can be used as a container or layout tool for other nodes. For example, you might add a collection of nodes as children to an `SKNode` that all move together within the scene; because nodes inherit the properties of their parent, changing the parent node’s [`position`](sknode/position.md) propagates the change to its children as well.

`SKNode` does not draw any content itself. Its visual counterparts are listed in Nodes that Draw in [`Nodes for Scene Building`](nodes-for-scene-building.md).

## Topics

### First Steps
- [Getting Started with Nodes](getting-started-with-nodes.md)
  Learn about the fundamental properties that provide a foundation for all other nodes.
- [init()](sknode/init.md)
  Initializes a blank node.
- [convenience init?(fileNamed: String)](sknode/init(filenamed:).md)
  Creates a new node by loading an archive file from the game’s main bundle.
- [init?(coder: NSCoder)](sknode/init(coder:).md)
  Called when a node is initialized from an .sks file.
- [convenience init(fileNamed: String, securelyWithClasses: Set<AnyHashable>) throws](sknode/init(filenamed:securelywithclasses:).md)
### Positioning Content in a Scene
- [var position: CGPoint](sknode/position.md)
  The position of the node in its parent’s coordinate system.
### Querying the Content Size
- [var frame: CGRect](sknode/frame.md)
  A rectangle in the parent’s coordinate system that contains the node’s content, ignoring the node’s children.
- [func calculateAccumulatedFrame() -> CGRect](sknode/calculateaccumulatedframe.md)
  Returns a rectangle in the parent’s coordinate system that contains the position and size of itself and all child nodes.
### Configuring Draw Order
- [About Node Drawing Order](about-node-drawing-order.md)
  Understand how SpriteKit layers your scene’s nodes from top to bottom.
- [var zPosition: CGFloat](sknode/zposition.md)
  The height of the node relative to its parent.
### Scaling and Rotating
- [var zRotation: CGFloat](sknode/zrotation.md)
  The Euler rotation about the z axis (in radians).
- [func setScale(CGFloat)](sknode/setscale(_:).md)
  Sets the [`xScale`](sknode/xscale.md) and [`yScale`](sknode/yscale.md) properties of the node.
- [var xScale: CGFloat](sknode/xscale.md)
  A scaling factor that multiplies the width of a node and its children.
- [var yScale: CGFloat](sknode/yscale.md)
  A scaling factor that multiplies the height of a node and its children.
### Accessing Related Nodes
- [About SpriteKit Coordinate Systems](about-spritekit-coordinate-systems.md)
  Learn how a node conforms to its coordinate systems.
- [var scene: SKScene?](sknode/scene.md)
  The scene node that contains this node.
- [var parent: SKNode?](sknode/parent.md)
  The node’s parent node.
- [var children: [SKNode]](sknode/children.md)
  The node’s children.
### Modifying the Node Tree
- [Accessing and Modifying the Node Tree](accessing-and-modifying-the-node-tree.md)
  See the objects and functions you use to control the node tree’s composition.
- [func addChild(SKNode)](sknode/addchild(_:).md)
  Adds a node to the end of the receiver’s list of child nodes.
- [func insertChild(SKNode, at: Int)](sknode/insertchild(_:at:).md)
  Inserts a node into a specific position in the receiver’s list of child nodes.
- [func isEqual(to: SKNode) -> Bool](sknode/isequal(to:).md)
  Compares the parameter node to the receiving node.
- [func move(toParent: SKNode)](sknode/move(toparent:).md)
  Moves the node to a new parent node in the scene.
- [func removeFromParent()](sknode/removefromparent.md)
  Removes the receiving node from its parent.
- [func removeAllChildren()](sknode/removeallchildren.md)
  Removes all of the node’s children.
- [func removeChildren(in: [SKNode])](sknode/removechildren(in:).md)
  Removes a list of children from the receiving node.
- [func inParentHierarchy(SKNode) -> Bool](sknode/inparenthierarchy(_:).md)
  Returns a Boolean value that indicates whether the node is a descendant of the target node.
### Customizing Nodes
- [Customizing the Behavior of a Node](customizing-the-behavior-of-a-node.md)
  Organize your app’s logic and display code with nodes.
### Propagating Properties to Children
- [About Node Property Propagation](about-node-property-propagation.md)
  Learn which properties of a node affect its child nodes.
### Accessing Nodes by Name
- [Searching the Node Tree](searching-the-node-tree.md)
  Access nodes by name to avoid needing an instance variable.
- [var name: String?](sknode/name.md)
  The node’s assignable name.
- [func childNode(withName: String) -> SKNode?](sknode/childnode(withname:).md)
  Searches the children of the receiving node for a node with a specific name.
- [func enumerateChildNodes(withName: String, using: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)](sknode/enumeratechildnodes(withname:using:).md)
  Searches the children of the receiving node to perform processing for nodes that share a name.
- [subscript(String) -> [SKNode]](sknode/subscript(_:).md)
  Returns an array of nodes that match the name parameter.
### Altering Node Visibility
- [var alpha: CGFloat](sknode/alpha.md)
  The transparency value applied to the node’s contents.
- [var isHidden: Bool](sknode/ishidden.md)
  A Boolean value that determines whether a node and its descendants are rendered.
### Running Actions
- [Getting Started with Actions](getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [func run(SKAction)](sknode/run(_:).md)
  Adds an action to the list of actions executed by the node.
- [func run(SKAction, completion: () -> Void)](sknode/run(_:completion:).md)
  Adds an action to the list of actions executed by the node and schedules the argument block to be run upon completion of the action.
- [func run(SKAction, withKey: String)](sknode/run(_:withkey:).md)
  Adds an identifiable action to the list of actions executed by the node.
- [var speed: CGFloat](sknode/speed.md)
  A speed modifier applied to all actions executed by a node and its descendants.
- [var isPaused: Bool](sknode/ispaused.md)
  A Boolean value that determines whether actions on the node and its descendants are processed.
- [func action(forKey: String) -> SKAction?](sknode/action(forkey:).md)
  Returns an action associated with a specific key.
- [func hasActions() -> Bool](sknode/hasactions.md)
  Returns a Boolean value that indicates whether the node is executing actions.
- [func removeAllActions()](sknode/removeallactions.md)
  Ends and removes all actions from the node.
- [func removeAction(forKey: String)](sknode/removeaction(forkey:).md)
  Removes an action associated with a specific key.
### Adding Physics Behaviors
- [Getting Started with Physics Bodies](getting-started-with-physics-bodies.md)
  Create and assign a physics body to enable physics.
- [var physicsBody: SKPhysicsBody?](sknode/physicsbody.md)
  The physics body associated with the node.
### Constraining Node Position or Rotation
- [var constraints: [SKConstraint]?](sknode/constraints.md)
  A list of constraints to apply to the node.
- [var reachConstraints: SKReachConstraints?](sknode/reachconstraints.md)
  The reach constraints to apply to the node when executing a reach action.
### Detecting Collisions Manually
- [func intersects(SKNode) -> Bool](sknode/intersects(_:).md)
  Returns a Boolean value that indicates whether this node intersects the specified node.
### Adding GameplayKit Behaviors
- [var entity: GKEntity?](sknode/entity.md)
  The GameplayKit entity this node represents.
- [class func obstacles(fromNodeBounds: [SKNode]) -> [GKPolygonObstacle]](sknode/obstacles(fromnodebounds:).md)
  Converts each node into an obstacle by transforming its bounds into the scene’s coordinate system.
- [class func obstacles(fromNodePhysicsBodies: [SKNode]) -> [GKPolygonObstacle]](sknode/obstacles(fromnodephysicsbodies:).md)
  Converts each node into an obstacle by transforming the node’s physics body shape into the scene’s coordinate system.
- [class func obstacles(fromSpriteTextures: [SKNode], accuracy: Float) -> [GKPolygonObstacle]](sknode/obstacles(fromspritetextures:accuracy:).md)
  Turns each node into an obstacle by changing the node’s texture into a physics shape and converting it into the scene’s coordinate system.
### Handling User Input
- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)
  Enable your node to respond to user input, like touches or mouse clicks.
- [var isUserInteractionEnabled: Bool](sknode/isuserinteractionenabled.md)
  A Boolean value that indicates whether the node receives touch events.
- [var focusBehavior: SKNodeFocusBehavior](sknode/focusbehavior.md)
  The focus behavior for a node.
### Hit Testing
- [Understanding Hit-Testing](understanding-hit-testing.md)
  Learn how find child nodes at a given point by using hit-testing.
- [func contains(CGPoint) -> Bool](sknode/contains(_:).md)
  Returns a Boolean value that indicates whether a point lies inside the parent’s coordinate system.
- [func atPoint(CGPoint) -> SKNode](sknode/atpoint(_:).md)
  Returns the deepest visible descendant that intersects a point.
- [func nodes(at: CGPoint) -> [SKNode]](sknode/nodes(at:).md)
  Returns an array of all visible descendants that intersect a point.
### Converting Between Coordinate Systems of Different Nodes
- [Converting Coordinate Spaces](converting-coordinate-spaces.md)
  Convert positions across the various coordinate spaces in a scene.
- [func convert(CGPoint, from: SKNode) -> CGPoint](sknode/convert(_:from:).md)
  Converts a point from the coordinate system of another node in the node tree to the coordinate system of this node.
- [func convert(CGPoint, to: SKNode) -> CGPoint](sknode/convert(_:to:).md)
  Converts a point in this node’s coordinate system to the coordinate system of another node in the node tree.
### Adding Custom Data Without Subclassing
- [var userData: NSMutableDictionary?](sknode/userdata.md)
  A dictionary containing arbitrary data.
### Providing Accessibility
- [var accessibilityChildren: [Any]?](sknode/accessibilitychildren.md)
  An array of user interface elements that represent children of this element.
- [var accessibilityFrame: CGRect](sknode/accessibilityframe.md)
  The size of this user interface element, in screen points.
- [var accessibilityHelp: String?](sknode/accessibilityhelp.md)
  The help description of this user interface element; for example, the text shown in a tooltip.
- [var accessibilityLabel: String?](sknode/accessibilitylabel.md)
  A short description of this user interface element.
- [var accessibilityParent: AnyObject?](sknode/accessibilityparent.md)
  The user interface element that contains this element.
- [var accessibilityRole: String?](sknode/accessibilityrole.md)
  A string value describing the user interface element type; for example, a button.
- [var accessibilityRoleDescription: String?](sknode/accessibilityroledescription.md)
  A string value describing the user interface element name and type; for example, the Buy button.
- [var accessibilitySubrole: String?](sknode/accessibilitysubrole.md)
  A string that defines this user interface element’s subrole; for example, a full-screen button.
- [var isAccessibilityElement: Bool](sknode/isaccessibilityelement.md)
  A toggle you implement to indicate to the system whether this user interface element should be exposed to the user.
- [var isAccessibilityEnabled: Bool](sknode/isaccessibilityenabled.md)
  A toggle you implement to indicate to the system whether this user interface element should respond to user input.
- [func accessibilityHitTest(CGPoint) -> Any?](sknode/accessibilityhittest(_:).md)
  Returns the frontmost user interface element in the element hierarchy.
### Setting a Node’s Unique Attributes for a Shader
- [var attributeValues: [String : SKAttributeValue]](sknode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](sknode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader
- [func value(forAttributeNamed: String) -> SKAttributeValue?](sknode/value(forattributenamed:).md)
  The value of a shader attribute.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
- [NSResponder](../AppKit/NSResponder.md)
- [UIResponder](../UIKit/UIResponder.md)
### Inherited By
- [SK3DNode](sk3dnode.md)
- [SKAudioNode](skaudionode.md)
- [SKCameraNode](skcameranode.md)
- [SKCropNode](skcropnode.md)
- [SKEffectNode](skeffectnode.md)
- [SKEmitterNode](skemitternode.md)
- [SKFieldNode](skfieldnode.md)
- [SKLabelNode](sklabelnode.md)
- [SKLightNode](sklightnode.md)
- [SKReferenceNode](skreferencenode.md)
- [SKShapeNode](skshapenode.md)
- [SKSpriteNode](skspritenode.md)
- [SKTileMapNode](sktilemapnode.md)
- [SKTransformNode](sktransformnode.md)
- [SKVideoNode](skvideonode.md)
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
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Using Base Nodes to Lay Out SpriteKit Content](using-base-nodes-to-lay-out-spritekit-content.md)
  Use nonvisual nodes to define the layout of a scene.
- [class SKCameraNode](skcameranode.md)
  A node that determines which parts of the scene are visible within a view.
- [class SKReferenceNode](skreferencenode.md)
  A node that’s defined in an archived `.sks` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode)*