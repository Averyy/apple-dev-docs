# emitter::setGroup

**Framework**: Compute Graph  
**Kind**: func

Sets the element group(s) for spawn requests from this emitter.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void emitter::setGroup(int activeGroup, int sequentialGroups)
```

#### Discussion

> **Note**: ![Graph](/images/com.apple.computegraph/emitter__setGroup.svg)

> **Note**: Reads from emitter state `int activeGroupIndex`, if it exists

> **Note**: Reads from emitter state `int sequentialGroupCount`, if it exists

## Parameters

- `activeGroup`: Index of the first active group
- `sequentialGroups`: Number of groups to spawn. Only used when the emitter’s groupMode is `sequential`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/emitter/setgroup)*