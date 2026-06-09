# AnimationGraphComponent.ActiveTag

**Framework**: RealityKit  
**Kind**: struct

Contains debug information of a single tag within a compiled animation graph, used for inspection and debugging.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ActiveTag
```

## Topics

### Identifying the tag
- [let id: Int](animationgraphcomponent/activetag/id.md)
  Returns the id of the tag.
### Instance Properties
- [let name: String](animationgraphcomponent/activetag/name.md)
  Returns the name of the tag.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var activeTags: [AnimationGraphComponent.ActiveTag]](animationgraphcomponent/activetags.md)
  The tags that were active during the last graph evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activetag)*