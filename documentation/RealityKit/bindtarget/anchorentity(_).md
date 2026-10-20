# anchorEntity(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Generates a complex bind path from a particular anchor entity in the scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
static func anchorEntity(_ name: String) -> BindTarget.EntityPath
```

## See Also

### Targeting entities and scenes
- [static func scene(String) -> BindTarget.ScenePath](./scene%28_%29.md)
  Generates a bind path from a particular scene.
- [BindTarget.ScenePath](./scenepath.md)
  A bind path for a particular scene.
- [static func entity(String) -> BindTarget.EntityPath](./entity%28_%29.md)
  Generates a complex bind path from a particular child entity of the current entity.
- [BindTarget.EntityPath](./entitypath.md)
  A bind path context for a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/anchorentity(_:))*