# physicsField

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The physics field associated with the node.

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
var physicsField: SCNPhysicsField? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNPhysicsField * physicsField;
```

#### Discussion

Physics fields apply forces to other physics bodies in a specified area around their node. For example, a SCNPhysicsDragField field slows all physics bodies that pass through its area. For a full list of field types and their effects, see [`SCNPhysicsField`](../scnphysicsfield.md).

A node can contain both a physics body that defines collision behavior and a physics field that defines forces in its area. For example, two nodes containing physics bodies and radial gravity fields will be attracted to one another, but will bounce off each other when they collide.

## See Also

### Adding Physics to a Node
- [var physicsBody: SCNPhysicsBody?](./physicsbody.md)
  The physics body associated with the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/physicsfield)*