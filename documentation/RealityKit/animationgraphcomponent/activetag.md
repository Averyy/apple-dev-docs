# AnimationGraphComponent.ActiveTag

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A graph-level signal raised by the graph while certain states are active.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ActiveTag
```

## Overview

Use tags to observe outputs the graph emits back to the rest of the application — for example, to play a footstep sound while the character is in a “running” state. The graph reports tags that are currently active or that fired during the most recent evaluation tick through [`activeTags`](./activetags.md).

## Topics

### Identifying the tag
- [let id: Int](./activetag/id.md)
  The unique identifier of the tag within the compiled graph.
### Instance Properties
- [let name: String](./activetag/name.md)
  The author-supplied name of the tag from the graph definition.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing active tags
- [var activeTags: [AnimationGraphComponent.ActiveTag]](./activetags.md)
  The tags that were active or fired during the most recent graph evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activetag)*