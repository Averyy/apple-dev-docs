# nodeWithMDLObject:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a node from the specified Model I/O object.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) nodeWithMDLObject:(MDLObject *) mdlObject;
```

## Return Value

A new node object.

## Discussion

The Model I/O framework provides universal support for import, export, description, and processing of several 3D asset file formats and related resources. (For details, see [Model I/O](../../ModelIO/ModelIO.md).)

The [`MDLObject`](../../ModelIO/mdlobject.md) class is the most general class in ModelIO, representing any object that can be contained in a scene file, along with the object’s position in the scene and its relationships to other objects. Use this method to import any Model I/O object, creating an equivalent [`SCNNode`](../scnnode.md) object. If the Model I/O object is of a more specific class, SceneKit imports that object as an attachment to the node—for example, using this method to import a [`MDLMesh`](../../ModelIO/mdlmesh.md) object creates a SceneKit node with an attached geometry, and importing a [`MDLLight`](../../ModelIO/mdllight.md) object creates a node with an attached light.

## Parameters

- `mdlObject`: A Model I/O object.

## See Also

### Creating a Node
- [+ node](./node.md)
  Creates and returns a node object.
- [init(geometry: SCNGeometry?)](./init%28geometry%29.md)
  Creates and returns a node object with the specified geometry attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/nodewithmdlobject:)*