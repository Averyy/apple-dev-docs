# BindTarget.ScenePath

**Framework**: RealityKit  
**Kind**: struct

A bind path for a particular scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct ScenePath
```

#### Overview

This structure defines an absolute bind path for a scene. You determine the scene that a particular instance references by specifying the scene’s name as the argument to [`BindPath.Part.scene(_:)`](bindpath/part/scene(_:).md).

## Topics

### Accessing the anchor entity
- [func anchorEntity(String) -> BindTarget.EntityPath](bindtarget/scenepath/anchorentity(_:).md)
  A path for the scene’s anchor entity.
### Accessing the bind target
- [var `self`: BindTarget](bindtarget/scenepath/self.md)
  A bind target for the scene.

## See Also

- [static func scene(String) -> BindTarget.ScenePath](bindtarget/scene(_:).md)
  Generates a bind path from a particular scene.
- [static func anchorEntity(String) -> BindTarget.EntityPath](bindtarget/anchorentity(_:).md)
  Generates a complex bind path from a particular anchor entity in the scene.
- [static func entity(String) -> BindTarget.EntityPath](bindtarget/entity(_:).md)
  Generates a complex bind path from a particular child entity of the current entity.
- [BindTarget.EntityPath](bindtarget/entitypath.md)
  A bind path context for a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/scenepath)*