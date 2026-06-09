# emitter::setGroup

**Framework**: ComputeGraph  
**Kind**: func

Sets the element group(s) for spawn requests from this emitter.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void emitter::setGroup(int activeGroup, int sequentialGroups)
```

#### Discussion

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/12f77d465ae272de6598a7fbc1de9c8f/emitter__setGroup.svg)

> **Note**: Reads from emitter state `int activeGroupIndex`, if it exists

> **Note**: Reads from emitter state `int sequentialGroupCount`, if it exists

## Parameters

- `activeGroup`: Index of the first active group
- `sequentialGroups`: Number of groups to spawn. Only used when the emitter’s groupMode is `sequential`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/emitter/setgroup)*