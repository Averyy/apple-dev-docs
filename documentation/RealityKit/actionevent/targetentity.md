# targetEntity

**Framework**: RealityKit  
**Kind**: property

The entity the bind target references.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
let targetEntity: Entity?
```

#### Discussion

For example, if a bind target references an entity’s transform (i.e. `.transform`), this value is set to that entity.

This may differ from the entity property in the playback controller if the bind target references an entity other than the entity that the animation was played on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionevent/targetentity)*