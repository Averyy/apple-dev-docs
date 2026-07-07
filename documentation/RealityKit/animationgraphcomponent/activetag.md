# AnimationGraphComponent.ActiveTag

**Framework**: RealityKit  
**Kind**: struct

A graph-level signal raised by the graph while certain states are active.

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

#### Overview

Use tags to observe outputs the graph emits back to the rest of the application — for example, to play a footstep sound while the character is in a “running” state. The graph reports tags that are currently active or that fired during the most recent evaluation tick through [`activeTags`](animationgraphcomponent/activetags.md).

## Topics

### Identifying the tag
- [let id: Int](animationgraphcomponent/activetag/id.md)
  The unique identifier of the tag within the compiled graph.
### Instance Properties
- [let name: String](animationgraphcomponent/activetag/name.md)
  The author-supplied name of the tag from the graph definition.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var activeTags: [AnimationGraphComponent.ActiveTag]](animationgraphcomponent/activetags.md)
  The tags that were active or fired during the most recent graph evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activetag)*