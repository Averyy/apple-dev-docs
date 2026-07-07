# group::elementActiveInGroup

**Framework**: Compute Graph  
**Kind**: func

Returns the number of currently active elements in the group.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
int group::elementActiveInGroup()
```

#### Return Value

The count of active elements currently in the group

#### Discussion

Use this function to determine how many particles are currently alive in the group, which may be less than the maximum if some particles have expired or not yet spawned.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/c0537c260b0ca1dce4eb05f73cff5312/group__elementActiveInGroup.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/group/elementactiveingroup)*