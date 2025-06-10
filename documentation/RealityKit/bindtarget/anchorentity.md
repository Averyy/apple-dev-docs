# anchorEntity(_:)

**Framework**: RealityKit  
**Kind**: method

Generates a complex bind path from a particular anchor entity in the scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
static func anchorEntity(_ name: String) -> BindTarget.EntityPath
```

## See Also

- [static func scene(String) -> BindTarget.ScenePath](bindtarget/scene(_:).md)
  Generates a bind path from a particular scene.
- [BindTarget.ScenePath](bindtarget/scenepath.md)
  A bind path for a particular scene.
- [static func entity(String) -> BindTarget.EntityPath](bindtarget/entity(_:).md)
  Generates a complex bind path from a particular child entity of the current entity.
- [BindTarget.EntityPath](bindtarget/entitypath.md)
  A bind path context for a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/anchorentity(_:))*