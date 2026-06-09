# group::elementIndexInGroup

**Framework**: ComputeGraph  
**Kind**: func

Returns the index of the current element within its group.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
int group::elementIndexInGroup()
```

#### Return Value

The zero-based index of the current element within its group

#### Discussion

Use this function to identify which particle within the group is being processed, allowing you to create unique behaviors for different particles in the same group.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/b59262f7384bdc796e0535908b818d60/group__elementIndexInGroup.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/group/elementindexingroup)*