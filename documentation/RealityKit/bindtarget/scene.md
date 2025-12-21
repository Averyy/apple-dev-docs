# scene(_:)

**Framework**: RealityKit  
**Kind**: method

Generates a bind path from a particular scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
static func scene(_ name: String) -> BindTarget.ScenePath
```

## See Also

- [BindTarget.ScenePath](bindtarget/scenepath.md)
  A bind path for a particular scene.
- [static func anchorEntity(String) -> BindTarget.EntityPath](bindtarget/anchorentity(_:).md)
  Generates a complex bind path from a particular anchor entity in the scene.
- [static func entity(String) -> BindTarget.EntityPath](bindtarget/entity(_:).md)
  Generates a complex bind path from a particular child entity of the current entity.
- [BindTarget.EntityPath](bindtarget/entitypath.md)
  A bind path context for a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/scene(_:))*