# path

**Framework**: Model I/O  
**Kind**: property

A path that identifies the object in an asset’s object hierarchy using object names.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var path: String { get }
```

#### Discussion

Model I/O forms a path for each object in an asset’s object hierarchy by concatenating the [`name`](mdlnamed/name.md) properties of objects in the hierarchy, separated by slashes and preceded by an initial slash.

> **Note**:  When using an object’s name in a path, Model I/O converts all characters not in the set `[A-Z][a-z][0-9][:-_.]` to underscores.

 When using an object’s name in a path, Model I/O converts all characters not in the set `[A-Z][a-z][0-9][:-_.]` to underscores.

For example, a mesh in an asset modeling a dining room scene might have the path `/meshes/table_anchor/chair1`, where “meshes” is one of the top-level children of the asset, “table anchor” is a [`MDLObject`](mdlobject.md) instance providing a transform inherited by several meshes, and “chair1” is the name of a [`MDLMesh`](mdlmesh.md) object.

## See Also

- [var parent: MDLObject?](mdlobject/parent.md)
  The parent object that contains this object.
- [var children: any MDLObjectContainerComponent](mdlobject/children.md)
  A component that manages this object’s collection of children.
- [func addChild(MDLObject)](mdlobject/addchild(_:).md)
  Adds a child object to this object, creating a container for the object’s children if necessary.
- [func enumerateChildObjects(of: AnyClass, root: MDLObject, using: (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)](mdlobject/enumeratechildobjects(of:root:using:stoppointer:).md)
  Executes the specified block using each object in this object’s child hierarchy.
- [func atPath(String) -> MDLObject](mdlobject/atpath(_:).md)
  Returns the child object at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/path)*